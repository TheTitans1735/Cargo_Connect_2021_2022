#!/usr/bin/env pybricks-micropython
from robot import *
# Write code here
ilan = Robot()
#ilan.wall_x_motor.run_time(200,3000,Stop.COAST,True)
wait(1000)
def go_trucks():

    # מאפס את הקיר
    ilan.reset_wall_bottom_right()

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

    # מוריד את הזרוע
    ilan.move_wall_to_point(300, 0)

    # מוריד את הקיר השני
    ilan.pid_follow_line(ilan.color_sensor_right,10,50,1.3, True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, y=0)
    ilan.robot.straight(-100)
    
    ilan.say("lets go titans! lets go rotem!")

def green_airplain_and_Containers():

    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    ilan.pid_gyro(25)
    ilan.pid_follow_line(ilan.color_sensor_right, 55, 150, 1.3, True)
    ilan.run_straight(-25)

    # מוריד את המכולה מהמטוס
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    wait(2000)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    wait(2000)
    ilan.move_wall_to_point(600, ilan.WALL_MAX_ANGLE_Y)
    wait(2000)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    wait(2000)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    wait(2000)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
    wait(2000)
    ilan.run_straight(10)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    wait(2000)
    ilan.run_straight(-15)
    wait(2000)
    ilan.turn(70)
    wait(2000)
    ilan.run_straight(-15)
    wait(2000)

green_airplain_and_Containers()

