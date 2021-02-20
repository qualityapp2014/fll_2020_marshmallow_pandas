#!/usr/bin/env pybricks-micropython
from core import *


# Create your objects here. 
ev3 = EV3Brick() 
ev3.speaker.set_speech_options('en', 'f1', 160, None) 


# Configure drive motors
motor_left = Motor(Port.A, Direction.COUNTERCLOCKWISE)
motor_right = Motor(Port.D, Direction.COUNTERCLOCKWISE)
left_motor = motor_left
right_motor = motor_right
robot = DriveBase(motor_left, motor_right, 87, 111)
robot.settings(400, 100, 90, 45)

# Configure medium motors
motor_med_left = Motor(Port.B)
motor_med_right = Motor(Port.C)

#Configure the sensors
color_left = ColorSensor(Port.S1)
color_right = ColorSensor(Port.S4)

ultrasonic = UltrasonicSensor(Port.S2)
gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)