#!/usr/bin/env pybricks-micropython
from robot import *

def run():
    r = Robot()
    gyro.reset_angle(0)

    # Turn and move to the bench
    # Attachment will trigger and pick up
    r.turn(-20, 100, 20)
    r.turn(10, 100, 20)
<<<<<<< HEAD
    r.move(70, 100, gyro_angle=13)
    r.move(35, 50, gyro_angle=13, stop=True)
=======
    r.move(70, 100)
    r.move(30, 50, stop=True)
>>>>>>> master

    # Move back and turn 180 to drop the cubes
    r.move(-80, 100)
    r.turn(186, 15, 40)
<<<<<<< HEAD
    r.move(-170, 100, gyro_angle=191)
    r.move(-20, 50, gyro_angle=191)

    # Move back to the base
    r.move(200, 300)
    r.turn(185, 240, 30)
=======
    r.move(-170, 100)
    r.move(-20, 50)

    # Move back to the base
    r.move(200, 200)
    r.turn(180, 160, 30)
>>>>>>> master
    r.move(30, 50)
    r.stop()

    motor_med_left.brake()
    motor_med_right.brake()


if __name__ == "__main__":
    run()
