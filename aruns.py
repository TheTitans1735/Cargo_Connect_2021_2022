#!/usr/bin/env pybricks-micropython
from robot import *

ilan = Robot()
ilan.reset_wall_bottom_right()
ilan.beep()


##### East run - Combo of Go trucks & Take containers #####

def east_run(close_or_far):
    """ Close = True | Far = False """
    """ Trucks | Bridge | Innovation Project | Green Yellow Blue Containers | Rail """
    my_debug = False
    
    ### FIRST PART ###
    go_trucks()

    ### SECOND PART ###
    ilan.wait_for_button("Second Part", my_debug)
    take_containers(close_or_far)



##### Go Trucks #####

def go_trucks():
    """ Trucks | Bridge | Innovation Project"""

    my_debug = False
    wall_debug = False

    # הזזת הקיר למקום הנחוץ בשביל המשימה
    ilan.wait_for_button("Move wall for mission", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -350, 550)

    # המתנה לכפתור - הוספת הלבשת המשאיות
    ilan.wait_for_button("place truck", True)

    # נסיעה צפונה
    ilan.wait_for_button("Go north with gyro", my_debug)
    ilan.pid_gyro(55, 150)

    # פנייה מזרחה
    ilan.wait_for_button("Turn east", my_debug)
    ilan.turn(90 - ilan.gyro_sensor.angle(), 200)

    ## שרשור המשאיות ##
    # נסיעה מזרחה בזמן הזזת הקיר - הורדה לקראת שרשור המשאיות
    ilan.wait_for_button("Go east with gyro", my_debug)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 350, 50, 31, 200, 0.5)

    # הזזת הקיר לימין - וידוא שרשור המשאיות 
    ilan.wait_for_button("Move wall for trucks", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 50)

    # הזזת הקיר מטה - שחרור הלבשת המשאית
    ilan.wait_for_button("Release truck arm", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X -250, 0)

    # הזזת הקיר שמאלה - שלא להתנגש בהלבשה שנפלה
    ilan.wait_for_button("Clear of truck", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2 - 100, 0)
    
    ## משאית קדמית אל הגשר ##
    # נסיעה לפנים
    ilan.wait_for_button("Catch front truck", my_debug)
    # ilan.pid_gyro(11, 200)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X / 2 - 100, 350, 11, 200, 1) # חדש - נסיעה במהלך הזזת הקיר

    # # place wall behind cabing of front truck
    # ilan.wait_for_button("UP - Wall to front truck", wall_debug)
    # ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2 - 100, 350)

    # הזזת הקיר ימינה - תפיסת המשאית
    ilan.wait_for_button("RIGHT - Wall to front truck", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 350, x_wait = False)

    # דחיפת המשאית אל הגשר בזווית קלה
    ilan.wait_for_button("Take truck to bridge", my_debug)
    ilan.turn(3)
    ilan.pid_gyro(15, 100)
    
    ## שחרור המשאית הקדמית ##
    # נסיעה קצרה לאחור
    ilan.wait_for_button("Clear of trucks", wall_debug)
    ilan.beep()
    ilan.pid_gyro(2, Forward_Is_True = False)

    # הרמת הקיר מעל המשאית הקדמית
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2, x_wait = False, y_wait = False)

    ## הפלת דלת הגשר הראשונה ##
    # פנייה אל הקו השחור
    ilan.wait_for_button("Turn to line", my_debug)

    # while ilan.color_sensor_right.reflection() > 40:
    #     ilan.right_motor.run(25)
    #     ilan.left_motor.run(-25)

    # ilan.left_motor.brake()
    # ilan.right_motor.brake()
    ilan.turn_to_threshold(ilan.color_sensor_right, False, 25)

    # הזזת הקיר שמאלה תוך כדי נסיעה על הקו - הפלת הגשר הראשון
    ilan.wait_for_button("Knock down first door", my_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y / 2, x_wait = False, y_wait = False)
    ilan.pid_follow_line(17, 100, ilan.color_sensor_right)

    ## הפלת דלת הגשר השנייה ##
    # נסיעה על הקו השחור לפנים
    ilan.wait_for_button("Go to second door", my_debug)
    ilan.pid_follow_line(15, 150, ilan.color_sensor_right, Kd = 0.085)

    # נסיעה על הקו השחור עד זיהוי קו שחור עם החיישן השמאלי
    ilan.pid_follow_line_until_other_detect_color(1, ilan.color_sensor_right, ilan.color_sensor_left, 100)

    ### סיום חלק 1 של ראן המזרח ###



