#!/usr/bin/env pybricks-micropython
from robot import *
# Write code here
ilan = Robot()
ilan.reset_wall()
ilan.beep()
#ilan.wall_x_motor.run_time(200,3000,Stop.COAST,True)
wait(1000)
def go_trucks():
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    # שמים את הזרוע
    wait(2000)

    # הזרוע נכנסת למשאית
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 70)
    ilan.beep()
    print("going")

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
    ilan.move_wall_to_point(x=500, y=0)
    ilan.reset_wall()
    ilan.move_wall_to_point(x=600, y=ilan.WALL_MAX_ANGLE_Y)

    # מוריד את הקיר השני
    ilan.pid_gyro(30, 50)
    ilan.move_wall_to_point(x=600, y=0)
    ilan.pid_gyro(-5, 50)
    # # ilan.robot.turn(-90)
    # ilan.pid_gyro(20)
    # #ilan.pid_follow_line(ilan.color_sensor_right,20,120,1.5, True)
    # #ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X,ilan.WALL_MAX_ANGLE_Y)  
    # ilan.beep()
go_trucks()
