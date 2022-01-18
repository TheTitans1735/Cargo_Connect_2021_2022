#!/usr/bin/env pybricks-micropython
from robot import *
import runs

ilan = Robot()

# Write your program here.
menu = ["Reset Wall","Trucks","Wing","Blue Green","Cargo Plane"]
i=0
ilan.ev3.speaker.beep()
#functions.pid_gyro(1000)
# Set up the Timer.  It is used to exit the input loop after 1 second.
timer = StopWatch()
# ilan.measure_wall()
# wait(1000000)
# ilan.pid_follow_line(ilan.color_sensor_right, 5000, 80, -1.5)

#ilan.robot.straight(100)


#Ilan moves the wall
# ilan.pid_follow_line(ilan.color_sensor_right,4000,150,1.5, True)

while False:
    #x=-1455
    #y=

    # Reset the Timer and the steps variable.
    timer.reset()
    
    # Wait until any Brick Button is pressed.
    while not any(ilan.ev3.buttons.pressed()):
        wait(10)

    # Respond to the Brick Button press.
    while timer.time() < 1000:
        # Check whether Up Button is pressed, and increase the steps
        # variable by 1 if it is.
        if Button.RIGHT in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            ilan.ev3.speaker.beep()
            i=i+1
            if i > len(menu)-1:
                i=0
            ilan.write(menu[i])

            # To avoid registering the same command again, wait until
            # the Up Button is released before continuing.
            while Button.RIGHT in ilan.ev3.buttons.pressed():
                wait(10)
        
        if Button.LEFT in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            ilan.ev3.speaker.beep()
            i=i-1
            if i < 0:
                i = len(menu)-1
            ilan.write(menu[i])
        if Button.CENTER in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            ilan.ev3.speaker.play_file(SoundFile.OKAY)
            if i==0:
                print("reset wall")
                #runs.go_trucks()
                ilan.measure_wall()
                
            
