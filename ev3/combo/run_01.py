#!/usr/bin/env pybricks-micropython
from robot import *

def run():
    r = Robot()
    gyro.reset_angle(0)

    # Turn and move to the bench
    # Attachment will trigger and pick up
    r.turn(-20, 100, 20)
    r.turn(9, 100, 20)
    r.move(100, 100)
    r.move(20, 50, stop=True)

    # Move back and turn 180 to drop the cubes
    r.move(-60, 100)
    r.turn(189, 12, 30)
    r.move(-160, 50)

    # Move back to the base
    r.move(100, 200)
    r.turn(180, 200, 15)
    r.move(50, 30)
    r.stop()

if __name__ == "__main__":
    run()