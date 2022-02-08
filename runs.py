#!/usr/bin/env pybricks-micropython

from robot import *
# Write code here
ilan = Robot()

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
    wait(200)
    sw.reset()
    
    ilan.pid_gyro(25, 250)
    ilan.pid_follow_line(ilan.color_sensor_right, 50, 100, 1.3, True)
    #turn engine over
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_gyro(24, Forward_Is_True=False)
    
    # מוריד את המכולה מהמטוס
    #move to left
    ilan.wait_for_button("20. wall left",debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)

    #go right to center
    ilan.wait_for_button("50. wall down",debug)
    ilan.move_wall_to_point(0, 100)

    ilan.wait_for_button("60. wall up middle",debug)
    ilan.move_wall_to_point(0,  300)

    ilan.wait_for_button("70. wall right",debug)
    ilan.move_wall_to_point(500, 300)

    ilan.wait_for_button("80. wall up",debug)
    ilan.move_wall_to_point(500, ilan.WALL_MAX_ANGLE_Y)

    ilan.wait_for_button("90. wall left then down",debug)
    ilan.move_wall_to_point(80, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(80, 0)

    ilan.wait_for_button("100. up",debug)
    ilan.move_wall_to_point(0, 650)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700)
    ilan.turn(10,150)
    ilan.pid_gyro(10)
    ilan.turn(-15,150)
    #ilan.pid_gyro(5)
    ilan.wait_for_button("110. wall reset",debug)
    ilan.wait_for_button("120. wall 0,0",debug)
    #ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 180)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-550, 180)
    ilan.pid_gyro(8,Forward_Is_True=False)
    #ilan.pid_gyro(2,Forward_Is_True=False)
    #ilan.turn(-10,150)
    #ilan.pid_gyro(10, 100,Forward_Is_True=False)
    ilan.wait_for_button("125. Pause after left",False)
    
    
    
    ilan.beep()

    ilan.wait_for_button("130. wall up",debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.turn(70,250)
    ilan.pid_gyro(33, 500, Forward_Is_True=False)
    ilan.turn(80, 200)
    ilan.wait_for_button("140. wall reset right",debug)


def green_airplain_and_Containers_old():

    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    ilan.wait_for_button("10. start",True)
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
    debug = True
    ilan.reset_wall()
    ilan.wait_for_button("Wait For Start",  debug)

    # נסיעה על שהכנף נוגעת במתקן שלה
    watch = StopWatch()
    ilan.pid_gyro(72, 250, Kp = 3.05)
    ilan.pid_gyro(10, 120)

    # קיר זז ותופס תרנגולת
    ilan.move_wall_to_point(600, 0)

    #wait(1000)

    #מזיז את הקיר על מנת לא להיתקע בתרנגולת
    ilan.pid_gyro(21, 100, Forward_Is_True = False)
    ilan.move_wall_to_point(0, 100)

    # חזרה הביתה
    ilan.pid_gyro(10, 100, False)
    ilan.turn(5)
    ilan.pid_gyro(55, 500, False, 3.05) 
    # ilan.pid_gyro(3, 100, Forward_Is_True = False)
    

    # מדפיס את זמן ביצוע המשימה
    print("Mission time: " + str(watch.time() / 1000))
    return

def take_container_activate():

    #מאפס את הקיר לאמצע
    ilan.reset_wall()
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y)

    #מחכה להלבשת הזרוע
    ilan.wait_for_button("Place arm", False)
    ilan.write("Far | Center | Close")

    #בודק לאיזה מקום צריך להגיע - ימין, אמצע שמאל
    while True:
        # Wait until any Brick Button is pressed.ilan
        while not any(ilan.ev3.buttons.pressed()):
           wait(10)

        # Respond to the Brick Button press.
        
        if Button.RIGHT in ilan.ev3.buttons.pressed():
            ilan.write("Close Container")
            take_container(0)
            return

        elif Button.CENTER in ilan.ev3.buttons.pressed():
            ilan.write("Center Container")
            take_container(1)
            return

        elif Button.LEFT in ilan.ev3.buttons.pressed():
            ilan.write("Far Container")
            take_container(2)
            return

        
            
