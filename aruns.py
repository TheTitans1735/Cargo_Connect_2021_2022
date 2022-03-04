#!/usr/bin/env pybricks-micropython
from robot import *

ilan = Robot()
ilan.reset_wall_bottom_right()

def turbina_run_vino_arm():
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-200, ilan.WALL_MAX_ANGLE_Y-250)
    ilan.pid_gyro(36)
    ilan.pid_follow_line(20,100, ilan.color_sensor_right, white_is_right=True)
    ilan.pid_gyro(30)
    ilan.pid_follow_line(20,100, ilan.color_sensor_right, white_is_right=True)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-600, ilan.WALL_MAX_ANGLE_Y-250, x_wait=False)
    ilan.wall_y_motor.run_until_stalled(-1200,Stop.BRAKE, duty_limit=75)

    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X-400, 0)
def green_airplane_and_containers_WithPneumatic():
    my_debug = False
    wall_debug = False

    # איפוס הקיר וסידור ההלבשה
    ilan.wait_for_button("wall bottom right", wall_debug)
    ilan.reset_wall_bottom_right()
    
    ilan.wait_for_button("Place container", True)
    wait(50)

    # נסיעה אל הקו, הזזת הקיר
    ilan.wait_for_button("Drive to line + move wall", my_debug)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, 0, 25, 200)

    #  נסיעה למשימה עם החיישן הימני - עד זיהוי קו אחד עם החיישן השמאלי
    ilan.wait_for_button("Drive on the lin until detect line", my_debug)
    ilan.pid_follow_right_line_until_left_detect_color(1, ilan.color_sensor_right, ilan.color_sensor_left, 90+10, white_is_right = True, kp=1.3)

    # נסיעה קצרה לפנים
    ilan.pid_gyro(2, 80)  

    # הפיכת המנוע
    ilan.wait_for_button("Turn engine over", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2 - 100, x_wait = False, y_wait = True)

    # נסיעה לאחור והזזת הקיר למעלה
    ilan.wait_for_button("Drive backward, move wall up", wall_debug)
    ilan.pid_gyro(4, 80, False)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y - 300) # הפעלת המנגנון הפנאומטי, הפלת החלק הצהוב

    # נסיעה לאחור + הזזת קיר שמאלה ולמטה
    ilan.wait_for_button("Drive backwrd, move wall left & down", wall_debug)
    ilan.PID_while_move_wall(0, 0, 22, Forward_Is_True = False)

    # חוזר הביתה
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y-400)
    ilan.pid_gyro(30, 200, False)
    ilan.turn(-50)


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

