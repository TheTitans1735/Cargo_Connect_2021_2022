#!/usr/bin/env pybricks-micropython

from robot import Robot
from pybricks.tools import wait, StopWatch, DataLog

# Write your program here.
ilan = Robot()
#Ilan goes back and forth

#Ilan moves the wall
ilan.move_wall(-100)
ilan.move_wall(150)

#Ilan moves forward
ilan.run_cm(20)

ilan.ev3.speaker.set_speech_options(voice='whisper')

#Ilan says angle, turns, X3
a=str(ilan.gyro_sensor.angle())
ilan.say("eedosa is" + a)
ilan.turn(r, 360)
a=str(ilan.gyro_sensor.angle())
ilan.say("eedosa" + a)
ilan.turn(l, 360)
a=str(ilan.gyro_sensor.angle())
ilan.say("eedosa" + a)

ilan.ev3.speaker.voice_opinion
ilan.say("Ani Eshmor Ba GitHub")

# Ilan did it his way! if you say so.
ev3.speaker.say('i did it my way')