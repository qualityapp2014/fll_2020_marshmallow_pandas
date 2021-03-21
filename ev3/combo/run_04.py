#!/usr/bin/env pybricks-micropython
from robot import *


def move_to_lane(r):
    # Move to lane
    motor_med_right.run_angle(1000, 800, wait=False)
    r.move(150, 100)
    r.turn(-12, 100, 30)
    r.follow(350, 100)


def hang_health_unit(r):
    # Hang health units
    r.turn(-51, 0, 50)
    r.move(50, 30, stop=True, gyro_angle=-53)
    motor_med_right.run_angle(500, 600)
    r.move(-70, 50)

def push_step_counter(r):
    # Push step counter
    r.turn(30, 10, 60)
    r.move(90, 100)
    r.turn(2, 30, 50)

    # Lower the arm at the end to avoid health unit stuck on step counter
    r.move(160, 20, gyro_angle=0)
    motor_med_right.run_angle(1000, 1000, wait=False)
    r.move(70, 20, gyro_angle=0)


def pass_bridge(r):
    # Turn to pass bridge
    r.turn(-10, -50, 30)
    motor_med_right.run_angle(1000, 1800, wait=False)
    r.turn(-78, 0, 50)
    r.turn(-90, 0, 10, terminate=is_right_black)

    r.follow(320, 75, use_left=False)
    motor_med_right.run_angle(1000, -400, wait=False)

    # Measure distance to locate in lane
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(70 + 490 - distance, 0, 200)
    r.move(distance_next, 50)
    print("Distance", ultrasonic.distance())


def drop_cubes(r):
    # Turn the Boccia and flip the cube 
    r.turn(-72, 20, 20)
    r.turn(-75, -40, 20, stop=True)
    motor_med_right.run_angle(1000, -1400)

    # Drop the cubes
    motor_med_right.run_angle(1000, 1400, wait=False)
    wait(500)
    r.move(-40, 50)
    r.turn(-88, 50, 30)
    motor_med_right.run_angle(1000, -3800, wait=False)
    r.move(180, 100, stop=True, gyro_angle=-90)
    motor_med_left.run_angle(1000, 1500)
    motor_med_left.run_angle(1000, -1500, wait=False)


def dance(r):
    # Dance floor
    r.turn(-145, -30, 60)
    r.move(200, 100, stop=True)
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