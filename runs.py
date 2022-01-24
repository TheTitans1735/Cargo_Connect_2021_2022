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
    ilan.move_wall_to_point(720, 0)
    ilan.move_wall_to_point(0, 0)
    ilan.pid_follow_line(ilan.color_sensor_right, 10, 120, 1.3, True)
    ilan.move_wall_to_point(720, 200)
    ilan.pid_follow_line(ilan.color_sensor_right, 18, 120, 1.3, True)

    # מרים את הקיר ומוריד את הגשר הראשון
    ilan.move_wall_to_point(720, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_follow_line(ilan.color_sensor_right,15,100,1.3, True)

    # מוריד את הזרוע
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
    ilan.reset_wall()

    # מוריד את הקיר השני
    ilan.pid_follow_line(ilan.color_sensor_right,10,100,1.3, True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
    ilan.robot.straight(-100)
    
    # ilan.say("lets go titans! lets go rotem!")

def green_airplain_and_Containers():

    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    wait(3000)
    ilan.pid_gyro(25)
    ilan.pid_follow_line(ilan.color_sensor_right, 50, 100, 1.3, True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_gyro(5, Forward_Is_True=False) #ilan.run_straight(-5)
    ilan.pid_gyro(20, Forward_Is_True=False) #ilan.run_straight(-20)    
    
    
    # מוריד את המכולה מהמטוס
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    wait(500)
    # ilan.move_wall_to_point(0, 0)
    wait(500)
    # ilan.move_wall_to_point(300, 0)
    ilan.move_wall_to_point(300, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(0, 100)
    ilan.move_wall_to_point(0,  300)
    ilan.move_wall_to_point(500, 300)
    wait(500)
    ilan.move_wall_to_point(500, 650)
    wait(500)
    ilan.reset_wall()
    ilan.move_wall_to_point(0, 650)
    ilan.beep()
    ilan.pid_gyro(10) #ilan.run_straight(10)
    ilan.reset_wall()
    ilan.move_wall_to_point(0, 0)
    ilan.pid_gyro(10, Forward_Is_True=False) #ilan.run_straight(-10)
    ilan.beep()
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.turn(70)
    ilan.pid_gyro(33, Forward_Is_True=False) #ilan.run_straight(-33)
    ilan.turn(80)
    ilan.reset_wall_bottom_right()





def wing():
    ilan.reset_wall()
    ilan.pid_gyro(82)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 0)

# wing()
# go_trucks()


