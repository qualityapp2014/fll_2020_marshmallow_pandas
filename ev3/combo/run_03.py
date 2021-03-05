#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move to location
    r.move(200, 200)
    r.follow(260, 100, find_lane=True)
    r.turn(-51, 100, 50)
    r.follow(260, 100)

    # Measure distance and turn
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(50 + 660 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    # Flip the block
    motor_med_right.run_angle(1000, -2500)
    motor_med_right.run_angle(1000, -1500, wait=False)
    
    # Basketball
    r.turn(-118, 0, 50)
    r.move(80, 50)
    r.turn(-113, 0, 50)
    r.move(20, 50, stop=True)
    
    motor_med_left.run_angle(1000, -1180)
    motor_med_left.run_angle(1000, 300)
    motor_med_left.run_angle(1000, 880, wait=False)
    r.move(-100, 100)
    motor_med_right.run_angle(1000, 3700, wait=False)
    r.move(-80, 50)

    # Pick health unit
    r.turn(-138, 0, 50)
    r.follow(200, 50, use_left=False)

    motor_med_right.run_angle(1000, -3000, wait=False)
    r.turn(-35, -150, 45)
    r.move(-600, 400, stop=True)
    motor_med_right.run_angle(1000, 3300, wait=False)    
    return


run()