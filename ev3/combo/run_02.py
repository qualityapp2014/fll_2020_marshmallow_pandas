#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move to the center lane
    r.move(200, 200)
    r.follow(260, 100, find_lane=True)
    r.turn(-51, 100, 50)
    motor_med_right.run_angle(1000, -2000, wait=False)
    r.follow(260, 100)

    # Measure distance and turn
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(45 + 660 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    # Flip the blue block
    motor_med_right.run_angle(1000, -2100, wait=False)
    wait(700)

    # Drop the basketball
    r.turn(-118, 40, 20)
    # Reduce speed and overrun a bit to ensure good contact
    r.move(70, 30)
    
    # Move back to fit fork lift
    r.move(-50, 50)
    r.turn(-116, 0, 30)
    r.move(40, 30, stop=True)
    
    # Lift crate
    motor_med_left.run_angle(1000, -1140)
    motor_med_left.run_angle(1000, 1140, wait=False)
    wait(300)

    # Back off and set arm for health unit
    r.move(-100, 100)
    motor_med_right.run_angle(1000, 3700, wait=False)

    # Pick up health unit
    r.turn(-136, -135, 50)
    r.follow(280, 50, use_left=False)

    # Return to the base
    motor_med_right.run_angle(1000, -3700, wait=False)
    r.move(-70, 200)
    r.turn(-25, -100, 50)
    r.move(-560, 400, stop=True)
    motor_med_right.run_angle(1000, 4100, wait=False)


if __name__ == "__main__":
    run()
