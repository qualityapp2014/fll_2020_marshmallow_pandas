#!/usr/bin/env pybricks-micropython
from config import *

# Create a dictionary for switch case in 
missions={0:"No action", 1:"Mission 1", 2:"Mission 2", 3:"Mission 3", 4:"Mission 4", 5:"Combo Mission 5", 6:"Combo Mission 6", 7:"Exit"}

def read_buttons(buttons_pressed):
    mission = 0
    if(Button.LEFT in buttons_pressed) and (Button.UP in buttons_pressed):
        mission = 5

    if(Button.RIGHT in buttons_pressed) and (Button.UP in buttons_pressed):
        mission = 6

    if(Button.UP in buttons_pressed) and (Button.DOWN in buttons_pressed):
        mission = 7

    if(mission == 0) and (Button.LEFT in buttons_pressed):
        mission = 1

    if(mission == 0) and (Button.UP in buttons_pressed):
        mission = 2

    if(mission == 0) and (Button.RIGHT in buttons_pressed):
        mission = 3

    if(mission == 0) and (Button.DOWN in buttons_pressed):
        mission = 4

    return mission

def execute_mission1():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[1] + ' Started!')
    return

def execute_mission2():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[2] + ' Started!')
    return

def execute_mission3():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[3] + ' Started!')
    return

def execute_mission4():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[4] + ' Started!')
    return

def execute_mission5():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[5] + ' Started!')
    return

def execute_mission6():
    ev3.light.on(Color.RED)
    ev3.speaker.say( missions[6] + ' Started!')
    return

def run_mission(mission):
    stop_program = False
    if mission == 1:
        execute_mission1()
    elif mission == 2:
        execute_mission2()
    elif mission == 3:
        execute_mission3()
    elif mission == 4:
        execute_mission4()
    elif mission == 5:
        execute_mission5()
    elif mission == 6:
        execute_mission6()
    elif mission == 0:
        #no action
        ev3.speaker.say('Doing Nothing!') 
    else:
        # set stop_program to true to exit
        stop_program = True

    return stop_program
    

def main():
    # Start the mission
    ev3.light.on(Color.YELLOW)
    ev3.speaker.say('Marshmallow Panda, getting started, please select the mission to execute!')

    while True:
        mission = 0
        while mission == 0:
            button_pressed = ev3.buttons.pressed()
            mission = read_buttons(button_pressed)
            print(mission)
        
        stop_program = run_mission(mission)    
        if stop_program:
            break
        else:
            continue

    ev3.speaker.say('Marshmallow Panda, all missions completed!')

if __name__ == "__main__":
    main()