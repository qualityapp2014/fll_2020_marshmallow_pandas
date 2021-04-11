#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    gyro.reset_angle(0)

    bench()
    basketball()
    boccia()
    health_unit()

    # Turn and move to the bench
    motor_med_left.run_angle(1000, 750, wait=False)
    motor_med_left.brake()
    motor_med_right.brake()


def bench(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Go straight to do bench and drop the cubes
    r.move(-320, 150, gyro_angle=0)
    r.move(-30, 50, gyro_angle=0, stop=True)
    

def basketball(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Back off and turn to lane
    r.move(100, 100, gyro_angle=0)
    r.turn(-124, 100, 50)
    r.move(240, 100, gyro_angle=-130)
    r.turn(-156, 100, 50)

    # Follow line to control position
    r.follow(200, 100)

    # Measure distance to flip the cube
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(60 + 750 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    r.move(-60, 100, gyro_angle=-180)
    r.turn(-216, 0, 50)
    r.move(100, 100, gyro_angle=-224)
    r.move(30, 50, gyro_angle=-224, stop=True)

    # Lift crate
    motor_med_left.run_angle(1000, -1150, wait=False)
    wait(2500)
    motor_med_left.run_angle(1000, 400)

    if debug:
        motor_med_left.run_angle(1000, 750, wait=False)


def boccia(debug=False):
    if debug:
        gyro.reset_angle(-225)

    # Turn to Boccia
    r.move(-100, 100, gyro_angle=-225)
    r.turn(-170, -100, 50)
    r.turn(-95, 100, 50)
    # Align by follow the line
    r.follow(180, 100, use_left=False)
    
    # Turn and drop the cubes
    r.turn(-160, 40, 80)
    r.move(60, 100, gyro_angle=-165, stop=True)
    motor_med_right.run_angle(1000, 1300)
    motor_med_right.run_angle(1000, -500, wait=False)

    # Back off and turn to flip the boccia
    r.move(-70, 50, gyro_angle=-165)
    r.turn(-135, -20, 50)
    r.move(130, 100, gyro_angle=-130)
    
    r.move(-60, 50, gyro_angle=-130, stop=True)
    motor_med_right.run_angle(1000, -1500)
    motor_med_right.run_angle(1000, 700, wait=False)


def health_unit(debug=False):
    if debug:
        gyro.reset_angle(-130)

    # Turn back to push health unit back
    r.turn(-180, -80, 50)
    r.turn(-260, 100, 50)
    r.move(180, 200, gyro_angle=-265)
    r.follow(220, 100)

    r.turn(-240, 100, 20)
    r.move(100, 100)
    r.turn(-270, 100, 10)
    r.move(100, 100, stop=True)


if __name__ == "__main__":
    run()
