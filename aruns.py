#!/usr/bin/env pybricks-micropython
from robot import *

ilan = Robot()
ilan.reset_wall_bottom_right()
      

def green_airplane_and_Containers():
    my_debug = False
    wall_debug = False

    # איפוס הקיר וסידור ההלבשה
    ilan.wait_for_button("wall bottom right", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0) # -100 קוד חדש ***
    
    ilan.wait_for_button("Place container", True)
    wait(200)
    
    # ilan.pid_gyro(25, 200)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, 0, 25, 200)

    # נסיעה למשימה - עד זיהוי קו אחד
    ilan.pid_follow_right_line_until_left_detect_color(1, 100)
    ilan.pid_follow_line(2, 80, ilan.color_sensor_right, Kp=1.3, white_is_right = True)

    # הפיכת המנוע
    ilan.wait_for_button("turn engine over", wall_debug)
    #נסיעה חזרה לאחור + קיר
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, ilan.WALL_MAX_ANGLE_Y - 50, 10, Forward_Is_True = False)

    # חדש - פנייה ימינה על מנת להשיג זווית ***
    ilan.turn(15, 150)

    # נסיעה אחורה
    ilan.pid_gyro(15, 150, False)

    # פנייה לתפיסת המטוס, נסיעה לפנים
    ilan.turn(-15, 150)
    # ilan.pid_gyro(5, 150)

     
    ### הורדת המכולה מהמטוס - שלב 1 ###
    # שמאלה
    ilan.wait_for_button("1 go left & up", True)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y, -1500)

    # למטה
    ilan.wait_for_button("2 down", wall_debug)
    ilan.move_wall_to_point(0, 100, -1500)

    # למעלה
    ilan.wait_for_button("3 little up", wall_debug)
    ilan.move_wall_to_point(0,  300, -1500)

    # ימינה
    ilan.wait_for_button("4 right", wall_debug)
    ilan.move_wall_to_point(500, 300, -1500, x_wait = False, y_wait = False)

    # למעלה עד הסוף
    ilan.wait_for_button("5 right & full up", False)
    ilan.move_wall_to_point(500, ilan.WALL_MAX_ANGLE_Y, -1500, x_wait = False) ## new code *****

    ### הורדת המכולה מהמטוס - שלב 2 ###
    # שמאלה, למטה
    ilan.wait_for_button("6 left", wall_debug)
    ilan.move_wall_to_point(80, ilan.WALL_MAX_ANGLE_Y, -1500)

    ilan.wait_for_button("7 down", wall_debug)
    ilan.move_wall_to_point(80, 0, -1500)

    # ימינה + למעלה
    ilan.wait_for_button("8 right and up", wall_debug)
    ilan.move_wall_to_point(80, 700 - 100, -1500)

    # הסתובב
    ilan.wait_for_button("9 turn to take container", my_debug)
    ilan.turn(10 , 150) # + 3 קוד חדש
    ilan.pid_gyro(10)
    ilan.turn(-15, 150)
    
    ilan.wait_for_button("10 left & down", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-550, 180, x_wait = False, y_wait = False)
    wait(500)
    ilan.wait_for_button("11 go back", wall_debug)
    ilan.pid_gyro(8,Forward_Is_True = False)
    
    ilan.beep()

    ilan.wait_for_button("12 go right & up", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 550, ilan.WALL_MAX_ANGLE_Y / 2, x_wait=False, y_wait= False)

    ilan.wait_for_button("turn right", my_debug)
    ilan.turn(70,250)

    ilan.wait_for_button("go home", my_debug)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y - 200, 33, 500, Forward_Is_True = False)

    ilan.wait_for_button("turn into base", my_debug)
    ilan.turn(80, 200)
    # ilan.wait_for_button("140. wall reset right",my_debug)


