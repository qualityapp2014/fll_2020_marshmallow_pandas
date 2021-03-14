#!/usr/bin/env pybricks-micropython
from robot import *

def run():
    r = Robot(20)
    gyro.reset_angle(0)

    # Turn and move to the bench
    # Attachment will trigger and pick up
    r.turn(-20, 100, 20)
    r.turn(9, 100, 20)
    r.move(120, 100, stop=True)

    # Move back and turn 180 to drop the cubes
    r.move(-60, 100)
    r.turn(184, 10, 70)
    r.move(-120, 100)
    r.move(-30, 50)
    r.stop()

    # Move back to base
    r.move(50, 200)
    r.turn(180, 200, 10)
    r.stop()

run()