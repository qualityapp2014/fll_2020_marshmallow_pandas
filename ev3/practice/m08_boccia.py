#!/usr/bin/env pybricks-micropython

#Importing configurations
from config import*

#back of robot alin with the hang mission. The robot's right wheels at the close to inner left side of the back line. 
robot.straight(280)
#the cup with the blocks position. The rubber bands should be parallel to the floor. 
motor_med_left.run_angle(500, 1600)
robot.straight(-180)
robot.turn(60)
motor_med_right.run_angle(400, -800)
robot.straight(-100)