def green_airplane_2022_02_21():
    my_debug = False
    wall_debug = False

    # איפוס הקיר וסידור ההלבשה
    ilan.wait_for_button("wall bottom right", wall_debug)
    ilan.reset_wall_bottom_right()
    
    ilan.wait_for_button("Place container", True)
    wait(200)

    # נסיעה אל הקו, הזזת הקיר
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, 0, 25, 200)

    # נסיעה למשימה - עד זיהוי קו אחד
    ilan.pid_follow_right_line_until_left_detect_color(1, 90 + 10, white_is_right = True)
    # ilan.pid_follow_line(2, 80, ilan.color_sensor_right, Kp=1.3, white_is_right = True) ***
    ilan.pid_gyro(2, 80)

    # הפיכת המנוע ונסיעה לאחור
    ilan.wait_for_button("turn engine over", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y - 50, x_wait = False, y_wait = False)

    ilan.pid_gyro(5, Forward_Is_True = False)
    
    # Z Combination!
    ilan.turn(15)
    ilan.pid_gyro(5, 80, False)

    ilan.turn(-15)
    ilan.pid_gyro(15 + 2, 80, False)

    ### הורדת המכולה מהמטוס - שלב 1 ###
    # שמאלה
    ilan.wait_for_button("1 - go left & up", wall_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y, -1500, False, False)

    # למטה
    ilan.wait_for_button("2 - down", wall_debug)
    ilan.move_wall_to_point(0, 100, -1500)

    # למעלה
    ilan.wait_for_button("3 - up", wall_debug)
    ilan.move_wall_to_point(0,  300, -1500)

    # ימינה
    ilan.wait_for_button("4 - right", wall_debug)
    # ilan.move_wall_to_point(500, 300, -1500)

    # למעלה עד הסוף
    ilan.wait_for_button("5 - full up", wall_debug)
    ilan.move_wall_to_point(500, ilan.WALL_MAX_ANGLE_Y, -1500, x_wait = False) ## new code *****


    ### הורדת המכולה מהמטוס - שלב 2 ###
    # שמאלה, למטה
    ilan.wait_for_button("6 - left", wall_debug)
    ilan.move_wall_to_point(80, ilan.WALL_MAX_ANGLE_Y, -1500)

    ilan.wait_for_button("7 - down", wall_debug)
    ilan.move_wall_to_point(80, 0, -1500)

    # למעלה
    ilan.wait_for_button("8 - up", wall_debug)
    # ilan.move_wall_to_point(0, 650, -1500) *****

    # ימינה + למעלה
    ilan.wait_for_button("9 - right and up", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700 - 100, -1500,x_wait=False)

    # הסתובב על מנת לקחת את המכולה
    ilan.wait_for_button("10 - turn to take container", my_debug)
    ilan.turn(10, 150) # פנייה ימינה
    ilan.pid_gyro(12 + 3) # נסיעה לאחור
    ilan.turn(-15 + 5, 150) # פנייה שמאלה

    ilan.wait_for_button("down", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 180)

    ilan.wait_for_button("left & down", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 550, 180, x_wait = False, y_wait = False)

    ilan.move_wall_to_point(200 - 70, 180 - 20, x_wait = True, y_wait = True)

    ilan.wait_for_button("go back",  my_debug)
    ilan.pid_gyro(7 + 4, Forward_Is_True = False)

    ilan.beep()

    ilan.wait_for_button("go right & up", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 550, ilan.WALL_MAX_ANGLE_Y / 2, x_wait = False, y_wait = False)

    ilan.wait_for_button("turn right", my_debug)
    ilan.turn(60, 250)

    ilan.wait_for_button("go home", my_debug)
    ilan.PID_while_move_wall(0, ilan.WALL_MAX_ANGLE_Y - 200, 28, 500, Forward_Is_True = False)

    ilan.wait_for_button("turn into base", my_debug)
    # ilan.turn(80, 400)
    ilan.turn_until_seconds(1, 80, 400)


