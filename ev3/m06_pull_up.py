#!/usr/bin/env pybricks-micropython

#Import from config
from config import *


UP_SPEED = -800
DOWN_SPEED = 800
ANGLE = 360


def lift(speed, angle):
    motor_med_right.run_angle(speed, angle, wait=False)
    motor_med_left.run_angle(speed, angle, wait=True)


def lift_up(turns):
    lift(UP_SPEED, ANGLE * turns)


def lift_down(turns):
    lift(DOWN_SPEED, ANGLE * turns)

