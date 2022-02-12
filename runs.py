#!/usr/bin/env pybricks-micropython

from robot import *
# Write code here
ilan = Robot()


def green_airplane_and_Containers():
    my_debug = False
    
    # אילן שם את המכולות בעיגול וחזר אחורה למטוס
    ilan.reset_wall_bottom_right()
    
    ilan.wait_for_button("10. start",True)
    wait(200)
    # sw.reset()
    
    ilan.pid_gyro(25, 600)
    ilan.pid_follow_right_line_until_left_detect_line(3, 120)
    ilan.pid_follow_line(ilan.color_sensor_right, 5, 80, 1.3, True)
    #turn engine over
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.pid_gyro(24, Forward_Is_True=False)
    
    # מוריד את המכולה מהמטוס
    #move to left
    ilan.wait_for_button("20. wall left",my_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y)

    #go right to center
    ilan.wait_for_button("50. wall down",my_debug)
    ilan.move_wall_to_point(0, 100)

    ilan.wait_for_button("60. wall up middle",my_debug)
    ilan.move_wall_to_point(0,  300)

    ilan.wait_for_button("70. wall right",my_debug)
    ilan.move_wall_to_point(500, 300)

    ilan.wait_for_button("80. wall up",my_debug)
    ilan.move_wall_to_point(500, ilan.WALL_MAX_ANGLE_Y)

    ilan.wait_for_button("90. wall left then down",my_debug)
    ilan.move_wall_to_point(80, ilan.WALL_MAX_ANGLE_Y)
    ilan.move_wall_to_point(80, 0)

    ilan.wait_for_button("100. up",my_debug)
    ilan.move_wall_to_point(0, 650)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700)
    ilan.turn(10,150)
    ilan.pid_gyro(10)
    ilan.turn(-15,150)
    #ilan.pid_gyro(5)
    ilan.wait_for_button("110. wall reset",my_debug)
    ilan.wait_for_button("120. wall 0,0",my_debug)
    #ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 180)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-550, 180)
    ilan.pid_gyro(8,Forward_Is_True=False)
    #ilan.pid_gyro(2,Forward_Is_True=False)
    #ilan.turn(-10,150)
    #ilan.pid_gyro(10, 100,Forward_Is_True=False)
    ilan.wait_for_button("125. Pause after left",False)
    
    
    
    ilan.beep()

    ilan.wait_for_button("130. wall up",my_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)
    ilan.turn(70,250)
    ilan.pid_gyro(33, 500, Forward_Is_True=False)
    ilan.turn(80, 200)
    ilan.wait_for_button("140. wall reset right",my_debug)


def wing_run():
    my_debug = True
    ilan.reset_wall()
    ilan.wait_for_button("Wait For Start",  my_debug)

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
        

def go_trucks():
    ilan.gyro_sensor.reset_angle(0)
    ilan.reset_wall() 
    my_debug = False

    #move wall to wait for truck holder
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 350)
    ilan.wait_for_button("place truck", True)
    wait(200)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -350, 350)
    init_gyro = ilan.gyro_sensor.angle()

    #gyro north
    ilan.wait_for_button("Go north with gyro", my_debug)
    ilan.pid_gyro(55, 100)
    current_gyro = ilan.gyro_sensor.angle()
    ilan.turn(90)
    #ilan.wait_for_button("Go east", True)

    #gyro east
    ilan.wait_for_button("Go east with gyro", my_debug)
    ilan.pid_gyro(32, 200)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -350, 50)
    ilan.pid_gyro(10, 100)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 50)

    #lower wall and release it 
    ilan.wait_for_button("Release truck", my_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 0)

    #move wall left to be clear of truck
    ilan.wait_for_button("Clear of truck", my_debug)
    ilan.reset_wall()
    
    # go forward in order to catch front truck
    ilan.wait_for_button("Catch front truck", True)
    # ilan.pid_gyro(13, 200) ***
    ilan.pid_gyro(2, 100) 
    ilan.pid_follow_line_2022_02_08(11, 150, ilan.color_sensor_right, Kp=1.25, Kd = 0.089) 

    # place wall behind cabing of front truck
    ilan.move_wall_to_point( 0, 350)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 350)

    # push to bridge
    ilan.wait_for_button("Take truck to bridge", my_debug)
    ilan.turn(3)
    # ilan.pid_gyro(15, 100) *** 
    ilan.pid_follow_line_2022_02_08(17, 150, ilan.color_sensor_right, Kd = 0.089)
    
    # lift wall to clear of trucks
    ilan.wait_for_button("Clear of trucks", my_debug)
    ilan.beep()
    ilan.pid_gyro(2, Forward_Is_True = False)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 200, 300)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 200, 450)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 450)

    # knock down first door and move onto the other
    ilan.wait_for_button("Knock down first door", my_debug)
    # ilan.pid_gyro(14) ***

    ilan.pid_follow_line_2022_02_08(19, 150, ilan.color_sensor_right, Kd = 0.085)

    # go back to the line
    ilan.wait_for_button("Go back to line", my_debug)
    # ilan.turn(-3) ***
    # ilan.pid_gyro(2, 100) ***
    # ilan.turn(4) ***

    # follow line to the second door
    ilan.wait_for_button("Go to second door", my_debug)
    ilan.pid_follow_line_2022_02_08(11, 150, ilan.color_sensor_right, Kd = 0.085)

    # lift wall to pass second part of bridge
    ilan.wait_for_button("Pass second door", my_debug)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    # move a bit forward to pass second part of bridge
    ilan.pid_follow_line_2022_02_08(8, 150, ilan.color_sensor_right)

    #lower wall to catch bridge part 2
    ilan.wait_for_button("Push second door", my_debug)
    ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, 400)

    #go back to hit bridge part 2
    ilan.pid_gyro(10, 200,False)

    ## FINISH TRUCKS


