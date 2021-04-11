#!/usr/bin/env pybricks-micropython
from robot import *


def move_to_lane(r):
    # Move to lane
    motor_med_right.run_angle(1000, 700, wait=False)
    r.move(150, 200)
    r.turn(-10, 100, 30)
    r.follow(340, 100)


def hang_health_unit(r):
    # Hang health units
    r.turn(-51, 10, 50)
    r.move(50, 50, stop=True, gyro_angle=-53)
    motor_med_right.run_angle(500, 800)
    r.move(-60, 80)


def push_step_counter(r):
    # Move to the step counter
    r.turn(30, 10, 50)
    r.move(110, 100)
    r.turn(2, 10, 30)

    # Push the step counter slowly
    r.move(160, 20, gyro_angle=0)
    # Lower the arm at the end to prepare passing the bridge
    # and avoid health unit stuck on step counter
    motor_med_right.run_angle(1000, 1100, wait=False)
    r.move(60, 20, gyro_angle=0)


def pass_bridge(r):
    # Turn to pass bridge
    r.stop()
    r.turn(-10, -40, 20)
    motor_med_right.run_angle(1000, 1600, wait=False)
    r.turn(-70, 20, 40)
    r.turn(-91, -30, 40)

    # Follow the lane to pass the bridge
    r.follow(360, 75, use_left=False, gradient=-1)
    motor_med_right.run_angle(1000, -500, wait=False)

    # Measure distance to locate in lane
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(70 + 470 - distance, 0, 200)
    r.move(distance_next, 50)
    print("Distance", ultrasonic.distance())


def drop_cubes(r):
    # Turn the Boccia and flip the cube 
    r.turn(-71, 30, 20)
    r.turn(-74, -40, 30, stop=True)
    motor_med_right.run_angle(1000, -1400)

    # Drop the cubes
    motor_med_right.run_angle(1000, 1400, wait=False)
    wait(500)
    r.move(-40, 50)
    r.turn(-88, 50, 30)
    motor_med_right.run_angle(1000, -3700, wait=False)
    r.move(180, 100, stop=True, gyro_angle=-90)
    motor_med_left.run_angle(1000, 1800)
    wait(700)
    motor_med_left.run_angle(1000, -1800, wait=False)


def dance(r):
    # Dance floor
    r.turn(-150, -30, 60)
    r.move(180, 200, stop=True)
    while True:
        r.turn(-145, 0, 30)
        r.turn(-135, 0, 30)
        r.move(-5, 20)


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