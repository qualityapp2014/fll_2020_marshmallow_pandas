#!/usr/bin/env pybricks-micropython
from robot import *


def move_to_lane(r):
    # Move to lane
    motor_med_right.run_angle(1000, 800, wait=False)
    r.move(150, 200)
    r.turn(-10, 100, 30)
    r.follow(340, 100)


def hang_health_unit(r):
    # Hang health units
    r.turn(-51, 0, 50)
    r.move(50, 50, stop=True, gyro_angle=-53)
    motor_med_right.run_angle(500, 800)
    r.move(-60, 80)


def push_step_counter(r):
    # Push step counter
    r.turn(30, 10, 60)
    r.move(100, 100)
    r.turn(2, 30, 50)

    # Lower the arm at the end to avoid health unit stuck on step counter
    r.move(160, 25, gyro_angle=0)
    motor_med_right.run_angle(1000, 1000, wait=False)
    r.move(60, 25, gyro_angle=0)


def pass_bridge(r):
    # Turn to pass bridge
    r.stop()
    r.turn(-15, -50, 20)
    motor_med_right.run_angle(1000, 1600, wait=False)
    r.turn(-65, 40, 50)
    r.turn(-88, -30, 50)
    r.move(70, 100, gyro_angle=-90)

    # Follow the lane to pass the bridge
    r.follow(300, 100, use_left=False, gradient=-1)
    motor_med_right.run_angle(1000, -500, wait=False)

    # Measure distance to locate in lane
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(70 + 470 - distance, 0, 200)
    r.move(distance_next, 50)
    print("Distance", ultrasonic.distance())


def drop_cubes(r):
    # Turn the Boccia and flip the cube 
    r.turn(-72, 30, 20)
    r.turn(-74, -40, 30, stop=True)
    motor_med_right.run_angle(1000, -1400)

    # Drop the cubes
    motor_med_right.run_angle(1000, 1400, wait=False)
    wait(500)
    r.move(-40, 50)
    r.turn(-88, 50, 30)
    motor_med_right.run_angle(1000, -3700, wait=False)
    r.move(160, 100, stop=True, gyro_angle=-90)
    motor_med_left.run_angle(1000, 1800)
    wait(500)
    motor_med_left.run_angle(1000, -1800, wait=False)


def dance(r):
    # Dance floor
    r.turn(-150, -30, 100)
    r.move(170, 150, stop=True)
    while True:
        r.turn(-145, 0, 30)
        r.turn(-135, 0, 30)
        r.move(-10, 20)


def run():
    r = Robot()
    gyro.reset_angle(0)

    move_to_lane(r)

    hang_health_unit(r)

    push_step_counter(r)

    pass_bridge(r)

    drop_cubes(r)

    dance(r)

if __name__ == "__main__":
    run()