def take_containers(close_or_far):
    "Close = True  |  Far  = False"
    my_debug = False

    # Continues mission after trucks
    #ilan.wait_for_button("Prepare wall", False)
    # ilan.reset_wall()
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-100,150)
    ilan.wait_for_button("Continue to Containers", my_debug)
    # 2022-02-11 - removed follow line and replaced by pid_gyro
    #ilan.pid_follow_right_line_until_left_detect_line(1)

    # check if robot needs to go to close / far containers
    ilan.wait_for_button("Go Close or Far", my_debug)
    cm_to_go_forward = 52 + 3
    ilan.pid_gyro(cm_to_go_forward)

    # Turn & drive to mission
    ilan.wait_for_button("Turn to mission", my_debug)
    ilan.turn(90 - ilan.gyro_sensor.angle()) # turn depending on current angle (error)
    
    # Move wall to containers depending on close / far
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)

    else:
        ilan.move_wall_to_point(0, 0)
    
    ilan.pid_gyro(8, 80)
    ilan.pid_gyro(8, 50)

    # Move wall up depending on close / far
    ilan.wait_for_button("Take containers", my_debug)
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700)

    else:
        ilan.move_wall_to_point(0, 700)

    # Go home
    ilan.wait_for_button("Go Home", my_debug)
    ilan.pid_gyro(22, 150, Forward_Is_True = False)
    ilan.turn(90)
    ilan.pid_gyro(89, 400)

    # Turn left to avoid airplane mission
    ilan.turn(-25, 200)
    ilan.pid_gyro(30, 400)
    
    # Go back right, catch blue
    ilan.turn(650, 150)
    ilan.pid_gyro(35, 300)

    # Go back home with container
    ilan.turn(-40, 400)
    ilan.pid_gyro(20, 400)


def east_run(close_or_far):
    "Close = True  |  Far = False"
    my_debug = False
    
    ### FIRST PART ###
    go_trucks()

    ### SECOND PART ###
    ilan.wait_for_button("Second Part", my_debug)
    take_containers(close_or_far)


    # ilan.pid_follow_line_2022_02_08(50, 150, ilan.color_sensor_right) #Kp=1.7, Ki=0.02, Kd=0.08
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, 350)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 350)
    # ilan.pid_follow_line_2022_02_08(20, 150, ilan.color_sensor_right) #Ki=0.06


def running ():
    ilan.write("Choose Run: \n wing_run L \n Green AP R \n East run close D \n East run far U")
    while True:

        # מחכה ללחיצת כפתור
        while not any(ilan.ev3.buttons.pressed()):
           wait(10)

        # מגיב ללחיצת כפתור
        
        # כפתור שמאלי - ראן לקיחת מכולות
        if Button.LEFT in ilan.ev3.buttons.pressed():
            ilan.write("wing Run")
            wing_run()

            return

        elif Button.RIGHT in ilan.ev3.buttons.pressed():
            ilan.write("Green Airplane & Containers")
            green_airplane_and_Containers()

            return

        elif Button.DOWN in ilan.ev3.buttons.pressed():
            ilan.write("East run close")
            east_run(True)

            return

        elif Button.UP in ilan.ev3.buttons.pressed():
            ilan.write("East run far")
            east_run(False)

            return


# Start run's stopwatch
sw = StopWatch()

# Activate all runs program
running()

# Print run's time
print("Run time is: " + str(sw.time()))
