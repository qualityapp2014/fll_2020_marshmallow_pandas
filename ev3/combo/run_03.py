#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move to the center lane
    r.move(200, 200)
    r.follow(260, 100, find_lane=True)
    r.turn(-51, 100, 50)
    r.follow(260, 100)

    # Measure distance and turn
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(45 + 660 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    # Flip the blue block
    motor_med_right.run_angle(1000, -2600)
    motor_med_right.run_angle(1000, -1500, wait=False)
    
    # Drop the basketball
    r.turn(-118, 70, 50)
    r.move(60, 50)
    # Reduce speed and overrun a bit to ensure good contact
    r.move(10, 20)
    
    # Move back to fit fork lift
    r.move(-30, 50)
    r.turn(-115, 40, 50, stop=True)
    
    # Lift crate
    motor_med_left.run_angle(1000, -1140)
    motor_med_left.run_angle(1000, 1140, wait=False)
    wait(300)

    # Back off and set arm for health unit
    r.move(-100, 100)
    motor_med_right.run_angle(1000, 3800, wait=False)
    r.move(-100, 100)

    # Pick up health unit
    r.turn(-136, 0, 50)
    r.follow(200, 50, use_left=False)

    # Return to the base
    motor_med_right.run_angle(1000, -3800, wait=False)
    r.turn(-35, -100, 30)
    r.move(-500, 400, stop=True)
    motor_med_right.run_angle(1000, 4100, wait=False)


if __name__ == "__main__":
    run()