##### Take Containers #####

def take_containers(close_or_far):
    """ Green Yellow Blue Containers | Rail """
    """ Close = True | Far = False """

    my_debug = False
    wall_debug = False

    ### תחילת חלק 2 של ראן המזרח ###
    ilan.wait_for_button("Continue to Containers", my_debug)

    ## נסיעה אל המשימה ##
    # נסיעה מזרחה
    if close_or_far:
        ilan.pid_gyro(44, 200)

    else:
        ilan.pid_gyro(44 + 1, 200) # new

    # פנייה דרומה לכיוון המשימה
    ilan.wait_for_button("Turn to mission", my_debug)
    ilan.turn(90 - ilan.gyro_sensor.angle(), 200) # פנייה בהתאם לזווית הג'יירו הנוכחית
    
    # הזזת הקיר לימין או לשמאל בהתאם לזוג המכולות שרוצים לקחת
    ilan.wait_for_button("Move wall to containers", wall_debug)
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 0)

    else:
        ilan.move_wall_to_point(0, 0)

    # התקרבות אל המשימה
    ilan.wait_for_button("Get closer to mission", my_debug)
    ilan.pid_gyro(8, 80)
    
    ## לקיחת המכולות ##
    # נסיעה לפנים - ההלבשה תופסת את המכולות
    ilan.wait_for_button("Catch containers", my_debug)
    ilan.pid_gyro(6.5, 50)
    
    # הזזת הקיר למעלה - הרמת המכולות
    ilan.wait_for_button("Take containers", wall_debug)
    if (close_or_far):
        ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 700)

    else:
        ilan.move_wall_to_point(50, 700)

    ## הפלת המסילה ##
    # הזזת הקיר למעלה 
    # (וימינה אם המכולות היו משמאל לרובוט)
    ilan.wait_for_button("Move wall full up", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y)

    # פנייה ימינה, הפניית החלק האחורי של הרובוט אל המסילה
    ilan.wait_for_button("Turn for mission", my_debug)
    ilan.turn(90, 150)

    # נסיעה לאחור, ההלבשה עוברת את המסילה וננעלת
    ilan.wait_for_button("Drive backward, pass rail with arm", my_debug)
    ilan.pid_gyro(18, 150, Forward_Is_True = False)
    # נסיעה לפנים, הפלת המסילה
    ilan.pid_gyro(17, 150, Forward_Is_True = True)

    ## חזרה הביתה ##
    # פנייה חזרה דרומה
    ilan.wait_for_button("Turn left", my_debug)
    ilan.turn(-90, 150)

    # נסיעה לאחור, פנייה מערבה
    ilan.wait_for_button("Drive backwards, Turn right", my_debug)
    ilan.pid_gyro(18, 150, Forward_Is_True = False)
    ilan.turn(90, 150)

    # נסיעה לפנים עד למטוס
    ilan.wait_for_button("Go until plane", my_debug)
    if close_or_far:
        ilan.pid_gyro(87, 400)

    else: 
        ilan.pid_gyro(87 + 1, 400)

    # פנייה שמאלה כדי לא להתנגש במטוס
    ilan.wait_for_button("Avoid plane", my_debug)
    ilan.turn(-30, 200)
    # נסיעה לפנים
    ilan.pid_gyro(30, 400)
    
    # פנייה ימינה, נסיעה אל תוך אזור הבית ותפיסת המכולה הנפתחת
    ilan.wait_for_button("Take container", my_debug)
    ilan.turn(57, 150)
    ilan.pid_gyro(45 + 4, 500)

    # פנייה בתוך אזור הבית כך שהמריץ יוכל לקחת את הרובוט
    ilan.turn(-90 - 25, 200)

    # המתנה עד שהמריץ לקח את הרובוט
    wait(3000)
    # הזזת הקיר בשביל ההרצה הבאה
    ilan.move_wall_to_point(0, 0, -5000)



