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
    ilan.pid_gyro(20,100)

    # הרובוט עוקב אחרי הקו עד לגשר, ושם את המשאיות בגשר
    ilan.pid_follow_line(ilan.color_sensor_right,45,120,1.3, True)
    ilan.beep()
    ilan.move_wall_to_point(720, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_follow_line(ilan.color_sensor_right, 10, 120, 1.3, True)
    ilan.move_wall_to_point(720, 150)
    ilan.pid_follow_line(ilan.color_sensor_right, 10, 120, 1.3, True)

    # # מרים את הקיר ומוריד את הגשר הראשון
    # ilan.move_wall_to_point(600, ilan.WALL_MAX_ANGLE_Y-100)
    # ilan.pid_follow_line(ilan.color_sensor_right,30,100,1.3, True)

    # מוריד את הזרוע
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(300, 0)

    # מוריד את הקיר השני
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, y=0)
    ilan.pid_follow_line(ilan.color_sensor_right,10,50,1.3, True)
    # ilan.robot.straight(-100)
    
    ilan.say("lets go titans! lets go rotem!")

def green_airplain_and_Containers():

    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    wait(2000)
    ilan.pid_gyro(25)
    ilan.pid_follow_line(ilan.color_sensor_right, 50, 100, 1.3, True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.run_straight(-5)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.run_straight(-20)
    
    
    # מוריד את המכולה מהמטוס
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(0, 100)
    ilan.move_wall_to_point(200, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(0, 100)
    ilan.move_wall_to_point(200,  ilan.WALL_MAX_ANGLE_Y)
    ilan.run_straight(10)
    ilan.move_wall_to_point(200, 100)
    ilan.beep()
    ilan.run_straight(-10)
    ilan.beep()
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.turn(70)
    ilan.run_straight(-35)
    ilan.turn(90)

green_airplain_and_Containers()

