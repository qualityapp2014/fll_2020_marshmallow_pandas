#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot(10)
    gyro.reset_angle(0)

    r.move(200, 100)
    r.follow(230, 100)
    r.turn(-45, 100, 50)
    r.follow(200, 100)

    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(110 + 550 - distance, 50, 200)
    r.move(distance_next, 100)
    print("Distance", ultrasonic.distance())

    r.turn(-110, 0, 50)
    r.move(60, 50)
    r.stop()

    motor_med_right.run_angle(400, 2000)
    r.turn(-110, 0, 50)
    r.move(50, 50)
    r.stop()
    motor_med_left.run_angle(400, -1150)
    motor_med_left.run_angle(400, 1150, wait=False)
    r.stop()

    r.move(-100, 50)
    r.stop()
    motor_med_right.run_angle(400, -2000)

run()