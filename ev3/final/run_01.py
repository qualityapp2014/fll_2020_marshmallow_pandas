#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    gyro.reset_angle(0)

    bench()
    basketball()
    boccia()
    health_unit()

    # Turn and move to the bench
    motor_med_left.brake()
    motor_med_right.brake()
    motor_med_left.run_angle(1000, 800)


def bench(debug=False):
    print("Mission - Bench")
    if debug:
        gyro.reset_angle(0)

    # Go straight to do bench and drop the cubes
    r.move(-350, 150, gyro_angle=0, stop=True)


def basketball(debug=False):
    print("Mission - Basketball")
    if debug:
        gyro.reset_angle(0)

    # Back off and turn to lane
    r.move(100, 100, gyro_angle=0)
    r.turn(-127, 100, 50)
    r.move(240, 150, gyro_angle=-130)
    r.turn(-172, 100, 50)

    # Follow line to control position
    r.follow(150, 100)

    # Measure distance to flip the cube
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(45 + 750 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    r.move(-60, 100)
    r.turn(-220, 30, 50)
    r.move(80, 100, gyro_angle=-223)
    r.move(45, 50, gyro_angle=-223, stop=True)

    # Lift crate
    motor_med_left.run_angle(1000, -1180, wait=False)
    wait(2500)
    motor_med_left.run_angle(1000, 380, wait=False)
    wait(700)

    if debug:
        motor_med_left.run_angle(1000, 800, wait=False)


def boccia(debug=False):
    print("Mission - Boccia")
    if debug:
        gyro.reset_angle(-225)

    # Turn to Boccia
    r.move(-100, 100, gyro_angle=-225)
    r.turn(-170, -100, 50)
    r.turn(-95, 100, 50)
    
    # Align by following the line
    r.follow(180, 100, use_left=False)
    
    # Turn and drop the cubes
    r.turn(-162, 40, 80)
    r.move(60, 100, gyro_angle=-165, stop=True)
    motor_med_right.run_angle(1000, 1300)
    motor_med_right.run_angle(1000, -500, wait=False)

    # Back off and turn to flip the boccia
    r.move(-70, 50)
    r.turn(-130, -20, 50)
    r.move(160, 100, gyro_angle=-132)
    
    r.move(-60, 100, gyro_angle=-132, stop=True)
    motor_med_right.run_angle(1000, -1700)
    motor_med_right.run_angle(1000, 900, wait=False)


def health_unit(debug=False):
    print("Mission - Health Unit")
    if debug:
        gyro.reset_angle(-130)

    # Turn back to push health unit back
    r.turn(-180, -80, 50)
    r.turn(-258, 100, 50)
    r.move(180, 200, gyro_angle=-260)
    r.follow(220, 100)

    r.turn(-240, 200, 20)
    r.move(100, 200, gyro_angle=-243)
    r.turn(-270, 200, 20)
    r.move(40, 200, stop=True)


if __name__ == "__main__":
    run()