####function changed 2022-04-03 
def go_trucks_before_2022_03_04_11_00_00():
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
    # 2022-03-04 rtm 2 new lines to offset gyro changes
    ilan.gyro_sensor.reset_angle(0)
    # init_gyro = ilan.gyro_sensor.angle()
    ilan.pid_gyro(55.6 -0.6, 150)
    # current_gyro = ilan.gyro_sensor.angle()

    # turn east
    # 2022-03-04 rtm new line to offset gyro changes
    ilan.turn(90 - ilan.gyro_sensor.angle(), 200)
    # ilan.turn(90, 200)
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
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X/2, ilan.WALL_MAX_ANGLE_Y/2, x_wait=False, y_wait=False) #שורה זו הוספה כדי להשתמש בזרוע של אורי
    ilan.pid_follow_line(17, 100, ilan.color_sensor_right)

    # lift wall to be able to pass second part of the bridge
    ilan.wait_for_button("Lift wall", wall_debug)
    # ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False) **** ירד כדי להתאים לזרוע של אורי

    # follow line past the second door
    ilan.wait_for_button("Go to second door", my_debug)
    # wait(300)
    ilan.pid_follow_line(15, 150, ilan.color_sensor_right, Kd = 0.085)
    ilan.pid_follow_right_line_until_left_detect_color(1,ilan.color_sensor_right, ilan.color_sensor_left, 100)
    
    
    #lower wall to catch bridge part 2
    ilan.wait_for_button("Push second door", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 400) *****
                                                            #הורדת קריאות אלו כדי להתאים לזרוע החדשה
    # #go back to hit bridge part 2
    # ilan.pid_gyro(10, 200, False) *****

    ## FINISH TRUCKS


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
    # 2022-03-04 rtm 2 new lines to offset gyro changes
    ilan.gyro_sensor.reset_angle(0)
    # init_gyro = ilan.gyro_sensor.angle()
    ilan.pid_gyro(55, 150)
    # current_gyro = ilan.gyro_sensor.angle()

    # turn east
    # 2022-03-04 rtm new line to offset gyro changes
    ilan.turn(88 - ilan.gyro_sensor.angle(), 200)
    # ilan.turn(90, 200)
    ilan.wait_for_button("ready for truck", wall_debug)
   

    # go east with gyro
    ilan.wait_for_button("Go east with gyro", my_debug)
    # ilan.pid_gyro(21 , 200) # +20 to compensate for going backwards
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X -350, 50, 30,200,0.5)


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
    ilan.pid_gyro(12, 200)

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
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X/2, ilan.WALL_MAX_ANGLE_Y/2, x_wait=False, y_wait=False) #שורה זו הוספה כדי להשתמש בזרוע של אורי
    ilan.pid_follow_line(17, 100, ilan.color_sensor_right)

    # lift wall to be able to pass second part of the bridge
    ilan.wait_for_button("Lift wall", wall_debug)
    # ilan.move_wall_to_point( ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False) **** ירד כדי להתאים לזרוע של אורי

    # follow line past the second door
    ilan.wait_for_button("Go to second door", my_debug)
    # wait(300)
    ilan.pid_follow_line(15, 150, ilan.color_sensor_right, Kd = 0.085)
    ilan.pid_follow_right_line_until_left_detect_color(1,ilan.color_sensor_right, ilan.color_sensor_left, 100)
    
    
    #lower wall to catch bridge part 2
    ilan.wait_for_button("Push second door", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 400) *****
                                                            #הורדת קריאות אלו כדי להתאים לזרוע החדשה
    # #go back to hit bridge part 2
    # ilan.pid_gyro(10, 200, False) *****

    ## FINISH TRUCKS

def take_containers_before_2022_03_04_11_16_00(close_or_far):
    "Close = True  |  Far  = False"
    my_debug = False
    wall_debug = False

    # Continues mission after trucks
    ilan.wait_for_button("Continue to Containers", my_debug)
    # 2022-02-11 - removed follow line and replaced by pid_gyro

    # check if robot needs to go to close / far containers
    ilan.wait_for_button("Go Close or Far", my_debug)
    cm_to_go_forward = 57 - 1 -10
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

    # ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, 22 - 1, 150, 0.5, Forward_Is_True = False)
    #2022-03-02 rotem move wall before driving to keep contaiers using wall
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    ilan.pid_gyro(5, 150, Forward_Is_True = False) # new code
    ilan.turn(90, 150) # new code
    ilan.pid_gyro(10, 150, Forward_Is_True = False) # new code

    ilan.pid_gyro(10, 150, Forward_Is_True = True) # new code
    ilan.turn(-90, 150) # new code

    ilan.pid_gyro(21 - 3 - 5, 150, Forward_Is_True = False)
    ilan.turn(90, 150)
    #2022-03-04 rtm changed 89 to 87 line below
    ilan.pid_gyro(87, 400)

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


