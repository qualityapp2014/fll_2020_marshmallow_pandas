#!/usr/bin/env pybricks-micropython

from config import *

# robot.settings(straight_speed, straight_acceleration, turn_rate, turn_acceleration)
# robot.settings(400, 100, 2000, 50)

robot.settings(1700, 1700, 2000, 50)
robot.straight(490)
robot.stop()
robot.settings(300,300,1000,0)
robot.straight(-100)   
robot.stop()
robot.straight(-700) 