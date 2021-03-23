#!/usr/bin/env pybricks-micropython
from robot import *

def run():
    r = Robot()
    gyro.reset_angle(0)

    # Turn and move to the bench
    # Attachment will trigger and pick up
    r.turn(-20, 100, 20)
    r.turn(10, 100, 20)
    r.move(60, 100, gyro_angle=13)
    r.move(50, 50, gyro_angle=13, stop=True)

    # Move back and turn 180 to drop the cubes
    r.move(-80, 100)
    r.turn(186, 15, 40)
    r.move(-170, 100, gyro_angle=191)
    r.move(-20, 50, gyro_angle=191)

    # Move back to the base
    r.move(200, 300)
    r.turn(188, 100, 50)
    r.stop()

    motor_med_left.brake()
    motor_med_right.brake()


if __name__ == "__main__":
    run()
