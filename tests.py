#!/usr/bin/env pybricks-micropython
from robot import *
"""קובץ טסטים"""
ilan = Robot()

def clean_wheels():
    # מפעיל את הגלגלים
    while True:
        ilan.right_motor.run(500)
        ilan.left_motor.run(500)

ilan.beep()
# ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
# clean_wheels()
ilan.robot.reset()     
ilan.left_motor.run_time(200, 6)
ilan.right_motor.run_time(190, 6)
ilan.robot.stop()