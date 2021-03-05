#!/usr/bin/env pybricks-micropython
from robot import *


def run():
   
    r = Robot(20)
    gyro.reset_angle(0)

    r.move(640, 100, stop=True)
    r.move(195, 20, stop=True)
    r.move(-150, 100, stop=True)
    r.turn(-70, 30, 50, stop=True)
    motor_med_right.run_angle(100, 500)
    
run()