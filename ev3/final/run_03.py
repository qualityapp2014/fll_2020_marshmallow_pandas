#!/usr/bin/env pybricks-micropython
from robot import *

def step_counter(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Move straight to step counter
    r.move(800, 300, gyro_angle=0)
    # Slow down to push to the end
    r.move(240, 200, gyro_angle=0, stop=True)


def tire_flip_small(debug=False):
    if debug:
        gyro.reset_angle(0)

    # Back off from step counter and turn to lane
    r.move(-50, 100, gyro_angle=0)
    motor_med_right.run_angle(1000, 3800, wait=False)
    r.turn(-51, 70, 30)
    r.move(170, 100, gyro_angle=-53, stop=True)
    wait(500)

    # Flip the tire
    motor_med_right.run_angle(1000, 700, wait=False)
    wait(300)
    r.move(-80, 200, stop=True)

    # Push the tire in
    r.move(110, 100, stop=True)


def row_machine(debug=False):
    if debug:
        gyro.reset_angle(-53)

    # Move back to the lane
    r.move(-60, 100, gyro_angle=-53)
    motor_med_right.run_angle(1000, -2200, wait=False)
    r.turn(-12, 100, 50)

    # Follow the lane and turn to row machine
    r.follow(320, 100)
    r.turn(-88, 100, 50)
    r.move(210, 100, gyro_angle=-90)
    r.turn(2, 0, 50)

    # Move close and pull the tire out
    r.move(20, 30, gyro_angle=4, stop=True)
    motor_med_right.run_angle(1000, 2300)
    r.move(-130, 30, gyro_angle=4, stop=True)
    motor_med_right.run_angle(1000, -3200, wait=False)
    wait(500)


def weight_machine(debug=False):
    if debug:
        gyro.reset_angle(4)

    # Turn to weight machine
    r.turn(-85, 30, 50)
    r.move(160, 100, gyro_angle=-90)
    r.turn(-68, 20, 30, stop=True)

    # Press down weight machine
    motor_med_right.run_angle(1000, 1500)
    motor_med_right.run_angle(600, 1000, wait=False)
    r.move(50, 30, gyro_angle=-68, stop=True)
    motor_med_right.run_angle(1000, -1500)


def tire_flip_large(debug=False):
    if debug:
        gyro.reset_angle(-65)

    # Turn to weight machine
    motor_med_right.run_angle(1000, 1000, wait=False)
    r.turn(-227, 0, 50)
    r.move(15, 20, gyro_angle=-230, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 800, wait=False)
    wait(500)
    r.move(-80, 400, stop=True)

    # Push the tire in
    r.move(200, 100, gyro_angle=-225)
    r.move(100, 100, gyro_angle=-235, stop=True)
    motor_med_right.run_angle(1000, -2000, wait=False)


def treadmill(debug=False):
    if debug:
        gyro.reset_angle(-233)

    # Back off and turn back
    r.move(-40, 100, gyro_angle=-233)
    r.turn(-292, 100, 30)
    r.move(140, 100, gyro_angle=-295)

    r.turn(-273, 100, 30)
    r.move(180, 100, gyro_angle=-270)

    # Back off to treadmill
    r.turn(-180, 30, 50)
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(-280, 150, gyro_angle=-178, stop=True)

    # Spin the treadmill
    motor_left.run_time(-800, 2500)
    

def health_unit(debug=False):
    if debug:
        gyro.reset_angle(-180)

    # Move off treadmill
    r.move(100, 100, gyro_angle=-180)
    r.follow(420, 100)

    r.turn(-118, 0, 50)
    r.move(20, 20, gyro_angle=-115, stop=True)

    # Hang health unit
    motor_med_left.run_angle(1000, 1000)


def dance_floor(debug=False):
    if debug:
        gyro.reset_angle(-115)

    # Back off and turn to pass the bridge
    r.move(-70, 30, gyro_angle=-115)
    r.turn(-176, 0, 50)
    motor_med_left.run_angle(1000, 4000, wait=False)
    r.move(250, 100, gyro_angle=-180)
    r.turn(-95, 0, 50)
    r.move(400, 200, gyro_angle=-90)

    # Turn to dance floor
    r.turn(-135, 200, 50)
    r.move(200, 200, gyro_angle=-140, stop=True)

    while True:
        r.turn(-145, 0, 30)
        r.turn(-135, 0, 30)


def run():
    gyro.reset_angle(0)

    step_counter()
    tire_flip_small()
    row_machine()
    weight_machine()
    tire_flip_large()
    treadmill()
    health_unit()
    dance_floor()


if __name__ == "__main__":
    run()