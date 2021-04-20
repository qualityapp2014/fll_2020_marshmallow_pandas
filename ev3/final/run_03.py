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
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(800, 300, gyro_angle=2)
    # Slow down to push to the end
    r.move(280, 120, gyro_angle=-1, stop=True)

    if reset:
        # Left = 0, Right = 2000
        motor_med_right.run_angle(1000, -2000)


def health_unit(reset=False):
    print('health_unit')
    if reset:
        gyro.reset_angle(0)

    # Back off from step counter and turn to bridge
    r.move(-55, 120, gyro_angle=0)
    motor_med_left.run_angle(1000, 300, wait=False)
    r.turn(-62, 70, 40)
    r.move(100, 120, gyro_angle=-65)
    r.move(20, 50, gyro_angle=-65, stop=True)

    # Hang health unit
    motor_med_left.run_angle(1000, 700)

    if reset:
        # Left = 1000, Right = 2000
        wait(1000)
        motor_med_left.run_angle(1000, -1000)


def tire_flip_small(reset=False):
    print('tire_flip_small')
    if reset:
        gyro.reset_angle(-67)

    # Back off and turn to tire
    r.move(-60, 100, gyro_angle=-65)
    motor_med_right.run_angle(1000, 1800, wait=False)

    r.turn(-50, 30, 50)
    r.move(100, 150, gyro_angle=-55)
    r.move(40, 50, gyro_angle=-55, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 600, wait=False)
    wait(500)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()

    # Push the tire in
    r.move(110, 150, gyro_angle=-40, stop=True)
    if reset:
        # Left = 1000, Right = 4400
        motor_med_right.run_angle(1000, -2400, wait=False)


def row_machine(reset=False):
    print('row_machine')
    if reset:
        gyro.reset_angle(-40)

    # Move back to the lane
    r.move(-50, 100, gyro_angle=-40)
    motor_med_left.run_angle(1000, 3000, wait=False)
    motor_med_right.run_angle(1000, -2900, wait=False)
    r.turn(-3, 140, 35)

    # Follow the lane and turn to row machine
    r.follow(220, 150)
    r.turn(-37, 100, 50)
    r.move(130, 150, gyro_angle=-40)
    r.move(30, 50, gyro_angle=-40, stop=True)

    # Pull the tire out
    motor_med_left.run_angle(1000, 300)
    motor_med_left.run_angle(500, 400, wait=False)
    r.turn(-74, -20, 30, stop=True)

    if reset:
        # Left = 4700, Right = 1500
        motor_med_right.run_angle(1000, 2900, wait=False)
        motor_med_left.run_angle(1000, -3700, wait=False)


def weight_machine(reset=False):
    print('weight_machine')
    if reset:
        gyro.reset_angle(-79)

    # Turn to weight machine
    motor_med_left.run_angle(1000, -800, wait=False)
    wait(100)

    r.move(-30, 50, gyro_angle=-79)
    r.turn(-110, 0, 50)
    r.move(150, 150, gyro_angle=-115)
    r.turn(-95, 150, 50)
    r.move(175, 150, gyro_angle=-90)
    r.turn(-80, 20, 50, stop=True)

    # Press down weight machine
    motor_med_left.run_angle(1000, 1100, wait=False)
    motor_med_right.run_angle(1000, 1200)
    motor_med_right.run_angle(1000, 800, wait=False)
    r.move(50, 50, gyro_angle=-70, stop=True)
    wait(300)
    
    if reset:
        # Left = 5000, Right = 3500
        wait(2000)
        motor_med_left.run_angle(1000, -300, wait=False)
        motor_med_right.run_angle(1000, -2000, wait=False)


def tire_flip_large(reset=False):
    print('tire_flip_large')
    if reset:
        gyro.reset_angle(-70)

    # Turn to weight machine
    motor_med_right.run_angle(1000, -1200, wait=False)
    r.move(-40, 80, gyro_angle=-70)
    
    r.turn(-120, -30, 60)
    motor_med_right.run_angle(1000, 1200, wait=False)
    r.turn(-208, -30, 60)
    r.move(-20, 50, gyro_angle=-210, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 600)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()

    # Push the tire in
    r.move(150, 200, gyro_angle=-200)
    r.move(100, 200, gyro_angle=-220, stop=True)

    if reset:
        # Left = 5000, Right = 4100
        motor_med_right.run_angle(1000, -600, wait=False)


def treadmill(reset=False):
    print('treadmill')
    if reset:
        gyro.reset_angle(-216)

    # Back off and turn back
    motor_med_right.run_angle(1000, -2000, wait=False)
    r.move(-30, 200, gyro_angle=-216)

    # Move to treadmill
    r.turn(-280, 200, 50)
    r.move(390, 200, gyro_angle=-284)
    r.turn(-185, -30, 50, stop=True)

    # Back off to treadmill
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(-130, 200, gyro_angle=-180, stop=True)

    # Spin the treadmill
    robot.stop()
    motor_left.run_time(-1000, 2500)


def dance_floor(reset=False):
    print('dance_floor')
    if reset:
        gyro.reset_angle(-180)

    # Back off and turn to pass the bridge
    motor_med_right.run_angle(1000, 900, wait=False)

    r.move(80, 100)
    r.follow(50, 100)
    r.move(460, 200, gyro_angle=-180)
    r.turn(-100, 100, 50)
    r.move(160, 200, gyro_angle=-96)
    motor_med_right.run_angle(1000, -5000, wait=False)
    motor_med_left.run_angle(1000, -5000, wait=False)
    r.move(150, 200, gyro_angle=-96)
    
    # Turn to dance floor
    r.turn(-120, 200, 50)
    r.move(200, 200, gyro_angle=-140, stop=True)

    if reset:
        wait(5000)
        motor_med_left.run_angle(1000, 5000, wait=False)
        motor_med_right.run_angle(1000, 4100, wait=False)
        return

    while True:
        r.turn(-145, 0, 30)
        r.turn(-135, 0, 30)


def run():
    gyro.reset_angle(0)
    
    step_counter()
    health_unit()
    tire_flip_small()
    row_machine()
    weight_machine()
    tire_flip_large()
    treadmill()
    dance_floor()


if __name__ == "__main__":
    #step_counter(True)
    #row_machine(True)
    #weight_machine(True)
    #treadmill(True)
    #dance_floor(True)
    #tire_flip_small(True)
    #tire_flip_large(True)
    #health_unit(True)
    run()