def wing_run():
    my_debug = False
    wall_debug = False
    ilan.reset_wall()
    ilan.wait_for_button("Wait For Start",  my_debug)

    # נסיעה על שהכנף נוגעת במתקן שלה
    watch = StopWatch()
    ilan.pid_gyro(72, 350, Kp = 3.05)
    ilan.pid_gyro(10, 180)

    # קיר זז ותופס תרנגולת
    ilan.move_wall_to_point(600, 0)

    #wait(1000)

    #מזיז את הקיר על מנת לא להיתקע בתרנגולת
    ilan.pid_gyro(21, 100, Forward_Is_True = False)
    ilan.wait_for_button("careful of chicken!", wall_debug)
    ilan.move_wall_to_point(0, 100)

    # חזרה הביתה
    ilan.pid_gyro(10, 400, False)
    ilan.turn(5, 200)
    # ilan.pid_gyro(55, 500, False, 3.05) 
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 100, 0, 55, 500, Forward_Is_True = False, Kp = 3.05)
    # ilan.pid_gyro(3, 100, Forward_Is_True = False)
    

    # מדפיס את זמן ביצוע המשימה
    print("Mission time: " + str(watch.time() / 1000))
    return


def go_trucks():
    ilan.gyro_sensor.reset_angle(0)
    # ilan.reset_wall() 
    my_debug = False
    wall_debug = False

    #move wall to wait for truck holder
    ilan.wait_for_button("move wall for mission", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -350, 550)

    ilan.wait_for_button("place truck", True)
    init_gyro = ilan.gyro_sensor.angle()

    # go north with gyro
    ilan.wait_for_button("Go north with gyro", my_debug)
    ilan.pid_gyro(55.6 -0.6, 150)
    current_gyro = ilan.gyro_sensor.angle()

    # turn east
    ilan.turn(90, 200)
    ilan.wait_for_button("ready for truck", wall_debug)
   

    # go east with gyro
    ilan.wait_for_button("Go east with gyro", my_debug)
    # ilan.pid_gyro(21 , 200) # +20 to compensate for going backwards
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X -350, 50, 31,200,0.5)


    ilan.wait_for_button("Move wall for trucks", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -350, 50) # move wall down
    # ilan.pid_gyro(10, 100)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 50) # move wall right

    # lower wall and release it 
    ilan.wait_for_button("Release truck", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 0)

    # move wall left to be clear of truck
    ilan.wait_for_button("Clear of truck", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2 - 100, 0)
    
    # go forward in order to catch front truck
    ilan.wait_for_button("Catch front truck", my_debug)
    ilan.pid_gyro(11, 200)

    # place wall behind cabing of front truck
    ilan.wait_for_button("UP - wall to front truck", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2 - 100, 350)
    ilan.wait_for_button("RIGHT - wall to front truck", wall_debug)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 350, x_wait = False)

    # push to bridge
    ilan.wait_for_button("Take truck to bridge", my_debug)
    ilan.turn(3)
    ilan.pid_gyro(15, 100)
    
    # lift wall to clear of trucks
    ilan.wait_for_button("Clear of trucks", wall_debug)
    ilan.beep()
    ilan.pid_gyro(2, Forward_Is_True = False)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 200, 300)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 200, 450)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 450, x_wait = False, y_wait = False)

    # go back to the line
    ilan.wait_for_button("Go back to line", my_debug)
    ilan.gyro_sensor.reset_angle(0)

    while ilan.color_sensor_right.reflection() > 40:
        ilan.right_motor.run(25)
        ilan.left_motor.run(-25)

    ilan.left_motor.brake()
    ilan.right_motor.brake()

    # TO DO !!!
    # knock down first door and move onto the other
    ilan.wait_for_button("Knock down first door", my_debug)
    ilan.pid_follow_line(17, 100, ilan.color_sensor_right)

    # lift wall to be able to pass second part of the bridge
    ilan.wait_for_button("Lift wall", wall_debug)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False) 

    # follow line past the second door
    ilan.wait_for_button("Go to second door", my_debug)
    # wait(300)
    ilan.pid_follow_line(19 - 1, 150, ilan.color_sensor_right, Kd = 0.085)
    # ilan.pid_follow_right_line_until_left_detect_color(1,100)
    

    #lower wall to catch bridge part 2
    ilan.wait_for_button("Push second door", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 400)

    #go back to hit bridge part 2
    ilan.pid_gyro(10, 200, False)

    ## FINISH TRUCKS


