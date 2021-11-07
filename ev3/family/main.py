#!/usr/bin/env pybricks-micropython
from config import *

import run_01
import run_02
import run_03


def run(number):
    if number == 1:
        run_01.run()
    if number == 2:
        run_02.run()
    if number == 3:
        run_03.run()


def main():
    # Turn on RED light to indicate ready
    ev3.light.on(Color.RED)

    number = 1
    ev3.screen.print("Run", number)
    while True:
        buttons = ev3.buttons.pressed()
        if Button.CENTER in buttons:
            ev3.screen.print("Starting Run", number)
            ev3.light.on(Color.GREEN)
            run(number)
            ev3.light.on(Color.RED)
            number += 1
            ev3.screen.print("Run", number)
        elif Button.DOWN in buttons:
            if number < 3:
                number += 1
                ev3.screen.print("Run", number)
                wait(250)
        elif Button.UP in buttons:
            if number > 1:
                number -= 1
                ev3.screen.print("Run", number)
                wait(250) 

if __name__ == "__main__":
    main()