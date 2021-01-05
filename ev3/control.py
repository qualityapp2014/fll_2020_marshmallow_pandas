from config import *

def move_motor(target, speed=100):
    left_motor.reset_angle(0)
    right_motor.reset_angle(0)
    
    left_motor.run_target(speed, target, wait=False)
    right_motor.run_target(speed, target, wait=False)
    while True:
        left_angle = left_motor.angle()
        right_angle = right_motor.angle()
        print('L: {}, R: {}, G: {}'.format(left_angle, right_angle, gyro.speed()))
        if left_angle >= target and right_angle >= target:
            break
        wait(1)
    
    left_motor.stop()
    right_motor.stop()


def move(distance, acceleration=100, interval=1, gyro_scaler=10):
    turn_rate = 0
    speed = 0
    direction = 1 if distance > 0 else -1
    speed_delta = direction * acceleration / interval
    
    robot.reset()
    gyro.reset_angle(0)
    while True:
        current_distance = robot.distance()
        if current_distance * direction >= distance * direction:
            break

        angle = gyro.angle()
        turn_rate = angle * gyro_scaler
        print('distance: {}, gyro angle: {}, turn rate: {}'.format(current_distance, angle, turn_rate))
        robot.drive(speed, turn_rate)
        wait(interval)

    robot.stop()

def move2(distance, acceleration=100, interval=1, gyro_scaler=3):
    turn_rate = 0
    speed = 0
    direction = 1 if distance > 0 else -1
    speed_delta = direction * acceleration / interval
    
    robot.reset()
    gyro.reset_angle(0)
    while True:
        current_distance = robot.distance()
        if current_distance * direction >= distance * direction:
            break

        angle = gyro.angle()
        turn_rate = -angle * gyro_scaler
        print('distance: {}, gyro angle: {}, turn rate: {}'.format(current_distance, angle, turn_rate))
        robot.drive(speed_delta, turn_rate)
        wait(interval)

    robot.stop()