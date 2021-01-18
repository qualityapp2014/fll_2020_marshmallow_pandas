from config import *
import time

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

def turn(angle):
    gyro.reset_angle(0)
    angle_error = angle

    max_iter = 15

    while abs(angle_error) > 0 and max_iter > 0:
        robot.turn(angle_error)
        angle_error = angle - gyro.angle()
        print('Angle: {}, angle error: {}'.format(gyro.angle(), angle_error))
        max_iter = max_iter - 1
        # wait(angle_error*30)

def follow(distance, turn_kp=0.2, turn_ki=0.1, turn_kd=0):
    if distance < 0:
        print("Can't go follow lines backwards.")
        return

    # need to measure and tune this
    BLACK = 10
    WHITE = 94

    MIDPOINT = (BLACK + WHITE) / 2

    wait_interval = 1 # Don't need to change this.

    # constants in turn rate pid control
#    turn_kp = 0.1
#    turn_ki = 0
#    turn_kd = 0

    max_angle_error_i = 5 # bound on error integral
    max_turn_rate = 20

    max_speed = 100
    min_speed = 30
    ramp_distance = 200 # distance to ramp from min_speed to max_speed and down again
    ramp_down_distance_mult = 1.5 # sets a longer time to ramp down because of slippage

    ###

    angle_error = 0
    angle_error_prev = 0
    angle_error_i = 0
    angle_error_d = 0
     
    direction = 1 if distance > 0 else -1

    print('Turn pid: {}, {}, {}'.format(turn_kp, turn_ki, turn_kd))
    print('Turn rate limits:  max_angle_error_i: {}, max_turn_rate: {}'.format(max_angle_error_i, max_turn_rate))

    robot.reset()
    time_prev = time.time()

    while True:

        current_distance = abs(robot.distance())
        if current_distance >= direction * distance:
            break

        speed_up = min(1, current_distance / ramp_distance) * (max_speed - min_speed) + min_speed
        speed_down = min(1, (abs(distance) - current_distance) / (ramp_distance * ramp_down_distance_mult)) \
            * (max_speed - min_speed) + min_speed

        speed = min(speed_up, speed_down) * direction

        time_now = time.time()
        time_interval = time_now - time_prev

        angle = MIDPOINT - color_left.reflection()
        angle_error = 0 - angle # assume 0 set point
        angle_error_i += angle_error * time_interval # error angle integral
        angle_error_i = max(-max_angle_error_i, min(max_angle_error_i, angle_error_i)) # set bounds on error integral

        angle_error_d = (angle_error - angle_error_prev) / time_interval # angle error derivative
        angle_error_prev = angle_error

        turn_rate = turn_kp * angle_error + turn_ki * angle_error_i + turn_kd * angle_error_d # pid equation

        turn_rate = max(-max_turn_rate, min(max_turn_rate, turn_rate))

        print('distance: {}, gyro angle: {}, speed: {:0.1f}, turn rate: {:0.2f}, dt: {:0.3f}'
            .format(current_distance, angle, speed, turn_rate, time_interval))
        print('    angle_error: {}, angle_error_i: {:0.2f}, angle_error_d: {:0.2f}'
            .format(angle_error, angle_error_i, angle_error_d))
        robot.drive(speed, turn_rate)
        time_prev = time_now
        wait(wait_interval)

    robot.stop()


