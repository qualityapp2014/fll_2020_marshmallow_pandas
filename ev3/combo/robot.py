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


def find_lane():
    return color_left.color() == Color.BLACK or color_right.color() == Color.BLACK


def get_color_delta(color):
    return sum(color.rgb()) / 150 - 1


GYRO_PID = [0.3, 0.2, 0.2, 0.3]
LINE_PID = [1, 2, 1, 0.3]


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
        #print("PID:", error, self.error_i, error_d, error * self.kp + self.error_i * self.ki + error_d * self.kd)
        return error * self.kp + self.error_i * self.ki + error_d * self.kd


class Robot:
    def __init__(self, accel=20):
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
            robot.stop()

    def reset(self):
        state = robot.state()
        self.speed = self.speed_last = state[1]
        self.turn_rate = state[3]
        robot.reset()

    def set_speed(self, speed, turn_rate):
        print("SPEED:", speed, turn_rate)
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
        print("Move:", distance, speed)
        self.reset()

        target_angle = gyro_angle or gyro.angle()

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        pid = PID(gyro_pid or GYRO_PID)
        while robot.distance() * direction < target:
            if terminate is not None and terminate():
                break
            delta = pid.delta(target_angle - gyro.angle())
            self.set_speed(speed_direction, delta)
            self.update()
        self.stop(stop)

        distance = robot.distance()
        print("Done:", distance, gyro.angle())
        return distance
        
    def turn(self, target_angle, speed, turn_rate, stop=False):
        current_angle = gyro.angle()
        print("Turn:", target_angle, speed, turn_rate, current_angle)

        direction = sign(target_angle - current_angle)
        self.set_speed(speed, turn_rate * direction)
        
        while (target_angle - gyro.angle()) * direction > 0:
            self.update()
        self.stop(stop)
        print("Done:", gyro.angle())

    def follow(self, distance, speed, use_left=True, line_delta=30, line_pid=None, stop=False):
        print("Follow:", distance, speed, line_pid)
        self.reset()

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        state = "find_lane_black"
        state_prev = None

        while robot.distance() * direction < target:
            if state != state_prev:
                print(state)
                state_prev = state

            left = color_left.color()
            right = color_right.color()
            if state == "find_lane_black":
                if left == Color.BLACK or right == Color.BLACK:
                    state = "find_lane_white"
                    adjust = -line_delta if left == Color.BLACK else line_delta
                    self.set_speed(speed_direction, adjust * direction)
            elif state == "find_lane_white":
                if left == Color.WHITE and right == Color.WHITE:
                    state = "find_edge"
                    pid = PID(line_pid or LINE_PID)
                    self.set_speed(speed_direction, 0)
            elif state == 'find_edge':
                if left == Color.BLACK or right == Color.BLACK:
                    state = "find_lane_white"
                    adjust = -line_delta if left == Color.BLACK else line_delta
                    self.set_speed(speed_direction, adjust * direction)
                else:
                    if use_left:
                        color = color_left
                        adjust = 1
                    else:
                        color = color_right
                        adjust = -1
                    self.set_speed(speed_direction, pid.delta(adjust * direction * get_color_delta(color))) 
            self.update()
        self.stop(stop)
