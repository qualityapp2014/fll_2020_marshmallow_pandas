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
    r.move(250, 120, gyro_angle=-1)

    robot.drive(60, 0)
    wait(600)
    fast_stop()

    if reset:
        # Left = 0, Right = 2000
        motor_med_right.run_angle(1000, -2000)


def health_unit(reset=False):
    print('health_unit')
    if reset:
        gyro.reset_angle(0)

    # Back off from step counter and turn to bridge
    r.move(-65, 100, gyro_angle=0)
    motor_med_left.run_angle(1000, 300, wait=False)
    r.turn(-62, 70, 40)
    r.move(100, 100, gyro_angle=-65)
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
    r.move(130, 100, gyro_angle=-55)
    r.move(25, 50, gyro_angle=-55, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 800, wait=False)
    wait(600)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()

    # Push the tire in
    r.move(110, 150, gyro_angle=-40, stop=True)
    if reset:
        # Left = 1000, Right = 4600
        motor_med_right.run_angle(1000, -2600, wait=False)


def row_machine(reset=False):
    print('row_machine')
    if reset:
        gyro.reset_angle(-40)

    # Move back to the lane
    r.move(-70, 100, gyro_angle=-40)
    motor_med_left.run_angle(1000, 3000, wait=False)
    motor_med_right.run_angle(1000, -3200, wait=False)
    r.turn(1, 140, 35)

    # Follow the lane and turn to row machine
    r.follow(220, 100)
    r.turn(-38, 100, 50)
    r.move(135, 100, gyro_angle=-40)
    r.move(30, 50, gyro_angle=-40, stop=True)

    # Pull the tire out
    motor_med_left.run_angle(1000, 500)
    motor_med_left.run_angle(500, 200, wait=False)
    r.turn(-75, -20, 30, stop=True)

    if reset:
        # Left = 4700, Right = 1400
        motor_med_right.run_angle(1000, 3200, wait=False)
        motor_med_left.run_angle(1000, -3700, wait=False)


def weight_machine(reset=False):
    print('weight_machine')
    if reset:
        gyro.reset_angle(-79)

    # Turn to weight machine
    motor_med_left.run_angle(1000, -800, wait=False)
    wait(200)

    r.move(-30, 50, gyro_angle=-79)
    r.turn(-112, 0, 50)
    r.move(180, 100, gyro_angle=-115)
    r.turn(-96, 100, 50)
    r.move(225, 100, gyro_angle=-90)
    r.turn(-74, 0, 30, stop=True)

    # Press down weight machine
    motor_med_left.run_angle(1000, 1100, wait=False)
    motor_med_right.run_angle(1000, 1400)
    motor_med_right.run_angle(1000, 800, wait=False)
    r.move(60, 50, gyro_angle=-70, stop=True)
    wait(300)
    
    if reset:
        # Left = 5000, Right = 3600
        wait(2000)
        motor_med_left.run_angle(1000, -300, wait=False)
        motor_med_right.run_angle(1000, -2200, wait=False)


def tire_flip_large(reset=False):
    print('tire_flip_large')
    if reset:
        gyro.reset_angle(-70)

    # Turn to weight machine
    motor_med_right.run_angle(1000, -1400, wait=False)
    r.move(-40, 80, gyro_angle=-70)
    
    r.turn(-120, 0, 60)
    motor_med_right.run_angle(1000, 1300, wait=False)
    r.turn(-220, -12, 60, stop=True)
    #r.move(-10, 50, gyro_angle=-223, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 800, wait=False)
    wait(700)
    robot.drive(-300, 0)
    wait(500)
    fast_stop()

    # Push the tire in
    r.move(120, 200, gyro_angle=-210)
    r.move(120, 200, gyro_angle=-235, stop=True)

    if reset:
        # Left = 5000, Right = 4300
        motor_med_right.run_angle(1000, -700, wait=False)


def treadmill(reset=False):
    print('treadmill')
    if reset:
        gyro.reset_angle(-216)

    # Back off and turn back
    r.move(-50, 200, gyro_angle=-216)
    motor_med_right.run_angle(1000, -2000, wait=False)

    # Move to treadmill
    r.turn(-278, 200, 50)
    r.move(465, 200, gyro_angle=-283)
    r.turn(-182, -30, 50, stop=True)

    # Back off to treadmill
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(-120, 200, gyro_angle=-180, stop=True)

    # Spin the treadmill
    robot.stop()
    motor_left.run_time(-1000, 2500)
    robot.stop()


def dance_floor(reset=False):
    print('dance_floor')
    if reset:
        gyro.reset_angle(-180)
        
    distance = ultrasonic.distance()

    # Back off and turn to pass the bridge
    r.move(80, 100, gyro_angle=-180)
    r.follow(80, 100)
    motor_med_right.run_angle(1000, 700, wait=False)

    distance_delta = clip(94 - distance, -100, 100)
    r.move(450 + distance_delta, 300, gyro_angle=-176)
    r.turn(-110, 200, 100)
    r.move(140, 200, gyro_angle=-98)
    motor_med_right.run_angle(1000, -5000, wait=False)
    motor_med_left.run_angle(1000, -5000, wait=False)
    r.move(140, 200, gyro_angle=-92)
    
    # Turn to dance floor
    r.turn(-130, 200, 50)
    r.move(100, 200, gyro_angle=-135, stop=True)

    if reset:
        wait(5000)
        motor_med_left.run_angle(1000, 5000, wait=False)
        motor_med_right.run_angle(1000, 4300, wait=False)
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

