#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    r.move(350, 100)
    r.move(100, 850)
    robot.drive(0, 0)
    wait(500)
    robot.stop()
    r.move(-200, 90)
    r.move(-300, 700)
    r.stop()

if __name__ == "__main__":
    run()