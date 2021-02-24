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


GYRO_PID = [0.3, 0.2, 0.2, 0.3]
LINE_PID = [20, 5, 5, 0.5]


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
    def __init__(self, accel):
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

    def reset(self):
        state = robot.state()
        self.speed = self.speed_last = state[1]
        self.turn_rate = state[3]
        robot.reset()

    def set_speed(self, speed, turn_rate):
        self.speed = speed
        self.turn_rate = turn_rate

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
        
    def move(self, distance, speed, turn_rate=0, gyro_pid=None, gyro_angle=None, stop=False):
        print("Move: ", distance, speed, turn_rate)
        self.reset()

        if gyro_angle is None:
            gyro_angle = 0
            gyro.reset_angle(0)

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        pid = PID(gyro_pid or GYRO_PID)
        while robot.distance() * direction < target:
            delta = pid.delta(gyro_angle - gyro.angle())
            self.set_speed(speed_direction, turn_rate + delta)
            self.update()
        self.stop(stop)
        print("Done: ", robot.distance(), gyro.angle())
        
    def turn(self, angle, speed, turn_rate, stop=False):
        print("Turn", angle, speed, turn_rate)
        direction = sign(angle)
        target = angle * direction
        self.set_speed(speed, turn_rate * direction)
        gyro.reset_angle(0)

        while gyro.angle() * direction < target:
            self.update()
        self.stop(stop)
        print("Done: ", gyro.angle())

    def follow(self, distance, speed, line_pid=None, stop=False):
        print("Follow: ", distance, speed, line_pid)
        self.reset()

        direction = sign(distance)
        target = direction * distance
        speed_direction = speed * direction
        self.set_speed(speed_direction, 0)

        pid = PID(line_pid or LINE_PID)
        adjust = 0

        while robot.distance() * direction < target:
            left_color = color_left.color()
            right_color = color_right.color()

            if adjust == 0:
                if left_color == Color.BLACK:
                    adjust = -1
                elif right_color == Color.BLACK:
                    adjust = 1
            elif left_color == Color.WHITE and right_color == Color.WHITE:
                adjust = 0

            self.set_speed(speed_direction, pid.delta(adjust) * direction)
            self.update()
        self.stop(stop)
