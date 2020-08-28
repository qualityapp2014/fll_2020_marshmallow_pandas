#!/usr/bin/env pybricks-micropython
import math

from config import *


def gyro_drift(iter, delay):
    speed_sum, speed_sum_sq, speed_max, speed_min = 0, 0, 0, 0

    for i in range(iter):
        s = gyro.speed()
        print(s)
        speed_max = max(s, speed_max)
        speed_min = min(s, speed_min)
        speed_sum += s
        speed_sum_sq += s ** 2
        wait(delay)

    speed_mean = speed_sum / iter
    speed_var = speed_sum_sq / iter - speed_mean ** 2
    return speed_mean, math.sqrt(speed_var), speed_max, speed_min


def drive(speed=200, iter=100, delay=10):
    ev3.speaker.say('start')
    gyro.reset_angle(0)
    robot.drive(speed, 0)
    print(gyro_drift(iter, delay))
    robot.stop()
    ev3.speaker.say('end')


def straight(distance=1000):
    ev3.speaker.say('forward')
    robot.straight(distance)
    ev3.speaker.say('backward')
    robot.straight(-distance)
    ev3.speaker.say('done')