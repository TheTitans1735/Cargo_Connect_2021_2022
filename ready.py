#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from robot import *

"""
Functions to get ready
"""

ilan = Robot()

def clean_wheels():
    # מפעיל את הגלגלים
    while True:
        ilan.right_motor.run(500)
        ilan.left_motor.run(500)


TEXT_MENU = """Choose Action: 
  < - Clean Wheels
  > - 
  O - 
  V - 
  ^ - 
"""
            
# clean_wheels()      
# ilan.turn(-90)
