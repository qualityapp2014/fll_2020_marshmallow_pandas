#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Create your objects here.
ev3 = EV3Brick()
ev3.speaker.set_speech_options('en', 'm1', 160, None)

# Initialize the robots
left_motor = Motor(Port.A)
right_motor = Motor(Port.B)
robot = DriveBase(left_motor, right_motor, 80, 80)
robot.settings(200, 400, 90, 180)

def main():
    # Start the mission
    ev3.light.on(Color.YELLOW)
    ev3.speaker.say('Marshmallow Panda, getting started!')

    # Move the robots
    robot.straight(100)
    robot.turn(90)
    robot.drive(300, 0)
    wait(300)
    robot.stop()

    # Complete the mission
    ev3.speaker.say('Mission completed!')
    ev3.light.on(Color.GREEN)

if __name__ == "__main__":
    main()