##### South Run #####

def south_run():
    """ Wing | Chicken | Gray container """

    my_debug = False 
    wall_debug = False

    # הזזת הקיר למקום הנחוץ בשביל המשימה
    ilan.move_wall_to_point(0, 0)
    ilan.wait_for_button("Place container", True)

    # נסיעה אל המשימה
    ilan.wait_for_button("Drive to mission", my_debug)
    ilan.pid_gyro(72, 350, Kp = 3.05)

    # דחיפה איטית של להב הטורבינה עד לנגיעה במשימה
    ilan.wait_for_button("Push turbine to mission", my_debug)
    ilan.pid_gyro(10, 180)

    # הזזת הקיר ותפיסת התרנגולת
    ilan.wait_for_button("Catch chicken", wall_debug)
    ilan.move_wall_to_point(600, 0)

    # משיכת התרנגולת והמכולה חזרה אל העיגול האפור
    ilan.wait_for_button("Pull chicken & container back to circle", my_debug)
    ilan.pid_gyro(21, 100, Forward_Is_True = False)

    # הזזת הקיר על מנת לא לקחת את התרנגולת הביתה
    ilan.wait_for_button("careful of chicken!", wall_debug)
    ilan.move_wall_to_point(0, 100)

    # חזרה הביתה - נסיעה לאחור והזזת הקיר בשביל המשימה הבאה
    ilan.pid_gyro(15, 200, False)
    ilan.turn(5, 150)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, 0, 55, 600, Forward_Is_True = False, Kp = 3.05) 

##### North West Run #####

def north_west_run():
    """ Engine | Green airplane | Green container | Gray container """

    my_debug = False
    wall_debug = False

    # הזזת הקיר למקום הנחוץ בשביל המשימה
    ilan.wait_for_button("Reset wall for mission", wall_debug)
    # ilan.reset_wall_bottom_right()
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X - 150, 0)
    
    # עצירה לשם הוספת המכולה הירוקה להלבשה
    ilan.wait_for_button("Place container", True)
    wait(50)

    # נסיעה אל הקו, הזזת הקיר
    ilan.wait_for_button("Drive to line + move wall", my_debug)
    ilan.PID_while_move_wall(ilan.WALL_MAX_ANGLE_X - 150, 0, 25, 200)

    #  נסיעה למשימה עם החיישן הימני - עד זיהוי קו שחור אחד עם החיישן השמאלי
    ilan.wait_for_button("Drive on the line until detect line", my_debug)
    ilan.pid_follow_line_until_other_detect_color(1, ilan.color_sensor_right, ilan.color_sensor_left, 90+10, white_is_right = True, kp=1.3)

    # נסיעה קצרה לפנים
    ilan.pid_gyro(2, 80)  

    # הפיכת המנוע
    ilan.wait_for_button("Turn engine over", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2 - 100, x_wait = False, y_wait = True)

    # נסיעה לאחור והזזת הקיר למעלה
    ilan.wait_for_button("Drive backward, activate Pneumatic", wall_debug)
    ilan.pid_gyro(4, 80, False)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y - 300)
    # ^                                            ^
    # | הפעלת המנגנון הפנאומטי, הפלת החלק הצהוב |

    # נסיעה לאחור + הזזת קיר שמאלה ולמטה
    # ^ תפיסת המכולה ומשיכתה אל העיגול האפור
    ilan.wait_for_button("Drive backward, pull gray container", wall_debug)
    ilan.PID_while_move_wall(0, 0, 22, Forward_Is_True = False)

    ## אילן חוזר הביתה ##
    ilan.wait_for_button("Avoid gray container", wall_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y - 400) # הזזת הקיר על מנת לא להזיז את המכולה 

    ilan.wait_for_button("Go home", my_debug)
    ilan.pid_gyro(30 + 2, 200, False) # נסיעה הביתה
    wait(100)
    # פנייה אל תוך איזור הבית                
    ilan.turn(-50, 200)

    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False)



