#!/usr/bin/env pybricks-micropython
from robot_control import *

turn_gyro(40, 75)
move_distance(400, 200)
turn_gyro(-32, 100)
move_distance(300, 100, line_delta=20)

stop_motors(0)
