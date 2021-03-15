#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    r.move(100, 100)
    r.follow(290, 100, use_left=False)
    robot.drive(800, 40)
    wait(75)
    robot.drive(0, 0)
    wait(1000)
    robot.stop()
    r.move(-300, 50)
    r.turn(20, -400, 10)
    r.stop()

if __name__ == "__main__":
    run()