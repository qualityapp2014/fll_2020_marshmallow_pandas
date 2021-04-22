#!/usr/bin/env pybricks-micropython
from robot import *


def run():
    r = Robot(20)
    stop = False

    r.turn(32, 100, 45, stop=stop)
    r.move(600, 100, stop=stop)
    r.turn(-32, 100, 45, stop=stop)
    r.follow(250, 100, stop=stop)
    r.stop()
