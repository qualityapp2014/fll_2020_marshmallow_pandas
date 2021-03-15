#!/usr/bin/env pybricks-micropython
from robot import *


def run():
   
    #r.move(640,100)
    #r.stop()
    r = Robot(10)
    gyro.reset_angle(0)

    debugmode=False

    r.move(200, 150, stop = debugmode)
    r.follow(400, 100, stop = debugmode)
    r.turn(30,10,50, stop = debugmode)
    r.move(105,50, stop = debugmode)
    r.turn(0,10,20, stop = debugmode)
    r.move(205,20, stop = debugmode)
    r.move(-50,100, stop = debugmode)    
            
    #following code intends to hang the objects in place
    r.turn(-75, 30, 50, stop = True)
    motor_med_right.run_angle(500, 850)
    #r.move(20,20,stop=True)
    #motor_med_right.run_angle(100,100)
    r.move(-100, 30, stop=True)
    motor_med_right.run_angle(500, 1800)
    
    #follow the line to the next task
    r.turn(-85, 300, 50, stop=debugmode)
    r.move(600, 200, stop = True)
    #r.turn(-70, 20, 50, stop = True)
    r.turn(-90, -20, 50, stop=True)
    #motor_med_right.run_angle(800, -800)
    motor_med_right.run_angle(500, -1800)
    motor_med_left.run_angle(800, 600)
    #r.move(80, 100, stop=True)
    #r.move(400, 200, stop=True)
    #r.follow(200, 100, find_lane=True, stop=True)
    #r.follow(200, 100, stop = True)   
       
run()
