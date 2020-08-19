#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import Motor, TouchSensor, ColorSensor, InfraredSensor, UltrasonicSensor, GyroSensor
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

def main():
    # Create your objects here.
    ev3 = EV3Brick()
    ev3.speaker.set_speech_options('en', 'f1', 160, None)

    # Initialize the robots
    left_motor = Motor(Port.B)
    right_motor = Motor(Port.C)
    robot = DriveBase(left_motor, right_motor, 50, 100)
    robot.settings(200, 400, 90, 180)

    # Start the mission
    ev3.light.on(Color.RED)
    ev3.speaker.say('Marshmallow Panda, Mission 4')

    # Move the robots
    robot.straight(500)
    # robot.turn(180)
    # robot.drive(300, 40)
    # wait(3000)
    # robot.stop()

    # Complete the mission
    ev3.speaker.say('Mission completed!')
    ev3.light.on(Color.GREEN)

if __name__ == "__main__":
    main()
