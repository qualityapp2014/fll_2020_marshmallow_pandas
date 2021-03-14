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
    r.turn(-80, -20, 50, stop = True)
    motor_med_right.run_angle(100, 850)
    r.move(50,20,stop=True)
    motor_med_right.run_angle(100,600)
    r.move(-100,20,stop=True)
    
    #r.follow(150, 100, use_left = True, stop = True)
    #r.move(195,20)
    #r.stop()
    #r.move(-150,100)
    #r.stop()
    #r.turn(-70,30,50)
    #r.stop()
    #motor_med_right.run(10, 20)
    
if __name__ == "__main__":
    run()