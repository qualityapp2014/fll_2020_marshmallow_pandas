#!/usr/bin/env pybricks-micropython
from core import *


# Create your objects here. 
ev3 = EV3Brick() 
ev3.speaker.set_speech_options('en', 'f1', 160, None) 

WHEEL_DIAMETER = 87

def config_motor(motor):
    motor.control.limits(800, 400, 100)
    motor.control.pid(200, 400, 5, 20, 5, 0)
    return motor


# Configure drive motors
motor_left = config_motor(Motor(Port.A, Direction.COUNTERCLOCKWISE))
motor_right = config_motor(Motor(Port.D, Direction.COUNTERCLOCKWISE))

robot = DriveBase(motor_left, motor_right, WHEEL_DIAMETER, 111)
robot.settings(400, 100, 90, 45)

# Configure medium motors
motor_med_left = Motor(Port.B)
motor_med_right = Motor(Port.C)

#Configure the sensors
color_left = ColorSensor(Port.S1)
color_right = ColorSensor(Port.S4)

ultrasonic = UltrasonicSensor(Port.S2)
gyro = GyroSensor(Port.S3, Direction.COUNTERCLOCKWISE)