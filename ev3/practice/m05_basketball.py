#!/usr/bin/env pybricks-micropython

#Import from config
from config import*

#Moving to the mission
#robot.turn(45)
#robot.straight(785)
#robot.turn(-130)
#robot.straight(120)

#Lift up attachment to lift up the basketball hoop
motor_med_right.run_angle(600, 1000)
robot.straight(10)
robot.straight(-10)
robot.turn(-40)
robot.straight(60)
motor_med_left.run_angle(100,-1100)
motor_med_left.run_angle(100,500)

#Going back to launch area
#robot.straight(-125)
#robot.turn(-170)
#robot.straight(550) 