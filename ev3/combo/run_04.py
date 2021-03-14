#!/usr/bin/env pybricks-micropython
from robot import *


def run():
   
    #r.move(640,100)
    #r.stop()
    r = Robot(20)
    gyro.reset_angle(0)

    debugmode=False

    r.move(200, 100, stop = debugmode)
    r.follow(400, 100, stop = debugmode)
    r.turn(30,10,50, stop = debugmode)
    r.move(105,50, stop = debugmode)
    r.turn(0,10,20, stop = debugmode)
    r.move(235,20, stop = debugmode)
    r.move(-50,100, stop = debugmode)    
            
    #following code intendes to hang the objects in place
    r.turn(-77, -10, 50, stop = True)
    motor_med_right.run_angle(100, 920)
    #r.move(20,20,stop=True)
    #motor_med_right.run_angle(100,100)
    r.move(-150,20,stop=True)
    motor_med_right.run_angle(200, 500)
    
    #follow the line to the next task
    r.turn(-90, 0, 50, stop=True)
    r.follow(200, 100, find_lane=True, stop=True)
    #r.follow(200, 100, stop = True)
    
       
run()