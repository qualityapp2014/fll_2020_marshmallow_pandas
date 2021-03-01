#!/usr/bin/env pybricks-micropython
from robot_control import *

move_distance(410, 200, line_delta=10)
turn_gyro(-45, 100)
motor_med_right.run_angle(500, -800, wait=False)
move_distance(185, 100, line_delta=10)
turn_gyro(-62, 100)
move_distance(120, 100, line_delta=20)
motor_med_right.run_angle(500, -800)
move_distance(-300, 350)
turn_gyro(90, 100)
move_distance(-700, 400)
move(0)
motor_med_right.run_angle(500, 1600)