def move2(distance):
    """ Move straight and read gyro angle to move in a straight line. """

    wait_interval = 1 # Don't need to change this.

    # constants in turn rate pid control
    turn_kp = 3
    turn_ki = 3
    turn_kd = 0.1

    max_angle_error_i = 5 # bound on error integral
    angle_error_i_decay = 3 # decay on error integral to avoid oscillation around 0
    max_turn_rate = 20

    max_speed = 300
    min_speed = 30
    ramp_distance = 200 # distance to ramp from min_speed to max_speed and down again
    ramp_down_distance_mult = 1.5 # sets a longer time to ramp down because of slippage

    ###

    angle_error = 0
    angle_error_prev = 0
    angle_error_i = 0
    angle_error_d = 0
     
    direction = 1 if distance > 0 else -1

    print('Turn pid: {}, {}, {}'.format(turn_kp, turn_ki, turn_kd))
    print('Turn rate limits:  max_angle_error_i: {}, max_turn_rate: {}'.format(max_angle_error_i, max_turn_rate))

    robot.reset()
    gyro.reset_angle(0)
    time_prev = time.time()

    while True:

        current_distance = abs(robot.distance())
        if current_distance >= direction * distance:
            break

        speed_up = min(1, current_distance / ramp_distance) * (max_speed - min_speed) + min_speed
        speed_down = min(1, (abs(distance) - current_distance) / (ramp_distance * ramp_down_distance_mult)) \
            * (max_speed - min_speed) + min_speed

        speed = min(speed_up, speed_down) * direction

        time_now = time.time()
        time_interval = time_now - time_prev

        angle = gyro.angle()
        angle_error = 0 - angle # assume 0 set point
        angle_error_i += angle_error * time_interval # error angle integral
        angle_error_i = max(-max_angle_error_i, min(max_angle_error_i, angle_error_i)) # set bounds on error integral

        # We add an error integral decay because the EV3's angle sensor only gives readings in integer degrees.
        # To prevent oscillation around -1 to 1 degree, we decay the integral error.
        angle_error_i *= max(0, 1 - angle_error_i_decay*time_interval)

        angle_error_d = (angle_error - angle_error_prev) / time_interval # angle error derivative
        angle_error_prev = angle_error

        turn_rate = turn_kp * angle_error + turn_ki * angle_error_i + turn_kd * angle_error_d # pid equation

        turn_rate = max(-max_turn_rate, min(max_turn_rate, turn_rate))

        print('distance: {}, gyro angle: {}, speed: {:0.1f}, turn rate: {:0.2f}, dt: {:0.3f}'
            .format(current_distance, angle, speed, turn_rate, time_interval))
        print('    angle_error: {}, angle_error_i: {:0.2f}, angle_error_d: {:0.2f}'
            .format(angle_error, angle_error_i, angle_error_d))
        robot.drive(speed, turn_rate)
        time_prev = time_now
        wait(wait_interval)

    robot.stop()

def move_pid_gyro(distance, target_angle=0, max_speed=300, min_speed=30):
    """ Move with a target turning angle and distance """
    # modified from move2 by Yan, if target_angle is set to 0, then it moves along a straight line

    wait_interval = 1 # Don't need to change this.

    # constants in turn rate pid control
    turn_kp = 3
    turn_ki = 3
    turn_kd = 0.1

    max_angle_error_i = 5 # bound on error integral
    angle_error_i_decay = 3 # decay on error integral to avoid oscillation around 0
    max_turn_rate = 20

    #max_speed = 300
    #min_speed = 30
    ramp_distance = 200 # distance to ramp from min_speed to max_speed and down again
    ramp_down_distance_mult = 1.5 # sets a longer time to ramp down because of slippage

    ###

    #angle_error = 0
    angle_error = target_angle
    #angle_error_prev = 0
    angle_error_prev = target_angle

    angle_error_i = 0
    angle_error_d = 0
     
    direction = 1 if distance > 0 else -1

    print('Turn pid: {}, {}, {}'.format(turn_kp, turn_ki, turn_kd))
    print('Turn rate limits:  max_angle_error_i: {}, max_turn_rate: {}'.format(max_angle_error_i, max_turn_rate))

    robot.reset()
    gyro.reset_angle(0)
    time_prev = time.time()

    while True:

        current_distance = abs(robot.distance())
        if current_distance >= direction * distance:
            break

        speed_up = min(1, current_distance / ramp_distance) * (max_speed - min_speed) + min_speed
        speed_down = min(1, (abs(distance) - current_distance) / (ramp_distance * ramp_down_distance_mult)) \
            * (max_speed - min_speed) + min_speed

        speed = min(speed_up, speed_down) * direction

        time_now = time.time()
        time_interval = time_now - time_prev

        angle = gyro.angle()
        #angle_error = 0 - angle # assume 0 set point
        angle_error = target_angle - angle # assume 0 set point
        angle_error_i += angle_error * time_interval # error angle integral
        angle_error_i = max(-max_angle_error_i, min(max_angle_error_i, angle_error_i)) # set bounds on error integral

        # We add an error integral decay because the EV3's angle sensor only gives readings in integer degrees.
        # To prevent oscillation around -1 to 1 degree, we decay the integral error.
        angle_error_i *= max(0, 1 - angle_error_i_decay*time_interval)

        angle_error_d = (angle_error - angle_error_prev) / time_interval # angle error derivative
        angle_error_prev = angle_error

        turn_rate = turn_kp * angle_error + turn_ki * angle_error_i + turn_kd * angle_error_d # pid equation

        turn_rate = max(-max_turn_rate, min(max_turn_rate, turn_rate))

        print('distance: {}, gyro angle: {}, speed: {:0.1f}, turn rate: {:0.2f}, dt: {:0.3f}'
            .format(current_distance, angle, speed, turn_rate, time_interval))
        print('    angle_error: {}, angle_error_i: {:0.2f}, angle_error_d: {:0.2f}'
            .format(angle_error, angle_error_i, angle_error_d))
        robot.drive(speed, turn_rate)
        time_prev = time_now
        wait(wait_interval)

    robot.stop() 