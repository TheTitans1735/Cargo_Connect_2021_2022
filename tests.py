#!/usr/bin/env pybricks-micropython
from robot import *
"""קובץ טסטים"""
ilan = Robot()


# ilan.drive_until_stalled(120)
ilan.beep()
ilan.pid_gyro(20, 500, False)