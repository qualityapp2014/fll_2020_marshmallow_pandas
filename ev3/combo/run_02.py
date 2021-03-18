#!/usr/bin/env pybricks-micropython
from robot import *


def is_right_white():
    return is_white(color_right.reflection())


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move to the center lane
    r.move(200, 200)
    r.follow(260, 100, find_lane=True)
    r.turn(-51, 100, 50)
    motor_med_right.run_angle(1000, -1800, wait=False)
    r.follow(260, 100)

    # Measure distance and turn
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(45 + 660 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    # Flip the blue block
    motor_med_right.run_angle(1000, -2300, wait=False)
    wait(1000)

    # Drop the basketball
    r.turn(-110, 20, 20)
    # Reduce speed and overrun a bit to ensure good contact
    r.move(70, 50)
    r.move(25, 30)
    
    # Move back to fit fork lift
    r.move(-50, 50)
    r.turn(-108, 0, 20)
    r.move(40, 30, stop=True)
    
    # Lift crate
    motor_med_left.run_angle(1000, -1170)
    motor_med_left.run_angle(1000, 1170, wait=False)
    wait(300)

    # Back off and set arm for health unit
    r.move(-120, 100)
    motor_med_right.run_angle(1000, 3700, wait=False)

    # Find lane by checking on white color
    r.turn(-120, -100, 50)
    r.turn(-150, 0, 20, terminate=is_right_white)

    # Follow the line to pick up the health unit
    r.follow(280, 50, use_left=False)

    # Return to the base
    motor_med_right.run_angle(1000, -3700, wait=False)
    r.move(-50, 200)
    r.turn(-40, -100, 60)
    r.move(-560, 400, stop=True)
    motor_med_right.run_angle(1000, 4100, wait=False)


if __name__ == "__main__":
    run()
