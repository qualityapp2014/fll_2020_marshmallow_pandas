#!/usr/bin/env pybricks-micropython
from core import *


# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.set_speech_options('en', 'm1', 160, None)


# Configure the robot and sensors
left_motor = Motor(Port.B)
right_motor = Motor(Port.A)
robot = DriveBase(left_motor, right_motor, 80, 98)
robot.settings(400, 100, 90, 45)
gyro = GyroSensor(Port.S1, Direction.COUNTERCLOCKWISE)
color_top = ColorSensor(Port.S2)
color_left = ColorSensor(Port.S3)
color_right = ColorSensor(Port.S4)