##### North Run #####

def north_run():
    """ Crane | Containers on Deck | Small Truck | Parking """

    my_debug  = False
    wall_debug = False

    # הזזת הקיר לקראת ההרצה
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X / 2, ilan.WALL_MAX_ANGLE_Y, x_wait = False)
    ilan.wait_for_button("Place Arm", True)

    ## משימת המנוף ##
    # נסיעה עד הקו השחור
    ilan.wait_for_button("Drive to line", my_debug)
    ilan.pid_gyro(27, 150)

    # נסיעה על הקו השחור עד זיהוי שני קוים שחורים עם החיישן השמאלי
    ilan.wait_for_button("Drive until detect 2 lines", my_debug)
    ilan.pid_follow_line_until_other_detect_color(2, ilan.color_sensor_right, ilan.color_sensor_left, 120, False)
    
    # פנייה צפונה לכיוון המשימות
    ilan.turn(-90, 180)

    # פנייה אל הקו השחור
    ilan.wait_for_button("Turn to line", False)
    ilan.turn_to_threshold(ilan.color_sensor_right, False, 25)

    # מעקב על הקו השחור + נסיעה ישרה
    ilan.wait_for_button("Follow line & gyro to mission", my_debug)
    ilan.pid_follow_line(12, 90, ilan.color_sensor_right, white_is_right = True) 
    ilan.pid_gyro(12 - 2 + 0.3, 150)

    # פנייה מזרחה אל המנוף
    ilan.wait_for_button("Turn to crane", my_debug)
    ilan.turn(90, 170)

    # הזזת הקיר לדחיפת המנוף תוך כדי פנייה אל הקו השחור
    ilan.wait_for_button("Move wall to push crane", wall_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y - 200, x_wait = False, y_wait = False)

    # פנייה אל הקו השחור
    ilan.wait_for_button("Turn to line", my_debug)  
    ilan.turn_to_threshold(ilan.color_sensor_right, False, 25)

    # מעקב על הקו השחור ודחיפת המנוף
    ilan.pid_follow_line(20, 100, ilan.color_sensor_right, white_is_right = True)

    ## משימת המכולות על הספינה ##
    # נסיעה לאחור עד זיהוי הקו השחור
    ilan.gyro_sensor.reset_angle(0)
    ilan.wait_for_button("Go backward until black line", my_debug)

    while ilan.color_sensor_left.reflection() > 8:
        ilan.robot.drive(-80, ilan.gyro_sensor.angle()*-1)

    ilan.robot.stop()
    wait(100)

    # הזזת הקיר לקראת משימת המכולות
    ilan.wait_for_button("Move wall for containers", wall_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y, x_wait = False, y_wait = False)

    # פנייה אל משימת המכולות
    ilan.wait_for_button("Turn to mission", my_debug)
    gyro_angle = ilan.gyro_sensor.angle()
    ilan.turn(-90 - gyro_angle + 1, 150)

    # נסיעה קצרה לאחור לקראת ההתיישרות על המשימה
    ilan.wait_for_button("place containers", my_debug)
    ilan.pid_gyro(5, 150, False)
    
    # הזזת הקיר ימינה ומטה 
    ilan.wait_for_button("Move wall right & down", wall_debug)
    ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, ilan.WALL_MAX_ANGLE_Y / 2 - 140) 

    # נסיעה לפנים והתיישרות על המשימה
    ilan.wait_for_button("Straighten on mission", my_debug)
    ilan.pid_gyro(6.2 , 60, True)

    # הזזת ההלבשה והשארת המכולות על הספינה
    ilan.wait_for_button("Clear of containers", wall_debug)
    ilan.move_wall_to_point(0, ilan.WALL_MAX_ANGLE_Y / 2 - 140, y_wait = False) # wall max left

    ## משימות המשאית הקטנה והחנייה ##
    # נסיעה לאחור מהמשימה
    ilan.wait_for_button("Drive Gyro backwards", my_debug)
    ilan.PID_while_move_wall(0, ilan.WALL_MAX_ANGLE_Y, 12.6  - 0.8, 150, Forward_Is_True = False)

    # פנייה ימינה, הפניית אחורי הרובוט מערבה
    ilan.wait_for_button("Turn towards mission", my_debug)
    ilan.turn(90, 150)

    # Z combo!
    ilan.wait_for_button("Drive backwards 1", my_debug)
    ilan.pid_gyro(10, 150, False)
    ilan.wait_for_button("Turn 1", my_debug)
    ilan.turn(50, 150)
    ilan.wait_for_button("Drive backwards 2", my_debug)
    ilan.pid_gyro(20 - 1, 150, False)
    ilan.wait_for_button("Turn 2", my_debug)
    ilan.turn(-50, 150)

    # נסיעה חזקה לאחור, דחיפת המשאית הקטנה
    ilan.wait_for_button("Drive back, push truck", my_debug)
    ilan.pid_gyro(17, 600, False)
    wait(100)

    # נסיעה איטית לאחור - חנייה והפלת החלק הצהוב
    ilan.pid_gyro(10, 50, False)
    
    # (: זה הג'וק שהקפיץ את השפריץ של המיץ לעציץ על השפיץ של הקפיץ בחריץ המסוכן האור ההר
    # ilan.say("ze hajuk shehekpitz et hashpritz shel hamitlahatzitz al hashpitz shel hakfitz baharitz hamesukan behor hahar")



