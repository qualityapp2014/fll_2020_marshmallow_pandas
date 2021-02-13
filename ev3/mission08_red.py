#!/usr/bin/env pybricks-micropython

#___Importing configurations___#

from config import *
from control import *


move2(507)
turn(-90)
move2(580)
motor_med_left.run_angle(1000, -700)
move2(-50)
robot.turn(45)
move2(-775)


motor_med_left.run_angle(1000, 700)