def take_containers(close_or_far):
    "Close = True  |  Far  = False"
    my_debug = False
    wall_debug = False

    # Continues mission after trucks
    ilan.wait_for_button("Continue to Containers", my_debug)
    # 2022-02-11 - removed follow line and replaced by pid_gyro

    # check if robot needs to go to close / far containers
    ilan.wait_for_button("Go Close or Far", my_debug)
    cm_to_go_forward = 57 - 1
    ilan.pid_gyro(cm_to_go_forward, 200)

    # Turn & drive to mission
    ilan.wait_for_button("Turn to mission", my_debug)
    ilan.turn(90 - ilan.gyro_sensor.angle(), 200) # turn depending on current angle (error)
    
    # Move wall to containers depending on close / far
    ilan.wait_for_button("Move wall to containers", wall_debug)
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
        # ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X, 0, 8,45)

    else:
        ilan.move_wall_to_point(0, 0)
        # ilan.PID_while_move_wall(0,0,8,80)
    ilan.pid_gyro(8, 80)
    
    ilan.pid_gyro(8 - 1.5, 50)
    ilan.wait_for_button("Knock down rail", my_debug)
    
    # Move wall up depending on close / far
    ilan.wait_for_button("Take containers", wall_debug)
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700)

    else:
        ilan.move_wall_to_point(0 + 50, 700)

    # Go home
    ilan.wait_for_button("Go Home", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 700)
    # ilan.pid_gyro(22, 150, Forward_Is_True = False)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, 22 - 1, 150, 0.5, Forward_Is_True = False)
    ilan.turn(90, 150)
    ilan.pid_gyro(89, 400)

    # Turn left to avoid airplane mission
    ilan.turn(-30, 200)
    ilan.pid_gyro(30, 400)
    
    # Go back right, catch blue
    ilan.turn(57, 150)
    ilan.pid_gyro(50, 500)

    # ilan.turn(-90, 400)
    ilan.turn_until_seconds(0.7, 70, 400, False)                      
    wait(1000)
    ilan.move_wall_to_point(0, 0, x_wait = False, y_wait = False)
    

def east_run(close_or_far):
    "Close = True  |  Far = False"
    my_debug = False
    
    ### FIRST PART ###
    go_trucks()

    ### SECOND PART ###
    ilan.wait_for_button("Second Part", my_debug)
    take_containers(close_or_far)


def crane_run():
    my_debug  = False
    
    # Let's Go Ilan !!
    ilan.wait_for_button("Start run", False)

    # drive to the line, move the wall in case last run didn't
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y - 200, 27, 150, wall_speed = -1500) # *** x was 0, y was max angle, 

    # follow the line to the mission (detect 2 lines) & turn to mission
    ilan.pid_follow_right_line_until_left_detect_color(2, 120, False    )
    ilan.turn(-90, 180)

    # turn to line
    ilan.wait_for_button("Turn to line", False)
    wait(50)
    while ilan.color_sensor_right.reflection() > 40:
        ilan.right_motor.run(25)
        ilan.left_motor.run(-25)
    ilan.right_motor.brake()
    ilan.left_motor.brake()

    wait(50)

    # follow the line & drive to get closer to mission
    ilan.wait_for_button("Follow line & gyro to mission", my_debug)
    ilan.pid_follow_line(12, 90, ilan.color_sensor_right, white_is_right = True) 
    ilan.pid_gyro(12, 150)

    # turn to crane
    ilan.wait_for_button("Turn to crane", my_debug)
    ilan.turn(90, 170)

    # move to crane
    ilan.wait_for_button("Go to crane", my_debug)
    wait(50)

    # turn to the line
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y - 200, x_wait = False, y_wait = False) # new movement
    while ilan.color_sensor_right.reflection() > 40:
        ilan.right_motor.run(25)
        ilan.left_motor.run(-25)

    ilan.right_motor.stop()
    ilan.left_motor.stop()    

    # follow the line,  push the crane
    ilan.pid_follow_line(20, 100, ilan.color_sensor_right, white_is_right = True)

    # straighten on black line
    ilan.gyro_sensor.reset_angle(0)
    ilan.wait_for_button("Go back until black line", my_debug)
    while ilan.color_sensor_left.reflection() > 8:
        ilan.robot.drive(-80, ilan.gyro_sensor.angle()*-1)
    ilan.robot.stop()
    
    wait(100)

    # turn to containers mission
    gyro_angle = ilan.gyro_sensor.angle()

    ilan.wait_for_button("Turn to mission", my_debug)
    ilan.turn(-90 - gyro_angle, 150)

    # move wall to place containers
    ilan.wait_for_button("place containers", my_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y - 200) # move wall right & down
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2 - 140) 
    ilan.pid_gyro(1.6, 60, False)

    # clear arm of containers
    ilan.wait_for_button("Clear of containers", my_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y / 2 - 140, y_wait = False) # wall max left

    # drive backwards from mission
    ilan.wait_for_button("Drive Gyro backwards", my_debug)
    ilan.PID_while_move_wall(0, ilan.WALL_MAX_ANGLE_Y, 10, 150, Forward_Is_True = False)

    ilan.wait_for_button("Turn to parking mission", my_debug)
    ilan.turn(-45, 120)

    ilan.wait_for_button("Drive to parking mission", my_debug)
    ilan.pid_gyro(37.1, 250)
    
    ilan.say("I did it")


