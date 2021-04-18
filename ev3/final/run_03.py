#!/usr/bin/env pybricks-micropython
from robot import *


def fast_stop():
    robot.drive(0, 0)
    wait(200)
    robot.stop()


def step_counter(reset=False):
    print('step_counter')
    if reset:
        gyro.reset_angle(0)

    # Move straight to step counter
    motor_med_right.run_angle(1000, 2400, wait=False)
    r.move(810, 300, gyro_angle=1)
    # Slow down to push to the end
    r.move(270, 120, gyro_angle=1)
    robot.drive(60, 0)
    wait(500)
    fast_stop()

    if reset:
        # Total = 2400
        motor_med_right.run_angle(1000, -2400, wait=False)


def tire_flip_small(reset=False):
    print('tire_flip_small')
    if reset:
        gyro.reset_angle(0)

    # Back off from step counter and turn to lane
    r.move(-60, 120, gyro_angle=0)
    r.turn(-10, 70, 30)
    motor_med_right.run_angle(1000, 1300, wait=False)
    r.turn(-52, 70, 30)
    r.move(140, 120, gyro_angle=-54)
    r.move(35, 30, gyro_angle=-54, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 1300, wait=False)
    wait(600)
    robot.drive(-20, 0)
    wait(200)
    robot.drive(-300, 0)
    wait(400)
    fast_stop()

    # Push the tire in
    r.move(110, 150, gyro_angle=-45, stop=True)
    if reset:
        # Total = 5000
        motor_med_right.run_angle(1000, -2600, wait=False)


def row_machine(reset=False):
    print('row_machine')
    if reset:
        gyro.reset_angle(-45)

    # Move back to the lane
    r.move(-60, 100, gyro_angle=-45)
    motor_med_right.run_angle(1000, -2900, wait=False)
    r.turn(-12, 100, 50)

    # Follow the lane and turn to row machine
    r.follow(320, 130)
    r.turn(-88, 100, 50)
    r.move(180, 120, gyro_angle=-90)
    r.turn(2, 0, 50, stop=True)

    # Move close and pull the tire out
    motor_med_right.run_angle(1000, 2000)
    r.turn(2, -10, 20, stop=True)
    motor_med_right.run_angle(1000, 500, wait=False)
    wait(400)
    r.move(-120, 30, gyro_angle=-3, stop=True)

    if reset:
        # Total = 4600
        motor_med_right.run_angle(1000, 400, wait=False)


def weight_machine(reset=False):
    print('weight_machine')
    if reset:
        gyro.reset_angle(0)

    # Turn to weight machine
    motor_med_right.run_angle(1000, -3300, wait=False)
    wait(600)

    r.turn(-87, 30, 50)
    r.move(170, 120, gyro_angle=-90)
    r.turn(-72, 20, 30, stop=True)

    # Press down weight machine
    motor_med_right.run_angle(1000, 1400)
    motor_med_right.run_angle(1000, 600, wait=False)
    r.move(50, 50, gyro_angle=-70, stop=True)
    wait(300)
    
    if reset:
        # Total = 3300
        motor_med_right.run_angle(1000, 1300, wait=False)


def tire_flip_large(reset=False):
    print('tire_flip_large')
    if reset:
        gyro.reset_angle(-70)

    # Turn to weight machine
    motor_med_right.run_angle(1000, -1200, wait=False)
    r.move(-40, 80, gyro_angle=-70)
    
    r.turn(-120, -30, 50)
    motor_med_right.run_angle(1000, 1200, wait=False)
    r.turn(-219, -20, 50)
    r.move(-35, 30, gyro_angle=-223, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 800, wait=False)
    wait(700)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()

    # Push the tire in
    r.move(160, 200, gyro_angle=-208)
    r.move(90, 200, gyro_angle=-250, stop=True)

    if reset:
        # Total = 4100
        motor_med_right.run_angle(1000, -800, wait=False)


def treadmill(reset=False):
    print('treadmill')
    if reset:
        gyro.reset_angle(-223)

    # Back off and turn back
    motor_med_right.run_angle(1000, -2000, wait=False)
    r.move(-90, 120, gyro_angle=-225)
    r.turn(-295, 100, 30)
    r.move(240, 130, gyro_angle=-300)

    # Back off to treadmill
    r.turn(-270, 100, 30)
    r.turn(-195, 20, 50, stop=True)
    wait(300)
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(-180, 200, gyro_angle=-183, stop=True)

    # Spin the treadmill
    robot.stop()
    motor_left.run_time(-1000, 2500)


def health_unit(reset=False):
    print('health_unit')
    if reset:
        gyro.reset_angle(-180)

    # Measure distance to wall to set line following length
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_delta = clip(90 - distance, -100, 100)

    # Move off treadmill
    r.move(100, 100, gyro_angle=-180)
    motor_med_right.run_angle(1000, 900, wait=False)
    motor_med_left.run_angle(1000, 300, wait=False)
    r.follow(660 + distance_delta, 150)

    r.turn(-122, -20, 40)
    r.move(40, 30, gyro_angle=-118, stop=True)

    # Hang health unit
    motor_med_left.run_angle(1000, 700)

    if reset:
        # Total = 5000
        motor_med_right.run_angle(1000, -900, wait=False)
        motor_med_left.run_angle(1000, -1000, wait=False)


def dance_floor(reset=False):
    print('dance_floor')
    if reset:
        gyro.reset_angle(-118)

    # Back off and turn to pass the bridge
    r.move(-60, 30, gyro_angle=-118)
    motor_med_left.run_angle(1000, 4000, wait=False)
    r.move(-60, 30, gyro_angle=-118)
    r.turn(-100, 80, 10)
    r.move(320, 200, gyro_angle=-96)

    # Turn to dance floor
    r.turn(-135, 200, 50)
    r.move(200, 200, gyro_angle=-140, stop=True)

    if reset:
        motor_med_left.run_angle(1000, -4000, wait=False)
        #motor_med_left.run_angle(1000, -5000, wait=False)
        #motor_med_right.run_angle(1000, -5000, wait=False)
        return

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


def test_flip():
    motor_med_right.run_angle(1000, 1500, wait=False)
    wait(500)
    robot.drive(-20, 0)
    wait(200)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()
    motor_med_right.run_angle(1000, -1500, wait=False)


if __name__ == "__main__":
    #tire_flip_large(True)
    #treadmill(True)
    #dance_floor(True)
    #tire_flip_small(True)
    #row_machine(True)
    #health_unit(True)
    run()
    #test_flip()
    #step_counter(True)