def take_container(port: int):
    debug = False

    #נוסע אל ועל הקו השחור
    ilan.pid_gyro(20)
    # ilan.pid_follow_right_line_until_left_detect_line(90, 3, 1.355, True)
    ilan.pid_follow_line(ilan.color_sensor_right, 98, 130, 1.355, True)
    wait(500)

    #בודק האם צריך להגיע למכולה ימין, אמצע או שמאל ונוסע קדימה בהתאם
    ilan.wait_for_button("Moving ahead", True)
    x = 42
    if port == 0:
        ilan.pid_gyro(x)
        ilan.write("Close Container")

    elif port == 1:
        ilan.pid_gyro(x + 7.5)
        ilan.write("Center Container")
        
    elif port == 2:
        ilan.pid_gyro(x + 16.5)
        ilan.write("Far Container")
    
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

def go_trucks2022_02_01():

    ilan.reset_wall() 
    #move wall to wait for truck holder
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -300, 350)
    ilan.wait_for_button("place truck", True)
    wait(200)
    init_gyro = ilan.gyro_sensor.angle()
    #gyro north
    ilan.pid_gyro(52, 300)
    current_gyro = ilan.gyro_sensor.angle()
    ilan.turn(101)
    #ilan.wait_for_button("Go east", True)
    #gyro east
    ilan.pid_gyro(32, 200)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -300, 50)
    ilan.pid_gyro(10, 100)
    #lower wall and release it 
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -300, 0)
    #move wall left to be clear of truck
    ilan.reset_wall()
    # go forward in order to catch front truck
    #ilan.pid_follow_line(ilan.color_sensor_right, 15, 150)
    ilan.pid_gyro(13, 200)
    # place wall behind cabing of front truck
    ilan.move_wall_to_point( 0, 300)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 300)
    # push to bridge
    ilan.turn(10)
    ilan.pid_gyro(15, 100)
    #ilan.pid_follow_line(ilan.color_sensor_right, 10, 150)
    ilan.wait_for_button("go to bridge", True)
    # lift wall to clear of trucks
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 400)
    # move to second part of bridge
    #ilan.pid_gyro(20, 200)
    ilan.pid_follow_line(ilan.color_sensor_right, 20, 150)
    # lift wall to pass second part of bridge
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    # move a bit forward to pass seconf part of bridge
    #ilan.pid_gyro(10, 200)
    ilan.pid_follow_line(ilan.color_sensor_right, 13, 150)
    #lower wall to catch bridge part 2
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 400)
    #go back to hit bridge part 2
    ilan.pid_gyro(-10, 200)
    ilan.wait_for_button("what's next?", True)
    ilan.pid_follow_line(ilan.color_sensor_right, 50, 150,Kp=1.7,Ki=0.02,Kd=0.08)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 350)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 350)
    ilan.pid_follow_line(ilan.color_sensor_right, 20, 150,Ki=0.06)
    #חוזר לאזור הבית
    # wait(1000)
    # ilan.pid_gyro(20, 200, False)
    # wait(500)
    # ilan.turn(90, 150)
    # wait(100)
    # ilan.pid_gyro(2000, 500)

def running ():
    ilan.write("Container L | Wing C | __ R")
    while True:

        # מחכה ללחיצת כפתור
        while not any(ilan.ev3.buttons.pressed()):
           wait(10)

        # מגיב ללחיצת כפתור
        
        # כפתור שמאלי - ראן לקיחת מכולות
        if Button.LEFT in ilan.ev3.buttons.pressed():
            ilan.write("Container Run")
            take_container_activate()

            return

        elif Button.CENTER in ilan.ev3.buttons.pressed():
            ilan.write("Wing Run")
            wing()

            return

        elif Button.RIGHT in ilan.ev3.buttons.pressed():
            ilan.write("No Run")
            
            # return

        



sw = StopWatch()

# ilan.pid_follow_line(ilan.color_sensor_right, 98, 130, 1.355, True)
ilan.reset_wall()
ilan.move_wall_to_point(500, 500)
ilan.pid_gyro(25, 150, True)
ilan.pid_follow_right_line_until_left_detect_line(50, 3, 1.3)
# green_airplane_and_Containers()
# green_airplain_and_Containers_old()
print("Run time[s] " + str(sw.time()/1000))

