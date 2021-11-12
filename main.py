#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
def move_wall(Vertical=0, horizontal=0):
    wall_up_down.dc(-1 * Vertical)
    


# Create your objects here.
ev3 = EV3Brick()
left_wheel = Motor(Port.B)
right_wheel = Motor(Port.C)

ilan = DriveBase(right_wheel , left_wheel , wheel_diameter = 62.4 , axle_track = 80)

wall_up_down = Motor(Port.A)
# up- , down+
wall_left_right = Motor(Port.D)
#right+ , left-


# Write your program here.

#Ilan goes back and forth
ilan.straight(-200)
wait(500)
ilan.straight(200)

#Ilan turns 360
ilan.turn(-480)
wait(500)

# #Ilan moves the Wall around 
ev3.speaker.beep()
wall_left_right.dc(170)
wait(2000)
wall_up_down.run_target(5000 , -1300 , Stop.BRAKE)
wait(2000)
wall_left_right.dc(-170)
wait(2000)
wall_up_down.dc(170)
wait(500)

# #Ilan did it his way! if you say so.
ev3.speaker.say('i did it my way')
ev3.speaker.beep()
