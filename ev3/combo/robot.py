#!/usr/bin/env pybricks-micropython
import math

from config import *


def sign(target):
    return 1 if target >= 0 else -1


def clip(x, min, max):
    if x < min:
        return min
    if x > max:
        return max
    return x


def is_black(reflection):
    return reflection < 15


def is_white(reflection):
    return reflection > 88


def is_right_white():
    return is_white(color_right.reflection())


def is_right_black():
    return is_black(color_right.reflection())


def get_delta(reflection):
    return reflection / 50 - 1


def need_terminate(terminate):
    if terminate is not None and terminate():
        print("Terminating")
        return True
    return False


GYRO_PID = [1, 0.5, 0.3, 0.3]
LINE_PID = [5, 5, 2, 0.3]


class PID:
    def __init__(self, pid):
        self.kp = pid[0]
        self.ki = pid[1]
        self.kd = pid[2]
        self.decay = pid[3]
        self.error_last = None
        self.error_i = 0

    def delta(self, error):
        self.error_i = self.error_i * self.decay + error
        error_d = 0 if self.error_last is None else error - self.error_last
        self.error_last = error
        return error * self.kp + self.error_i * self.ki + error_d * self.kd


class Robot:
    def __init__(self, accel=10):
        self.accel = accel
        self.speed = 0
        self.speed_last = 0
        self.turn_rate = 0
        robot.stop()

    def stop(self, stop=True):
        if stop:
            self.set_speed(0, 0)
            while not self.done():
                self.update()
            robot.drive(0, 0)

    def reset(self):
        state = robot.state()
        self.speed = self.speed_last = state[1]
        self.turn_rate = state[3]
        robot.reset()

    def set_speed(self, speed, turn_rate):
        #print("SPEED:", speed, turn_rate)
        self.speed = speed
        self.turn_rate = turn_rate
        self.update()

    def done(self):
        return abs(self.speed_last - self.speed) < 0.001

    def update(self):
        state = robot.state()

        # Skip update if not catching up
        if abs(self.speed_last - state[1]) > self.accel:
            return

        delta = clip(self.speed - self.speed_last, -self.accel, self.accel)
        self.speed_last += delta
        robot.drive(self.speed_last, self.turn_rate)
        
    def move(self, distance, speed, gyro_pid=None, gyro_angle=None, terminate=None, stop=False):
        self.reset()
        target_angle = gyro_angle if gyro_angle is not None else gyro.angle()
        print("Move:", distance, speed, target_angle)

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        pid = PID(gyro_pid or GYRO_PID)
        while robot.distance() * direction < target:
            if need_terminate(terminate):
                break
            delta = pid.delta(target_angle - gyro.angle())
            self.set_speed(speed_direction, delta)
            self.update()
        self.stop(stop)

        distance = robot.distance()
        print("Done:", distance, gyro.angle())
        return distance
        
    def turn(self, target_angle, speed, turn_rate, stop=False, terminate=None):
        current_angle = gyro.angle()
        print("Turn:", target_angle, speed, turn_rate, current_angle)
        self.reset()

        direction = sign(target_angle - current_angle)
        self.set_speed(speed, turn_rate * direction)
        
        while (target_angle - gyro.angle()) * direction > 0:
            if need_terminate(terminate):
                break
            self.update()
        self.stop(stop)
        print("Done:", gyro.angle())

    def follow(self, distance, speed, use_left=True, line_delta=20, line_pid=None, find_lane=False, stop=False, gradient=1):
        print("Follow:", distance, speed, line_pid)
        self.reset()

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        state = "find_lane_black" if find_lane else 'find_edge'
        state_prev = None
        pid = PID(line_pid or LINE_PID)

        while robot.distance() * direction < target:
            if state != state_prev:
                print(state)
                state_prev = state

            left = color_left.reflection()
            right = color_right.reflection()
            if state == "find_lane_black":
                if is_black(left) or is_black(right):
                    state = "find_lane_white"
                    if is_black(left):
                        self.set_speed(speed_direction, -line_delta * direction)
                    else:
                        self.set_speed(speed_direction, line_delta * direction)
            elif state == "find_lane_white":
                if is_white(left) and is_white(right):
                    state = "find_edge"
                    self.set_speed(speed_direction, 0)
            elif state == 'find_edge':
                delta = direction * get_delta(left) if use_left else -direction * get_delta(right)
                self.set_speed(speed_direction, pid.delta(delta * gradient))
            self.update()
        self.stop(stop)
