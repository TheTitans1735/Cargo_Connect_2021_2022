#!/usr/bin/env pybricks-micropython
from re import I
from robot import *
# Write code here
ilan = Robot()
#ilan.wall_x_motor.run_time(200,3000,Stop.COAST,True)
ilan.say("I am ready!")
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



def green_airplane_and_Containers():
    debug = False
    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    
    ilan.wait_for_button("10. start",True)
    wait(500)
    ilan.pid_gyro(25, 250)
    ilan.pid_follow_line(ilan.color_sensor_right, 50, 100, 1.3, True)
    #turn engine over
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    #ilan.pid_gyro(20, Forward_Is_True=False) #ilan.run_straight(-20)    
    ilan.pid_gyro(25, Forward_Is_True=False) #ilan.run_straight(-20)
    
    
    # מוריד את המכולה מהמטוס
    #move to left
    ilan.wait_for_button("20. wall left",debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    #wait(500)
    # ilan.move_wall_to_point(0, 0)
    #wait(500)
    # ilan.move_wall_to_point(300, 0)
    #go right to center
    
    # ilan.wait_for_button("30. wall x center")
    # ilan.move_wall_to_point(300, ilan.WALL_MAX_ANGLE_Y)
    # #go down
    # ilan.wait_for_button("40. wall left")
    # ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)
    ilan.wait_for_button("50. wall down",debug)
    ilan.move_wall_to_point(0, 100)
    ilan.wait_for_button("60. wall up middle",debug)
    ilan.move_wall_to_point(0,  300)
    ilan.wait_for_button("70. wall right",debug)
    ilan.move_wall_to_point(500, 300)
    ilan.wait_for_button("80. wall up",debug)
    #wait(500)
    ilan.move_wall_to_point(500, ilan.WALL_MAX_ANGLE_Y)
    #wait(500)
    ilan.wait_for_button("90. wall left then down",debug)
    ilan.move_wall_to_point(80, ilan.WALL_MAX_ANGLE_Y)
    #wait(500)
    ilan.move_wall_to_point(80, 0)
    ilan.wait_for_button("100. up",debug)
    ilan.move_wall_to_point(0, 650)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 650)
    #ilan.beep()
    ilan.pid_gyro(10) #ilan.run_straight(10)
    ilan.wait_for_button("110. wall reset",debug)
    #ilan.reset_wall()
    ilan.wait_for_button("120. wall 0,0",debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-100, 0)
    ilan.pid_gyro(10, Forward_Is_True=False) #ilan.run_straight(-10)
    ilan.beep()
    ilan.wait_for_button("130. wall up",debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.turn(70)
    ilan.pid_gyro(33, 500, Forward_Is_True=False) #ilan.run_straight(-33)
    ilan.turn(80, 200)
    ilan.wait_for_button("140. wall reset right",debug)
    #ilan.reset_wall_bottom_right()





def wing():
    watch = StopWatch()
    ilan.reset_wall()
    while not any(ilan.ev3.buttons.pressed()):
        wait(10)
    # נסיעה על שהכנף נוגעת במתקן שלה
    watch = StopWatch()
    ilan.pid_gyro(72, 250, Kp = 3.05)
    ilan.pid_gyro(10, 120)

    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 0)
    # קיר זז ותופס תרנגולת
    ilan.move_wall_to_point(600, 0)
    #wait(1000)
    ilan.pid_gyro(21, 100, Forward_Is_True = False)
    ilan.move_wall_to_point(0, 100)
    # חזרה הביתה
    ilan.pid_gyro(52, 500, Forward_Is_True = False) 
    ilan.pid_gyro(3, 100, Forward_Is_True = False)
    print(watch.time())

def take_container_activate():

    #מאפס את הקיר לאמצע
    ilan.reset_wall()
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y)

    #מחכה להלבשת הזרוע
    ilan.wait_for_button("Place arm", True)
    ilan.write("Far  |  Center | Close")

    #בודק לאיזה מקום צריך להגיע - ימין, אמצע שמאל
    while True:
        # Wait until any Brick Button is pressed.
        while not any(ilan.ev3.buttons.pressed()):
           wait(10)

        # Respond to the Brick Button press.
        
        if Button.RIGHT in ilan.ev3.buttons.pressed():
            ilan.write("Right Container")
            take_container(0)
            return

        elif Button.CENTER in ilan.ev3.buttons.pressed():
            ilan.write("Middle Container")
            take_container(1)
            return

        elif Button.LEFT in ilan.ev3.buttons.pressed():
            ilan.write("Left Container")
            take_container(2)
            return

        
            
def take_container(port: int):
    debug = False

    #נוסע אל ועל הקו השחור
    ilan.pid_gyro(20)
    ilan.pid_follow_line(ilan.color_sensor_right, 98, 130, 1.355, True)
    wait(1000)

    #בודק האם צריך להגיע למכולה ימין, אמצע או שמאל ונוסע קדימה בהתאם
    ilan.wait_for_button("Moving ahead", debug)
    x = 42
    if port == 0:
        ilan.pid_gyro(x)

    elif port == 1:
        ilan.pid_gyro(x + 10)

    elif port == 2:
        ilan.pid_gyro(x + 16.5)
    
    #מסתובב אל המשימה
    ilan.turn(90, 150)

    #מוריד את הקיר קרוב לרצפה
    ilan.wait_for_button("Move wall down", debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 220)

    if port == 2:
        ilan.move_wall_to_point(0, 220)

    #נוסע אל המשימה
    ilan.wait_for_button("Drive to mission", debug)
    ilan.pid_gyro(11)

    wait(500)
    #מוריד את הקיר למטה, תופס את המכולה - קרוב, אמצע
    ilan.wait_for_button("Take conatainer", debug)
    if port == 2:
        ilan.move_wall_to_point(0, 0)

    #מוריד את הקיר למטה, תופס את המכולה - רחוק
    else:
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 0)

    #מעלה את הקיר למעלה - קרוב, אמצע
    ilan.wait_for_button("Move wall up", debug)
    if port == 2:
        ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)

    #מעלה את הקיר למעלה - רחוק
    else:
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y)

    #חוזר לאזור הבית
    wait(1000)
    ilan.pid_gyro(20, 200, False)
    wait(500)
    ilan.turn(90, 150)
    wait(100)
    ilan.pid_gyro(2000, 500)


"Testing Area"

# wing()
# prepare_go_trucks3()
# go_trucks3()
# green_airplane_and_Containers()
# ilan.say("hello. i'm ilan with a russian accent", 'ru', 1000)

# 01-02-2022
# wing()
#ilan.pid_gyro(20, 200)
#ilan.pid_follow_line(ilan.color_sensor_right, 40, 150, 1.3, True)

take_container_activate()