def take_containers(close_or_far):
    "Close = True  |  Far  = False"
    my_debug = False
    wall_debug = False

    # Continues mission after trucks
    ilan.wait_for_button("Continue to Containers", my_debug)
    # 2022-02-11 - removed follow line and replaced by pid_gyro

    # check if robot needs to go to close / far containers
    ilan.wait_for_button("Go Close or Far", my_debug)
    cm_to_go_forward = 57 - 1 -10
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

    # ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y, 22 - 1, 150, 0.5, Forward_Is_True = False)
    #2022-03-02 rotem move wall before driving to keep contaiers using wall
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    # ilan.pid_gyro(5, 150, Forward_Is_True = False) # new code
    ilan.turn(90, 150) # new code
    ilan.pid_gyro(15, 150, Forward_Is_True = False) # new code

    ilan.pid_gyro(15, 150, Forward_Is_True = True) # new code
    ilan.turn(-90, 150) # new code

    ilan.pid_gyro(21 - 3, 150, Forward_Is_True = False)
    ilan.turn(90, 150)
    #2022-03-04 rtm changed 89 to 87 line below
    ilan.wait_for_button("Go home", True)
    ilan.pid_gyro(87, 400)

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
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y, x_wait=False)
    ilan.wait_for_button("PLACE ARM")
    # ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y - 200, 27, 150, wall_speed = -1500) # *** x was 0, y was max angle, 
    ilan.pid_gyro(27, 150)
    # follow the line to the mission (detect 2 lines) & turn to mission
    ilan.pid_follow_right_line_until_left_detect_color(2, ilan.color_sensor_right, ilan.color_sensor_left, 120, False)
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
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False)
    gyro_angle = ilan.gyro_sensor.angle()

    ilan.wait_for_button("Turn to mission", my_debug)
    ilan.turn(-90 - gyro_angle, 150)

    # move wall to place containers
    ilan.wait_for_button("place containers", my_debug)
    ilan.pid_gyro(5, 150, False) # new
    
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y - 200) # move wall right & down
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2 - 140) 
    # ilan.pid_gyro(1.6, 60, False)
    ilan.pid_gyro(6, 60, True) # new

    # clear arm of containers
    ilan.wait_for_button("Clear of containers", my_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y / 2 - 140, y_wait = False) # wall max left

    # drive backwards from mission
    ilan.wait_for_button("Drive Gyro backwards", my_debug)
    ilan.PID_while_move_wall(0, ilan.WALL_MAX_ANGLE_Y, 10 + 1.6 + 1, 150, Forward_Is_True = False) # + 1.6 + 1 new

    ilan.wait_for_button("Turn to parking mission", my_debug)
    ilan.turn(-47, 120)

    ilan.wait_for_button("Drive to parking mission", my_debug)
    ilan.pid_gyro(34.1, 250)
    ilan.beep()
    ilan.pid_gyro(6, 70)
    
    ilan.say("ishmi bili oten doten ba boba beten deten ah chen chef")
    ilan.ev3.speaker.play_file("kmo hatuna shel aravim magevet ba avir uh uh")


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
                turbina_run_vino_arm()
                # wing_run() # הפעלת הראן

                sum_time = sw.time() + sum_time
                # print("!!!TIMER --- Current, Sum!!!")
                # print(sw.time(), sum_time)
                ilan.write("!!! Timer !!! \n    Mission time: " + str(sw.time()) + " \n Total time: " + str(sum_time))

            elif Button.RIGHT in ilan.ev3.buttons.pressed():
                ilan.write("Green Airplane & Containers")
                sw.reset() # מאפס את שעון המשימה

                # green_airplane_and_Containers() # הפעלת הראן
                # green_airplane_and_containers()
                green_airplane_and_containers_WithPneumatic()

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

# ilan.pid_gyro(35,300,Forward_Is_True = False)
# ilan.wait_for_button("Go until line", True)
# ilan.drive_until_line(10,50,ilan.color_sensor_left, Color.BLACK, 2)
# ilan.wait_for_button("Turn to line", True)
# ilan.pid_gyro(4, 100)
# wait(100)
# ilan.turn(50)
# ilan.turn_until_black(ilan.color_sensor_left, True, 25)

# ilan.robot.straight(50000)
# green_airplane_and_containers_WithPneumatic()
# go_trucks_with_new_arm()
# ilan.learn_pid_line_values(ilan.color_sensor_right, 150, 120, "kp",kp=1.3, num_of_loops=1)
# ilan.move_wall_to_point(500,500)

# ilan.pid_follow_line(150, speed=150, line_sensor=ilan.color_sensor_right, Kp=1.393, Ki=0.038, white_is_right=True, Kd=0.072)  
# *******************ilan.pid_follow_line(150, speed=120, line_sensor=ilan.color_sensor_right, Kp=1.353, Ki=0.0352, white_is_right=True, Kd=0.062)  

# Kp=1.353, Ki=0.0352, Kd=0.062 pretty good - speed 120









# ilan.say("ze hajuk shehekpitz et hashpritz shel hamitlahatzitz al hashpitz shel hakfitz baharitz hamesukan behor hahar")