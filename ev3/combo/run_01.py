#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot(10)
    gyro.reset_angle(0)

    r.move(100, 100)
    r.turn(-28, 0, 50)

    r.move(100, 100)
    r.turn(10, 0, 30)
    r.move(160, 100)

    r.move(-50, 100)
    r.turn(190, 0, 50)

    
    r.move(100, 100)
    r.turn(210, 0, 50)
    r.move(-150, 100)
    r.turn(197, 0, 20)

    r.move(-160, 100)
    r.move(270, 150)

    r.stop()

run()