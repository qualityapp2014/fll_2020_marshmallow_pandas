#!/usr/bin/env pybricks-micropython
from core import *


# Create your objects here. 
ev3 = EV3Brick() 
ev3.speaker.set_speech_options('en', 'f1', 160, None) 

# Configure drive motors
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D, Direction.COUNTERCLOCKWISE)

robot = DriveBase(motor_left, motor_right, 55, 120)
robot.settings(400, 200, 180, 180)

# Configure medium motors
motor_med_left = Motor(Port.B)
motor_med_right = Motor(Port.C)

#Configure the sensors
color_left_rear = ColorSensor(Port.S1)
color_left_front = ColorSensor(Port.S2)
color_right_front = ColorSensor(Port.S3)
color_right_rear = ColorSensor(Port.S4)