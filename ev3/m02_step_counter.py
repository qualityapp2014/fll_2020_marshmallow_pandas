#!/usr/bin/env pybricks-micropython

#Importing configurations
from config import *

#Moving to the mission
robot.straight(-850)

robot.stop()
robot.settings(20, 10, 90, 45)

robot.straight(-190)

robot.stop()
robot.settings(400, 100, 90, 45)

#Going back from the mission
robot.straight(1000)



