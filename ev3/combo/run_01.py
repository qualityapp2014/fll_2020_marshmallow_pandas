#!/usr/bin/env pybricks-micropython
from robot import *

def run():
    r = Robot()
    gyro.reset_angle(0)

    # Turn and move to the bench
    # Attachment will trigger and pick up
    r.turn(-20, 100, 20)
    r.turn(5, 100, 20)
    r.move(70, 100)
    r.move(25, 30, stop=True)

    # Move back and turn 180 to drop the cubes
    r.move(-120, 100)
    r.turn(176, 15, 60)
    r.move(-210,100)
    r.move(-30, 20)

    # Move back to the base
    r.move(200, 200)
    r.turn(180, 200, 30)
    r.move(60, 50)
    r.stop()

if __name__ == "__main__":
    run()