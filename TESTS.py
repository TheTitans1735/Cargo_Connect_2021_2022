#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from robot import *
# Write code here
ilan = Robot()

ilan.pid_gyro(50, Forward_Is_True=True)
wait(1000)
ilan.pid_gyro(50, Forward_Is_True=False)
print(ilan.ev3.battery.current())