TEXT_MENU = """Choose Run: 
  < - Wing run 
  > - Green AP 
  O - Crane run 
  V - East run close 
  ^ - East run far"""


##### פונקציה להפעלת הריצות באמצעות כפתורי הרובוט #####

def running ():
    """!! One Function To Rule Them All !!"""
    
    while True:


        
        try:
            # מדפיס את טקסט הריצות על הרובוט ועל מסך המחשב
            
            ilan.write(TEXT_MENU)
            
            
            # מחכה ללחיצת כפתור
            while not any(ilan.ev3.buttons.pressed()):
                wait(60)
            

            # כפתור שמאלי - ראן דרום
            if Button.LEFT in ilan.ev3.buttons.pressed():
                
                ilan.write("South Run - Wing Run")
                south_run() # הפעלת הריצה


            # כפתור ימני - ראן צפון מערב
            elif Button.RIGHT in ilan.ev3.buttons.pressed():

                ilan.write("North West Run - Green Airplane & Containers")
                north_west_run() # הפעלת הריצה


            # כפתור תחתון - ראן מזרח (מכולות קרובות)
            elif Button.DOWN in ilan.ev3.buttons.pressed():

                ilan.write("East run close")
                east_run(True) # הפעלת הריצה (מכולות קרובות)


            # כפתור עליון - ראן מזרח (מכולות רחוקות)
            elif Button.UP in ilan.ev3.buttons.pressed():

                ilan.write("East run far")
                east_run(False) # הפעלת הראן (מכולות רחוקות)


            elif Button.CENTER in ilan.ev3.buttons.pressed():

                ilan.write("Crane run")
                north_run() # הפעלת הראן


        except Exception as ex:
            print("Error: {}".format(ex))
            wait(2500)

running()

# north_west_run()
# south_run_2022_03_09()

# # הזזה מהירה של הגלגלים 
# ilan.write("Start moving wheels")
# ilan.beep()
# while True:
#         ilan.right_motor.run(500)
#         ilan.left_motor.run(500)