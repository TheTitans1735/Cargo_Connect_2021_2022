#!/usr/bin/env pybricks-micropython
from robot import *
# Write code here
ilan = Robot()
ilan.reset_wall()
ilan.beep()
#ilan.wall_x_motor.run_time(200,3000,Stop.COAST,True)
wait(1000)
def go_trucks():
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    # הזרוע נכנסת למשאית
    ilan.move_wall_to_point(720, 70)
    ilan.beep()
    print("going")


    # שמים את הזרוע
    wait(4000)

    # הרובוט נוסע אל הקו 
    ilan.pid_gyro(15,100)

    # הרובוט עוקב אחרי הקו עד לגשר, ושם את המשאיות בגשר
    ilan.pid_follow_line(ilan.color_sensor_right,62,120,1.3, True)
    ilan.beep()

    # מרים את הקיר ומוריד את הגשר הראשון
    ilan.move_wall_to_point(600, ilan.WALL_MAX_ANGLE_Y-100)
    ilan.pid_follow_line(ilan.color_sensor_right,30,100,1.3, True)

    # ilan.move_wall_to_point(600, 150)
    # ilan.pid_gyro(-13,100)

    # מוריד את הזרוע
    ilan.move_wall_to_point(300, 0)
    ilan.reset_wall()

    # מוריד את הקיר השני
    ilan.pid_follow_line(ilan.color_sensor_right,10,50,1.3, True)
    ilan.beep()
    ilan.reset_wall()
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, y=0)
    ilan.beep()
 
    ilan.robot.straight(-100)
    
    ilan.say("lets go titans! lets go rotem!")
    
 


    # # ilan.robot.turn(-90)
    # ilan.pid_gyro(20)
    # #ilan.pid_follow_line(ilan.color_sensor_right,20,120,1.5, True)
    # #ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X,ilan.WALL_MAX_ANGLE_Y)  
    # ilan.beep()



go_trucks()