#!/usr/bin/env pybricks-micropython
from robot import *

def step_counter(reset=False):
    print('step_counter')
    if reset:
        gyro.reset_angle(0)

    # Move straight to step counter
    motor_med_right.run_angle(1000, 2400, wait=False)
    r.move(830, 300, gyro_angle=1)
    # Slow down to push to the end
    r.move(250, 100, gyro_angle=1)
    robot.drive(50, 0)
    wait(1000)
    robot.drive(0, 0)
    wait(300)

    if reset:
        motor_med_right.run_angle(1000, -2400, wait=False)


def tire_flip_small(reset=False):
    print('tire_flip_small')
    if reset:
        gyro.reset_angle(0)

    # Back off from step counter and turn to lane
    r.move(-60, 100, gyro_angle=0)
    r.turn(-10, 70, 30)
    motor_med_right.run_angle(1000, 1300, wait=False)
    r.turn(-50, 70, 30)
    r.move(170, 100, gyro_angle=-51, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 1200, wait=False)
    wait(600)
    robot.drive(-20, 0)
    wait(200)
    robot.drive(-300, 0)
    wait(400)
    robot.drive(0, 0)
    wait(1000)

    # Push the tire in
    r.move(130, 100, gyro_angle=-45, stop=True)
    if reset:
        motor_med_right.run_angle(1000, -2500, wait=False)


def row_machine(reset=False):
    print('row_machine')
    if reset:
        gyro.reset_angle(-45)

    # Move back to the lane
    r.move(-80, 100, gyro_angle=-45)
    motor_med_right.run_angle(1000, -2900, wait=False)
    r.turn(-10, 100, 50)

    # Follow the lane and turn to row machine
    r.follow(310, 100)
    r.turn(-88, 100, 50)
    r.move(200, 100, gyro_angle=-90)
    r.turn(3, 0, 50, stop=True)

    # Move close and pull the tire out
    motor_med_right.run_angle(1000, 2000)
    motor_med_right.run_angle(1000, 400, wait=False)
    r.move(-130, 30, gyro_angle=2, stop=True)
    motor_med_right.run_angle(1000, -3300, wait=False)
    wait(500)

    if reset:
        motor_med_right.run_angle(1000, -3800, wait=False)


def weight_machine(reset=False):
    print('weight_machine')
    if reset:
        gyro.reset_angle(-5)

    # Turn to weight machine
    r.turn(-87, 30, 50)
    r.move(150, 100, gyro_angle=-90)
    r.turn(-75, 20, 30, stop=True)

    # Press down weight machine
    motor_med_right.run_angle(1000, 1400)
    motor_med_right.run_angle(1000, 900, wait=False)
    r.move(50, 30, gyro_angle=-70, stop=True)


def tire_flip_large(reset=False):
    print('tire_flip_large')
    if reset:
        gyro.reset_angle(-70)

    # Turn to weight machine
    motor_med_right.run_angle(1000, -1300, wait=False)
    r.move(-30, 50, gyro_angle=-70)
    
    r.turn(-120, -30, 50)
    motor_med_right.run_angle(1000, 1000, wait=False)
    r.turn(-210, -30, 50)
    r.move(-40, 50, gyro_angle=-215, stop=True)

    # Flip the tire
    motor_med_right.run_angle(1000, 800, wait=False)
    wait(600)
    robot.drive(-300, 0)
    wait(500)
    robot.drive(0, 0)
    wait(500)

    # Push the tire in
    r.move(180, 100, gyro_angle=-208)
    r.move(100, 100, gyro_angle=-225, stop=True)


def treadmill(reset=False):
    print('treadmill')
    if reset:
        gyro.reset_angle(-225)

    # Back off and turn back
    motor_med_right.run_angle(1000, -2000, wait=False)
    r.move(-60, 100, gyro_angle=-225)
    r.turn(-290, 100, 30)
    r.move(160, 100, gyro_angle=-295)

    # Back off to treadmill
    r.turn(-260, 100, 30)
    r.turn(-188, 30, 50)
    motor_med_right.run_angle(1000, 2000, wait=False)
    r.move(-180, 200, gyro_angle=-180, stop=True)

    # Spin the treadmill
    robot.stop()
    motor_left.run_time(-800, 2500)
    

def health_unit(reset=False):
    print('health_unit')
    if reset:
        gyro.reset_angle(-180)

    # Move off treadmill
    motor_med_right.run_angle(1000, 800, wait=False)
    r.move(100, 100, gyro_angle=-180)
    r.follow(420, 100)

    r.turn(-118, 0, 50)
    r.move(20, 20, gyro_angle=-115, stop=True)

    # Hang health unit
    motor_med_left.run_angle(1000, 1000)


def dance_floor(reset=False):
    print('dance_floor')
    if reset:
        gyro.reset_angle(-115)

    # Back off and turn to pass the bridge
    r.move(-70, 30, gyro_angle=-115)
    r.turn(-176, 0, 50)
    motor_med_left.run_angle(1000, 4000, wait=False)
    r.move(250, 100, gyro_angle=-180)
    r.turn(-95, 0, 50)
    r.move(400, 200, gyro_angle=-90)

    # Turn to dance floor
    r.turn(-130, 200, 50)
    r.move(200, 200, gyro_angle=-140, stop=True)

    motor_med_left.run_angle(1000, -5000, wait=False)
    motor_med_right.run_angle(1000, -5000, wait=False)
    return

    while True:
        r.turn(-145, 0, 30)
        r.turn(-135, 0, 30)


def run():
    step_counter(True)
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
    robot.drive(0, 0)
    wait(1000)
    motor_med_right.run_angle(1000, -1500, wait=False)

if __name__ == "__main__":
    #tire_flip_large(True)
    #treadmill(True)
    #run()
    tire_flip_small(True)

