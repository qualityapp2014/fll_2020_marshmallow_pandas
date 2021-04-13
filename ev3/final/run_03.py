#!/usr/bin/env pybricks-micropython
from robot import *

def step_counter(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Move straight to step counter
    r.move(800, 300, gyro_angle=0)
    # Slow down to push to the end
    r.move(240, 200, gyro_angle=0, stop=True)


def row_machine(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Back off from step counter and turn to lane
    r.move(-50, 100, gyro_angle=0)
    r.turn(-40, 50, 20)
    r.move(110, 100, gyro_angle=-43)
    r.turn(-10, 100, 50)

    r.follow(240, 100)
    r.turn(-42, 100, 50)

    r.move(100, 100, gyro_angle=-45, stop=True)


def run():
    gyro.reset_angle(0)

    step_counter()


if __name__ == "__main__":
    row_machine(True)