#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from robot import *
# # Write code here
ilan = Robot()

def clean_wheels():
    # מפעיל את הגלגלים
    while True:
        ilan.right_motor.run(120)
        ilan.left_motor.run(120)


TEXT_MENU = """Choose Action: 
  < - Clean Wheels
  > - Light Sensor Calibration
  O - 
  V -
  ^ - 
"""

def get_ready():
    """!! CHECKLISTTTT !!"""
    
    while True:
        
        # מדפיס את טקסט הריצות על הרובוט ועל מסך המחשב
        ilan.write(TEXT_MENU)

        # מחכה ללחיצת כפתור
        while not any(ilan.ev3.buttons.pressed()):
            wait(10)
        
        # כפתור שמאלי - ראן לקיחת מכולות
        if Button.LEFT in ilan.ev3.buttons.pressed():
            clean_wheels()

        # elif Button.RIGHT in ilan.ev3.buttons.pressed():
           

        # elif Button.DOWN in ilan.ev3.buttons.pressed():
           


        # elif Button.UP in ilan.ev3.buttons.pressed():
            
# clean_wheels()      
ilan.turn(-90)