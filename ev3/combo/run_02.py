#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

    # Move forward and follow the line
    r.move(100, 100)
    r.follow(240, 150, use_left=False)

    # Accelerate and brake suddenly to throw the bar
    robot.drive(800, 20)
    wait(100)
    robot.drive(0, 0)
    wait(1000)
    robot.stop()

    # Move back
    r.move(-80, 100)
    r.move(-270, 200)
    r.turn(20, -500, 30)
    r.stop()
    
    motor_med_left.brake()
    motor_med_right.brake()


if __name__ == "__main__":
    run()