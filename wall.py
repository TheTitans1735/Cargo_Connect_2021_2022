#!/usr/bin/env pybricks-micropython
from pybricks.tools import wait
from robot import *

ilan = Robot()
# Write your program here.
ilan.beep()
# Set up the Timer.  It is used to exit the input loop after 1 second.
ilan.reset_wall()
# wait(1500)
print("---")
# ilan.move_wall_to_point(200,150)
# wait(1500)
timer = StopWatch()
speed = 100 #start with
ilan.write("Use buttons to move wall")
while True:
    ilan.write(str(ilan.wall_x_motor.angle()) + "," + str(ilan.wall_y_motor.angle()))
    # Reset the Timer and the steps variable.
    timer.reset()
    
    # Wait until any Brick Button is pressed.
    while not any(ilan.ev3.buttons.pressed()):
        wait(10)

    # Respond to the Brick Button press.
    while True:
        # Check whether Up Button is pressed, and increase the steps
        # variable by 1 if it is.
        if Button.RIGHT in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            #ilan.ev3.speaker.beep()
            #ilan.wall_x_motor.run_time(speed, 180, then=Stop.BRAKE, wait=True)
            ilan.wall_x_motor.dc(speed)
            #ilan.write(str(ilan.wall_x_motor.angle()) + ", " + str(ilan.wall_y_motor.angle()))
            
            # To avoid registering the same command again, wait until
            # the Up Button is released before continuing.
            #while Button.RIGHT in ilan.ev3.buttons.pressed():
            #    wait(10)
        if Button.LEFT in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            #ilan.ev3.speaker.beep()
            #ilan.wall_x_motor.run_time(speed * -1, 180, then=Stop.BRAKE, wait=True)
            ilan.wall_x_motor.dc(-speed)
            ilan.write(str(ilan.wall_x_motor.angle()) + ", " + str(ilan.wall_y_motor.angle()))
            # To avoid registering the same command again, wait until
            # the Up Button is released before continuing.
            #while Button.RIGHT in ilan.ev3.buttons.pressed():
            #    wait(10)
        if Button.UP in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            #ilan.ev3.speaker.beep()
            #ilan.wall_y_motor.run_time(speed , 180, then=Stop.BRAKE, wait=True)
            ilan.wall_y_motor.dc(speed)
            ilan.write(str(ilan.wall_x_motor.angle()) + ", " + str(ilan.wall_y_motor.angle()))
            # To avoid registering the same command again, wait until
            # the Up Button is released before continuing.
            #while Button.RIGHT in ilan.ev3.buttons.pressed():
            #    wait(10)
        if Button.DOWN in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            timer.reset()
            #ilan.ev3.speaker.beep()
            #ilan.wall_y_motor.run_time(speed *-1, 180, then=Stop.BRAKE, wait=True)
            ilan.wall_y_motor.dc(-speed)

            ilan.write(str(ilan.wall_x_motor.angle()) + ", " + str(ilan.wall_y_motor.angle()))
            # To avoid registering the same command again, wait until
            # the Up Button is released before continuing.
            #while Button.RIGHT in ilan.ev3.buttons.pressed():
            #    wait(10)
        if Button.CENTER in ilan.ev3.buttons.pressed():
            # Reset the Timer to enable entering multiple commands.
            speed -= 10
            if speed <= 0:
                speed = 10
            
            #ilan.write("speed = " + str(speed))
        ilan.wall_y_motor.hold()
        ilan.wall_x_motor.hold()