#!/usr/bin/env pybricks-micropython
from core import *
from config import *
from control import *

#move forward
move_pid_gyro(226)

#back turn 90 degree then back straight to the treadmill
move_pid_gyro(-1865,-90, 300, 30, 60)

#stop both motors
robot.stop()

#reset left motor angle to 0
motor_left.reset_angle(0)

#turn left motor for needed rounds
motor_left.run_target(100,-930)

#stop left motor
motor_left.stop()

#move back to the base
move_pid_gyro(1800)