#!/usr/bin/env pybricks-micropython
from re import I
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
    ilan.pid_follow_line(ilan.color_sensor_right,50,120,1.3, True)
    ilan.move_wall_to_point(600, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_follow_line(ilan.color_sensor_right, 10, 120, 1.3, True)
    ilan.reset_wall_bottom_right()
    ilan.reset_wall()
    

    # מרים את הקיר ומוריד את הגשר הראשון
    ilan.move_wall_to_point(720, 150)
    ilan.pid_follow_line(ilan.color_sensor_right,15,100,1.3, True)

    # # מוריד את הזרוע
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
    ilan.reset_wall()

    # מוריד את הקיר השני
    ilan.pid_follow_line(ilan.color_sensor_right,10,100,1.3, True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
    ilan.robot.straight(-100)
    

def go_trucks2():
    
    # מאפס את הקיר
    ilan.reset_wall_bottom_right()

    # הזרוע נכנסת למשאית
    ilan.move_wall_to_point(720, 70)
    ilan.beep()
    print("going")


    # שמים את הזרוע

    wait(1000)
    # הרובוט נוסע אל הקו 
    ilan.pid_gyro(20,100)

    # הרובוט עוקב אחרי הקו עד לגשר, ושם את המשאיות בגשר
    ilan.pid_follow_line(ilan.color_sensor_right,45,120,1.35, True)
    ilan.move_wall_to_point(600, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_follow_line(ilan.color_sensor_right,10,120,1.3, True)
    ilan.move_wall_to_point(720, 250)
    ilan.pid_follow_line(ilan.color_sensor_right, 19, 150, 1.3, True)
    ilan.pid_gyro(5, 150, False)
    ilan.reset_wall()
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 300)
    ilan.pid_follow_line(ilan.color_sensor_right,20,150,1.3, True)
    ilan.reset_wall()
    ilan.pid_follow_line(ilan.color_sensor_right,10,150,1.3, True)
    ilan.reset_wall_bottom_right()
    ilan.run_straight(-10)
    ilan.pid_gyro(30, 150)
    ilan.turn(90)
    ilan.run_straight(-10)


# def prepare_go_trucks3():
def go_trucks3():
    # ilan.write2("the run 'go trucks'\n will run by pressing \nthe: \ncenter button")

    ilan.reset_wall_bottom_right()
    ilan.move_wall_to_point(450, 450)
    # שמים את הזרוע
    while not any(ilan.ev3.buttons.pressed()):
        wait(10)
       
    ilan.pid_gyro(60, 200)
    wait(500)
    ilan.turn(90 - ilan.gyro_sensor.angle())
    # while not any(ilan.ev3.buttons.pressed()):
    #         wait(10)
    
   
    
    # while not any(ilan.ev3.buttons.pressed()):
    #         wait(10)
    
    #ilan.pid_gyro(38, 700)
    ilan.pid_gyro(25, 700)
    ilan.move_wall_to_point(650, 450)
    ilan.move_wall_to_point(650, 350)
    ilan.pid_gyro(30, 200)



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
    # נסיעה על שהכנף נוגעת במתקן שלה
    ilan.pid_gyro(82)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 0)
    # קיר זז ותופס תרנגולת
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    wait(1000)
    ilan.pid_gyro(10, 600, Forward_Is_True = False)
    ilan.move_wall_to_point(400, 100)
    # חזרה הביתה
    ilan.pid_gyro(82, 600, Forward_Is_True = False) 

# wing()
# prepare_go_trucks3()
go_trucks3()
# ilan.say("hello. i'm ilan with a russian accent", 'ru', 1000)