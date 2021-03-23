#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move to the center lane
    r.move(150, 200)
    r.turn(-21, 100, 50)

    r.follow(230, 100)
    r.turn(-72, 100, 50)
    motor_med_right.run_angle(1000, 2300, wait=False)
    r.follow(260, 120)

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
    r.turn(-135, 10, 50)
    r.turn(-142, 0, 20)
    # Reduce speed and overrun a bit to ensure good contact
    r.move(100, 50, gyro_angle=-145)
    r.move(20, 20, gyro_angle=-145)
    
    # Move back to fit fork lift
    r.move(-50, 50)
    r.turn(-142, 0, 20)
    r.move(40, 50, gyro_angle=-142, stop=True)
    
    # Lift crate
    motor_med_left.run_angle(1000, -1160, wait=False)
    wait(2500)
    motor_med_left.run_angle(1000, 1160, wait=False)
    wait(500)

    # Back off and set arm for health unit
    r.move(-130, 100)
    motor_med_right.run_angle(1000, 3900, wait=False)

    # Find lane by checking on white color
    r.turn(-165, -80, 50)
    r.turn(-180, 0, 20, terminate=is_right_white)

    # Follow the line to pick up the health unit
    r.follow(240, 75, use_left=False)

    # Return to the base
    motor_med_right.run_angle(1000, -3900, wait=False, then=Stop.BRAKE)
    r.move(350, 400, stop=True)

    motor_med_left.brake()


if __name__ == "__main__":
    run()