TEXT_MENU = """Choose Run: 
  < - Wing run 
  > - Green AP 
  O - Crane run 
  V - East run close 
  ^ - East run far"""

def running ():
    """!! One Function To Rule Them All !!"""

    # יוצר את שעוני העצר
    sw = StopWatch() # שעון לכל משימה
    sum_time = 0 # זמן כולל
    
    while True:
        
        try:
            # מדפיס את טקסט הריצות על הרובוט ועל מסך המחשב
            ilan.write(TEXT_MENU)

            # מחכה ללחיצת כפתור
            while not any(ilan.ev3.buttons.pressed()):
                wait(60)
            
            # כפתור שמאלי - ראן לקיחת מכולות
            if Button.LEFT in ilan.ev3.buttons.pressed():
                ilan.write("wing Run")
                sw.reset() # מאפס את שעון המשימה
                
                wing_run() # הפעלת הראן

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(sw.time(), sum_time)
                ilan.write("!!! Timer !!! \n    Mission time: " + str(sw.time()) + " \n Total time: " + str(sum_time))

            elif Button.RIGHT in ilan.ev3.buttons.pressed():
                ilan.write("Green Airplane & Containers")
                sw.reset() # מאפס את שעון המשימה

                # green_airplane_and_Containers() # הפעלת הראן
                green_airplane_2022_02_21()

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(sw.time(), sum_time)
                ilan.write("!!! Timer !!! \n    Mission time: " + str(sw.time()) + " \n Total time: " + str(sum_time))

            elif Button.DOWN in ilan.ev3.buttons.pressed():
                ilan.write("East run close")
                sw.reset() # מאפס את שעון המשימה

                east_run(True) # הפעלת הראן (מכולות קרובות)

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(str(sw.time()) + " , " + str(sum_time))
                ilan.write("!!! Timer !!! \n    Mission time: " + str(sw.time()) + " \n Total time: " + str(sum_time))


            elif Button.UP in ilan.ev3.buttons.pressed():
                ilan.write("East run far")
                sw.reset() # מאפס את שעון המשימה

                east_run(False) # הפעלת הרא (מכולות רחוקות)

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(sw.time(), sum_time)
                ilan.write("!!! Timer !!! \n    Mission time: " + str(sw.time()) + " \n Total time: " + str(sum_time))


            elif Button.CENTER in ilan.ev3.buttons.pressed():
                ilan.write("Crane run")
                sw.reset() # מאפס את שעון המשימה

                crane_run() # הפעלת הראן

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(sw.time(), sum_time)

        except Exception as ex:
            print("Error: {}".format(ex))
            wait(2500)

running()
# ilan.turn_until_seconds(2, 80, 400)

# ilan.beep()
# wait(2000)

# ilan.turn_until_seconds(2, 80, 400, False)