#!/usr/bin/env pybricks-micropython
from robot import *


def bench(reset=False):
    print("Mission - Bench")
    if reset:
        gyro.reset_angle(0)

    # Go straight to do bench and drop the cubes
    r.move(-350, 150, gyro_angle=0, stop=True)


def basketball(reset=False):
    print("Mission - Basketball")
    if reset:
        gyro.reset_angle(0)

    # Back off and turn to lane
    r.move(40, 200, gyro_angle=0)
    r.turn(-127, 100, 60)
    r.move(235, 150, gyro_angle=-130)
    r.turn(-171, 150, 50)

    # Follow line to control position
    r.follow(100, 100)

    # Measure distance to flip the cube
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(50 + 740 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    r.move(-50, 100)
    r.turn(-220, 30, 50)
    r.move(70, 120, gyro_angle=-222)
    r.move(30, 50, gyro_angle=-222, stop=True)

    # Lift crate
    motor_med_left.run_angle(1000, -1150, wait=False)
    wait(2500)
    motor_med_left.run_angle(1000, 350, wait=False)
    wait(500)

    if reset:
        wait(1000)
        motor_med_left.run_angle(1000, 800, wait=False)


def boccia(reset=False):
    print("Mission - Boccia")
    if reset:
        gyro.reset_angle(-224)

    # Turn to Boccia
    r.move(-50, 100, gyro_angle=-224)
    r.turn(-170, -100, 60)
    r.turn(-95, 150, 60)
    
    # Align by following the line
    r.follow(180, 150, use_left=False)
    
    # Turn and drop the cubes
    r.turn(-162, 40, 80)
    r.move(50, 150, gyro_angle=-165, stop=True)
    motor_med_right.run_angle(1000, 1300)
    motor_med_right.run_angle(1000, -500, wait=False)

    # Back off and turn to flip the boccia
    r.move(-60, 100, gyro_angle=-165)
    r.turn(-135, -20, 60)
    r.move(120, 100, gyro_angle=-133)
    
    r.move(-40, 100, gyro_angle=-133, stop=True)
    motor_med_right.run_angle(1000, -1700)
    motor_med_right.run_angle(1000, 900, wait=False)


def health_unit(reset=False):
    print("Mission - Health Unit")
    if reset:
        gyro.reset_angle(-135)

    # Turn back to push health unit back
    r.turn(-180, -100, 70)
    r.turn(-261, 150, 75)
    r.move(150, 200, gyro_angle=-263)
    r.move(50, 100, gyro_angle=-265)
    r.follow(50, 100)
    r.follow(140, 150)

    r.turn(-240, 200, 40)
    r.move(100, 200, gyro_angle=-243)
    r.turn(-260, 200, 30)
    r.move(130, 300, stop=True)

    motor_med_left.run_angle(1000, 800)
    if reset:
        motor_med_left.run_angle(1000, -800)


def run():
    gyro.reset_angle(0)

    bench()
    basketball()
    boccia()
    health_unit()

    # Turn and move to the bench
    motor_med_left.brake()
    motor_med_right.brake()


if __name__ == "__main__":
    run()
