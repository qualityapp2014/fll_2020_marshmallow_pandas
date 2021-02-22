#!/usr/bin/env pybricks-micropython
import math

from config import *


def get_direction(target):
    if target > 0:
        return 1
    return -1


def stop_motors():
    motor_left.reset_angle(0)
    motor_right.reset_angle(0)


def move(speed, delta=0):
    motor_left.run(speed + delta)
    motor_right.run(speed - delta)


class MotorAngles:
    def __init__(self):
        self.angles = motor_left.angle() + motor_right.angle()
    
    def get_distance(self):
        angles = (motor_left.angle() + motor_right.angle() - self.angles) / 2
        return angles / 360 * WHEEL_DIAMETER * math.pi


def move_distance(target, speed, delta=0, line_delta=0, stop=False):
    print("Starting to move.")
    direction = get_direction(target)

    # Set motor speed
    motor_speed = speed * direction    
    move(speed, delta)
    motor_angles = MotorAngles()
    
    adjust_delta = 0

    while True:
        if line_delta > 0:
            if adjust_delta == 0:
                if color_left.color() == Color.BLACK:
                    adjust_delta = -line_delta
                elif color_right.color() == Color.BLACK:
                    adjust_delta = line_delta
                if adjust_delta != 0:
                    print("Adjusting: {}.".format(adjust_delta))
                    move(motor_speed, delta + adjust_delta)
            else:
                if color_left.color() == Color.WHITE and color_right.color() == Color.WHITE:
                    print("Line returned.")
                    adjust_delta = 0
                    move(motor_speed, delta)

        distance = motor_angles.get_distance()
        if (distance - target) * direction >= 0:
            print("Target reached: {}.".format(distance))
            break    
    
    if stop:
        stop_motors()


def move_gyro(target, speed, gyro_delta=10, gyro_min=0.01, stop=False):
    print("Starting to move.")
    direction = get_direction(target)

    # Set motor speed
    motor_speed = speed * direction
    motor_angles = MotorAngles()
    move(motor_speed)
    gyro.reset_angle(0)
    
    while True:
        angle = gyro.angle()
        if abs(angle) > gyro_min:
            move(motor_speed, -gyro.angle() * gyro_delta)

        distance = motor_angles.get_distance()
        if (distance - target) * direction >= 0:
            print("Target reached: {}.".format(distance))
            break

def turn_gyro(target, speed):
    print("Starting to turn using Gyro. target: {}, speed: {}".format(target, speed))
    direction = get_direction(target)
    move(0, speed * direction)
    gyro.reset_angle(0)
    while True:
        delta = (gyro.angle() - target) * direction
        if delta >= 0:
            print("Target reached: {}".format(delta))
            break
    stop_motors()
    