#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot()
    gyro.reset_angle(0)

<<<<<<< HEAD
    # Move to the center lane
    r.move(200, 200)
    r.follow(260, 150, find_lane=True)
    r.turn(-51, 100, 50)
    motor_med_right.run_angle(1000, 2200, wait=False)
    r.follow(260, 100)

    # Measure distance and turn
    distance = ultrasonic.distance()
    print("Distance", distance)
    distance_next = clip(45 + 660 - distance, 0, 200)
    r.follow(distance_next, 50, stop=True)
    print("Distance", ultrasonic.distance())

    # Flip the blue block
    motor_med_right.run_angle(1000, -2200, wait=False)
    wait(1000)

    # Drop the basketball
    r.turn(-112, 0, 50)
    # Reduce speed and overrun a bit to ensure good contact
    r.move(100, 100, gyro_angle=-118)
    r.move(20, 20, gyro_angle=-118)
    
    # Move back to fit fork lift
    r.move(-50, 50)
    r.turn(-111, 0, 20)
    r.move(40, 30, gyro_angle=-109, stop=True)
    
    # Lift crate
    motor_med_left.run_angle(1000, -1160, wait=False)
    wait(2500)
    motor_med_left.run_angle(1000, 1160, wait=False)
    wait(500)

    # Back off and set arm for health unit
    r.move(-120, 100)
    motor_med_right.run_angle(1000, 3800, wait=False)

    # Find lane by checking on white color
    r.turn(-124, -100, 50)
    r.turn(-150, 0, 20, terminate=is_right_white)

    # Follow the line to pick up the health unit
    r.follow(240, 50, use_left=False)

    # Return to the base
    motor_med_right.run_angle(1000, -3800, wait=False)
    r.move(-80, 30)
    r.turn(-30, -100, 60)
    r.move(-560, 400, stop=True)

    motor_med_left.brake()
    motor_med_right.brake()

=======
    # Move forward and follow the line
    r.move(100, 100)
    r.follow(240, 100, use_left=False)

    # Accelerate and brake suddenly to throw the bar
    robot.drive(800, 20)
    wait(100)
    robot.drive(0, 0)
    wait(1000)
    robot.stop()

    # Move back
    r.move(-250, 100)
    r.turn(20, -500, 10)
    r.stop()
>>>>>>> master

if __name__ == "__main__":
    run()
