from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media import ev3dev
import csv
import time
#import datetime
"""
All Robot actions
"""
class Robot:

    ##### ROBOT TRAITS #####
    
    def __init__(self):

        # define robot
        self.ev3 = EV3Brick()

        ## Ilan's Configuration ##
        # motors
        self.left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

        # robot
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=62.4, axle_track=122)
        self.robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

        # color sensors
        self.color_sensor_left = ColorSensor(Port.S2)
        self.color_sensor_right = ColorSensor(Port.S1)

        # gyro sensor
        self.gyro_sensor= GyroSensor(Port.S3)

        # wall's motors
        self.wall_x_motor = Motor(Port.D) 
        self.wall_y_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE) 

        # define constant traits - wall's max angles
        self.WALL_MAX_ANGLE_X = 860
        self.WALL_MAX_ANGLE_Y = 740
        


    ##### RESET WALL #####

    def reset_wall(self):
        """"
        מאפס את הקיר לצד שמאל למטה
        """

        # define x & y motor's speed
        speed_x = -800
        speed_y = -1200

        # move the wall to max values
        self.wall_y_motor.run_until_stalled(speed_y,Stop.HOLD, duty_limit=85)
        self.wall_x_motor.run_until_stalled(speed_x,Stop.HOLD, duty_limit=5)
        wait(100)

        # make wall's 0 angle current angle
        self.wall_x_motor.reset_angle(0)
        self.wall_y_motor.reset_angle(0)

        # enter the current wall values into the file
        self.push_wall_values()
        
        # write current angles
        self.write("x = " + str(self.wall_x_motor.angle()) + "\ny = " + str(self.wall_y_motor.angle()))



    ##### RESET WALL BOTTON RIGHT #####

    def reset_wall_bottom_right(self):
        """"
        מאפס את הקיר לצד ימין למטה
        """

        # define x & y motor's speed
        speed_x = 800
        speed_y = -1200
        
        # move the wall to max values
        self.wall_y_motor.run_until_stalled(speed_y,Stop.HOLD, duty_limit=85)
        self.wall_x_motor.run_until_stalled(speed_x,Stop.HOLD, duty_limit=5)
        wait(100)

        # make wall's 0 angle current angle
        self.wall_x_motor.reset_angle(self.WALL_MAX_ANGLE_X)
        self.wall_y_motor.reset_angle(0)

        # enter the current wall values into the file
        self.push_wall_values()
        
        # write current angles
        self.write("x = " + str(self.wall_x_motor.angle()) + "\ny = " + str(self.wall_y_motor.angle()))



    ##### PUSH WALL'S CURRENT VALUES #####

    def push_wall_values(self):
        """
        כתיבת ערך הפוזיציה הנוכחית של הקיר בקובץ טקסט    
        """
        # with open('wall_values.txt', 'w+') as f:
        #     wait(50)
        #     f.write(str(self.wall_x_motor.angle()) + "," + str(self.wall_y_motor.angle()))
        pass
            

        
    ##### UPDATE WALL'S CURRENT VALUES #####

    def update_angles_from_file(self):
        """
        עדכון ערך הפוזיציה הנוכחית של הקיר לפי מה שנכתב בקובץ הטקסט
        """
        # with open('wall_values.txt') as f:
        #     content = f.readline()
        #     x_value, y_value = content.split(",")
        #     wait(50)
        #     self.wall_x_motor.reset_angle(int(x_value))
        #     self.wall_y_motor.reset_angle(int(y_value))
        pass


    
    ##### MOVE WALL TO POINT #####

    def move_wall_to_point(self, x:int,y:int, speed=-1200, x_wait = True, y_wait = True):
        """
        הזזת הקיר לנקודה מסויימת בטווח התנועה שלו
        """
        # get the wall's current position from file
        self.update_angles_from_file()

        # make sure wall does not try to extend beyond boundries:
        # define minimum and maximum values
        x = min( x, self.WALL_MAX_ANGLE_X)
        y = min( y, self.WALL_MAX_ANGLE_Y)
        x = max( x, 10)
        y = max( y, 10)
        
        # move motors until wall reaches the target position
        # motors can move together or continue to next function based on wait paremiter 

        self.wall_x_motor.run_target(speed, x, Stop.BRAKE, wait = x_wait)
        self.wall_y_motor.run_target(speed, y, Stop.BRAKE, wait = y_wait) 
        
        
        wait(100)
        self.push_wall_values()
        print("x = " + str(self.wall_x_motor.angle()) + ", y = "  + str(self.wall_y_motor.angle()))
        
    ######################## MEASURE WALL ###################################
    # ideally will be run only once to measure the angles of the wall extremes
    def measure_wall(self):

        """"פונקציה שבעזרתה בדקנו מה האיקס והוואי של הקיר בפינות"""

        self.reset_wall()
        max_x = self.wall_x_motor.run_until_stalled(800,Stop.HOLD, duty_limit=20)
        max_y = self.wall_y_motor.run_until_stalled(800,Stop.HOLD, duty_limit=1)
        self.write("max x= " + str(max_x) + " max y= " + str(max_y))
        self.wall_y_motor.stop()
        self.wall_x_motor.stop()

    def PID_while_move_wall(self, x:int,y:int, drive_distance , drive_speed = 150 , seconds_to_start_wall = 0,wall_speed=-1200 , Forward_Is_True = True, Kp = 3.06, Ki= 0.027, Kd = 3.02):
        
        self.update_angles_from_file()
        x = min( x, self.WALL_MAX_ANGLE_X)
        y = min( y, self.WALL_MAX_ANGLE_Y)
        x = max( x, 10)
        y = max( y, 10)
        #print(str(x),str(y))
         # מוסיפים 5 בגלל שציר וואי פועל עם גלגלי שיניים אחרים שמשנים לו טיפה את המעלות שהוא מגיע אליהם
        # if y ended before x, wait for x to get to target
        # self.wall_x_motor.run_target(speed, x, Stop.HOLD, wait=True)
        # wait(3000)
        
        


        ##################################____PID PART____#############################
        direction_indicator = -1
        speed_indicator = -1       #משתנה שנועד כדי לכפול אותו במהירות ובתיקון השגיאה כדי שנוכל לנסוע אחורה במידת הצורך          
        if Forward_Is_True:             #אם נוסעים קדימה - תכפול באחד. אחורה - תכפול במינוס אחד
            direction_indicator = -1
            speed_indicator = 1   
        self.robot.reset() 
        self.gyro_sensor.reset_angle(0)
        #Td = 1000 # target distance
        #Ts = 150 # target speed of robot in mm/s
        #Kp = 3 #  the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        #Ki = 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        #Kd = 3 #  the Constant 'K' for the 'd' derivative term
        #print(robot.distance())
        sw_for_wall_timing = StopWatch()
        while (abs(self.robot.distance()) < drive_distance*10 or self.wall_x_motor.speed() != 0 and self.wall_y_motor.speed() != 0):
            self.check_forced_exit()

            error = self.gyro_sensor.angle() # proportional 
            print("distance: " + str(self.robot.distance()) + " gyro: " + str(self.gyro_sensor.angle()))
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
        
            correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1

            self.robot.drive(drive_speed * speed_indicator , correction * direction_indicator * -1)
            if sw_for_wall_timing.time() > seconds_to_start_wall * 1000: 
                self.wall_x_motor.run_target(wall_speed, x, Stop.BRAKE, wait=False)         #לולאה שתפקידה לתזמן את תחילת פעולת הקיר
                self.wall_y_motor.run_target(wall_speed, y, Stop.BRAKE, wait=False)
            
            lastError = error  
        
            #print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
            
        self.robot.stop()
        self.wall_x_motor.stop()
        self.wall_y_motor.stop()
        self.push_wall_values()
        if self.wall_x_motor.angle() != x or self.wall_y_motor.angle() != y:                # מקרה קצה שבו הזזת הקיר לא הושלמה בתום המרחק
            self.move_wall_to_point(x,y)
        print("distance: " + str(self.robot.distance()) + " gyro: " + str(self.gyro_sensor.angle()))
        print("wall_x: " + str(self.wall_x_motor.angle()) + " wall_y: " + str(self.wall_y_motor.angle()))
        
            
    
    def check_gyro(self):
        """
        פונקציה לבדיקה האם הגיירו מאופס, אם לא משמיע אזעקה עד שהוא מאופס.
        """
    
        try:
            current_gyro = self.gyro_sensor.angle()
            wait(500)
            while current_gyro != self.gyro_sensor.angle():
                for _ in range(3):
                    self.ev3.speaker.play_file("GENERAL_ALERT.wav")
                    wait(10)
                wait(10)
        except:
            self.ev3.speaker.play_file("GENERAL_ALERT.wav")
            wait(10)
        
            
            
        return True



    #waiting for button and showing text - for debugging
    def check_forced_exit(self):
        if len(self.ev3.buttons.pressed()) >= 2:
            self.write("Forced Exit")
            print("!!!!!!!!!!!!!!!!!!!! FORCED EXIT !!!!!!!!!!!!!!!!!!!!!!!!")
            raise Exception("Forced Exit")
        

    def wait_for_button(self, text, debug = True):
        self.write(text)
        self.check_forced_exit()
        if not debug:
            return
        
        while not any(self.ev3.buttons.pressed()):
            wait(10)
            

    # move the wall to the point specified
    


    ###################### WRITE ON EV3 SCREEN WITH WRAP########################
    def write(self, my_text):
        " מדפיס טקסט נתון במחשב ועל מסך הרובוט "
        self.ev3.screen.clear()

        print(my_text)
        
        lines = my_text.split("\n")
        for i in range(0, len(lines)):
            self.ev3.screen.draw_text(1, i * 20, lines[i], text_color = Color.BLACK, background_color=None)
    
    def beep(self):

        """"אילן עושה ביפ"""

        self.ev3.speaker.beep()

    
    def say(self, text, voice='m1', volume=100):

        """"אילן אומר את הטקסט.
        ניתן לשלוט על הווליום ואפילו לשנות את המבטא של אילן."""

        self.ev3.speaker.set_volume(volume)
        self.ev3.speaker.set_speech_options(voice)
        self.ev3.speaker.say(text)


    # ------------------ PID Gyro ------------------ 

    def pid_gyro(self,Td, Ts = 150, Forward_Is_True = True, Kp = 3.06, Ki= 0.027, Kd = 3.02):
        # if self.stop_run = True
        direction_indicator = -1
        speed_indicator = -1       #משתנה שנועד כדי לכפול אותו במהירות ובתיקון השגיאה כדי שנוכל לנסוע אחורה במידת הצורך          
        if Forward_Is_True:             #אם נוסעים קדימה - תכפול באחד. אחורה - תכפול במינוס אחד
            direction_indicator = -1
            speed_indicator = 1   
        self.robot.reset() 
        self.gyro_sensor.reset_angle(0)
        #Td = 1000 # target distance
        #Ts = 150 # target speed of robot in mm/s
        #Kp = 3 #  the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        #Ki = 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        #Kd = 3 #  the Constant 'K' for the 'd' derivative term
        
        while (abs(self.robot.distance()) < Td*10):
            wait(20) #ע"מ לא לגזול את כל המשאבים
            self.check_forced_exit()

            error = self.gyro_sensor.angle() # proportional 
            print("distance: " + str(self.robot.distance()) + " gyro: " + str(self.gyro_sensor.angle()))
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
        
            correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1
        
            self.robot.drive(Ts * speed_indicator , correction * direction_indicator * -1) 

            lastError = error  
          
            
        self.robot.stop()
        

    # ------------------ PID Gyro until color ------------------
    def pid_gyro_until_color(self, stop_color = Color.BLACK, Ts = 150, Forward_Is_True = True, Kp = 3.06, Ki= 0.027, Kd = 3.02):
        
        direction_indicator = -1
        speed_indicator = -1       #משתנה שנועד כדי לכפול אותו במהירות ובתיקון השגיאה כדי שנוכל לנסוע אחורה במידת הצורך  

        if Forward_Is_True:             #אם נוסעים קדימה - תכפול באחד. אחורה - תכפול במינוס אחד
            direction_indicator = -1
            speed_indicator = 1   

        self.robot.reset() 
        self.gyro_sensor.reset_angle(0)
        #Td = 1000 # target distance
        #Ts = 150 # target speed of robot in mm/s
        #Kp = 3 #  the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        #Ki = 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        #Kd = 3 #  the Constant 'K' for the 'd' derivative term
        #print(robot.distance())
        while (self.color_sensor_right.color() != stop_color or self.color_sensor_left.color() != stop_color):
            self.check_forced_exit()

            error = self.gyro_sensor.angle() # proportional 
            print("distance: " + str(self.robot.distance()) + " gyro: " + str(self.gyro_sensor.angle()))
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
        
            correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1
        
            self.robot.drive(Ts * speed_indicator , correction * direction_indicator * -1) 

            lastError = error  
        
            #print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
            
        self.robot.stop()


    # ------------------ Straighten on Black ------------------
    def straighten_on_black(self, speed = 90, drive_forward = True):
        if drive_forward == False:
            speed = speed * -1

        self.right_motor.run(speed)
        self.left_motor.run(speed)

        right_sensor_flag = False
        left_sensor_flag = False
        target_reflection = -1

        while(right_sensor_flag == False or left_sensor_flag == False):
            self.check_forced_exit()

            if target_reflection == -1:
                if self.color_sensor_right.color() == Color.BLACK:
                    right_sensor_flag = True
                    target_reflection = self.color_sensor_right.reflection()
                    self.right_motor.brake()

                elif self.color_sensor_left.color() == Color.BLACK:
                    left_sensor_flag = True
                    target_reflection = self.color_sensor_left.reflection()
                    self.left_motor.brake()

                self.write("L: " + str(self.color_sensor_left.color()) + " R: " + str(self.color_sensor_right.color()))

            else:
                if self.color_sensor_right.reflection() == target_reflection:
                    right_sensor_flag = True
                    self.right_motor.brake()

                if self.color_sensor_left.reflection() <= target_reflection:
                    left_sensor_flag = True
                    self.left_motor.brake()

                self.write("L: " + str(self.color_sensor_left.reflection()) + " R: " + str(self.color_sensor_right.reflection()))

            wait(10)
        
        self.write("C Left: " + str(self.color_sensor_left.color()))
        self.write("C Right: " + str(self.color_sensor_right.color()))
        self.write("R Left: " + str(self.color_sensor_left.reflection()))
        self.write("R Right: " + str(self.color_sensor_right.reflection()))

            

            


    # ------------------ PID Follow Line ------------------

    def pid_follow_line(self, distance, speed, line_sensor, stop_condition = lambda: False, Kp = 1.30 ,Ki = 0.01, white_is_right = True, Kd=0.07):
        self.robot.reset() 
        initial_gyro_angle = self.gyro_sensor.angle()
        # Start a stopwatch to measure elapsed time
        watch = StopWatch()
        #self.data =DataLog("Distance", "Reflection", "Error", "PROPORTIONAL_GAIN", "INTEGRAL_GAIN", "DERIVATIVE_GAIN", "integral", "derivative", "turn_rate", "gyro", "speed", "white_is_right","Gyro_Offset","MS_From_Start" timestamp=True)
        log_file_name = time.strftime("%Y_%m_%d_%H_%M_%S")
        print(log_file_name)
        self.data =DataLog("Distance", "Reflection", "Error", "PROPORTIONAL_GAIN", "INTEGRAL_GAIN", "DERIVATIVE_GAIN", "integral", "derivative", "turn_rate", "gyro", "speed", "white_is_right","Gyro_Offset","MS_From_Start",name=log_file_name,timestamp=False)
        # Calculate the light threshold. Choose values based on your measurements.
        #6,71
        BLACK = 6
        WHITE = 71
        threshold = (BLACK + WHITE) / 2
        #self.robot.reset()
        #logger = DataLog('error', 'integral','derivative','turn_rate')
        # Set the drive speed at 100 millimeters per second.
        DRIVE_SPEED = speed
        # Set the gain of the proportional line controller. This means that for every
        # percentage point of light deviating from the threshold, we set the turn
        # rate of the drivebase to 1.2 degrees per second.
        # For example, if the light value deviates from the threshold by 10, the robot
        # steers at 10*1.2 = 12 degrees per second.
        PROPORTIONAL_GAIN = Kp
        DERIVATIVE_GAIN = Kd
        INTEGRAL_GAIN = Ki
        integral = 0
        derivative =0
        last_error = 0
        
        # Start following the line endlessly.
        #while True:
        while (abs(self.robot.distance()) < distance*10):
            self.check_forced_exit()

            # Calculate the deviation from the threshold.
            error = line_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error
            
            # Calculate the turn rate.
            turn_rate = PROPORTIONAL_GAIN * error + DERIVATIVE_GAIN * derivative + INTEGRAL_GAIN * integral
            if white_is_right:
                turn_rate = turn_rate * -1
            # Set the drive base speed and turn rate.
            self.robot.drive(DRIVE_SPEED, turn_rate)
            print("distance = " , self.robot.distance() , "  |  reflection = " , line_sensor.reflection() , "  |  error = " , error ,
                "  |  integral = " , integral , "  |  derivative = " , derivative , "  |  turn_rate = " , turn_rate, "  |  gyro = ", self.gyro_sensor.angle())
            last_error = error
            self.data.log(self.robot.distance(), line_sensor.reflection(), error, PROPORTIONAL_GAIN, INTEGRAL_GAIN, DERIVATIVE_GAIN, integral, derivative, turn_rate, self.gyro_sensor.angle(), speed, white_is_right,self.gyro_sensor.angle()- initial_gyro_angle,watch.time())
            # עוצר במקרה שזיהה תנאי עצירה
            if stop_condition():
                break

            # You can wait for a short time or do other things in this loop.
            wait(10)
            
        #print(logger)    
        self.robot.stop()


    ##### PID FOLLOW RIGHT LINE UNTIL LEFT DETECT COLOR #####
    def pid_follow_right_line_until_left_detect_color(self, lines_till_stop, follow_color_sensor, detection_color_sensor, speed = 90, white_is_right = True, stop_color = Color.BLACK, kp = 1.3):
        my_debug = False

        # מגדיר את תנאי העצירה
        stop_on_black = lambda : detection_color_sensor.color() == stop_color

        self.wait_for_button("Start Follow", my_debug)

        # מוצא קווים ככמות הפרמטר
        for i in range (0, lines_till_stop):
            self.check_forced_exit()
            
            if (i > 0):
                self.pid_follow_line(10, 80, follow_color_sensor, Kp=kp, white_is_right = white_is_right)
            
            self.pid_follow_line(150, speed, follow_color_sensor, stop_condition = stop_on_black, Kp = kp, white_is_right = white_is_right)
            self.beep()


    def run_straight(self, distance):
        self.robot.straight(distance * 10)

######################## TURN ###################################
    def turn(self, angle, speed=100):
        self.gyro_sensor.reset_angle(0)
        # 2022-02-05 Rotem was wait 500. Reduced to 10
        wait(10)


        #פנייה ימינה - זווית פנייה חיובית
        if angle > 0:

            #נוסע כמעט עד ערך הזווית במהירות מלאה
            while self.gyro_sensor.angle() <= angle * 0.8:
                self.check_forced_exit()

                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(speed=(-1 * speed))
                self.left_motor.run(speed=speed)
            self.right_motor.brake()
            self.left_motor.brake()

            #נוסע את שארית ערך הזווית במהירות מופחתת - פי 0.2
            while self.gyro_sensor.angle() < angle:
                self.check_forced_exit()
                
                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(speed=(-0.2 * speed))
                self.left_motor.run(speed=speed*0.2)
            self.right_motor.brake()
            self.left_motor.brake()
            
            #תיקון איטי נוסף למקרה שצריך
            while self.gyro_sensor.angle() > angle:
                self.check_forced_exit()
                
                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(20)
                self.left_motor.run(-20)
                wait(10)

          

        #פנייה שמאלה - זווית פנייה שלילית
        elif angle < 0:  
            
            #נוסע כמעט עד ערך הזווית במהירות מלאה, הגלגלים נעים בכיוון הפוך
            while self.gyro_sensor.angle() >= angle * 0.8:
                self.check_forced_exit()
                
                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(speed=(speed))
                self.left_motor.run(speed=speed*-1)
            self.right_motor.brake()
            self.left_motor.brake()

            #נוסע את שארית ערך הזווית במהירות מופחתת - פי 0.2
            while self.gyro_sensor.angle() > angle:
                self.check_forced_exit()
                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(speed=(0.2 * speed))
                self.left_motor.run(speed=speed*-0.2)
            self.right_motor.stop()
            self.left_motor.stop()

            #תיקון איטי נוסף למקרה שצריך
            while self.gyro_sensor.angle() > angle:
                self.check_forced_exit()
                print("degree: " + str(self.gyro_sensor.angle()))
                self.right_motor.run(-20)
                self.left_motor.run(20)
                wait(10)  
   
        self.right_motor.stop()
        self.left_motor.stop()
        print("final degree: " + str(self.gyro_sensor.angle()))
        # self.robot.stop()
        # print("Gyro angle:" + str(self.gyro_sensor.angle()))


    # TURN UNTIL SECONDS
    def turn_until_seconds(self, seconds, max_angle, speed = 150, turn_right = True):
        "Right = True, Left = False"

        if turn_right == False:
            speed = speed * -1

        sw = StopWatch()
        self.gyro_sensor.reset_angle(0)

        while sw.time() < seconds * 1000 and abs(self.gyro_sensor.angle()) < max_angle:
            self.check_forced_exit()
            
            self.left_motor.run(speed)
            self.right_motor.run(speed * -1)

        self.right_motor.stop()
        self.left_motor.stop()


    def turn_until_color (self, line_sensor, color = Color.BLACK, turn_right = True, speed = 100):
        if turn_right == False:
            speed = speed * -1

        while line_sensor.color() != color:
            self.check_forced_exit()
            
            self.left_motor.run(speed)
            self.right_motor.run(speed * -1)

        self.right_motor.stop()
        self.left_motor.stop()



    ##### LEARN THE BEST VALUES FOR PID FOLLOW LINE #####
    def learn_pid_line_values (self, line_sensor, distace = 150, speed = 100, value_checking = "Kp", kp = 1.3, ki = 0.01, kd = 0.07, num_of_loops = 20):

        # Create the file to write in with following catagories:
        # Direction - Forward / Backward | Time passed from last end of the line | Distance passed from last end of the line |
        # Current Kp value | Current Ki value | Current Kd value | Current Gyro angle |
        pid_line_values = DataLog ('Direction', 'Time from line end', 'Distance from line end',
        'Kp', 'Ki', 'Kd', 'Gyro angle', name = 'Learn Pid Values', timestamp = True)

        while True:

            for i in range(0, num_of_loops):
                self.pid_follow_line(distace, speed, line_sensor, Kp = kp, Ki = ki, Kd = kd)
                wait(200)
                self.turn(180, 200)

                self.pid_follow_line(distace, speed, line_sensor, Kp = kp, Ki = ki, Kd = kd, white_is_right = False)
                wait(200)
                self.turn(200, 200)

            if value_checking == "Kp" or value_checking == "kp":
                kp = kp + 0.01

            elif value_checking == "Ki" or value_checking == "ki":
                ki = ki + 0.01

            elif value_checking == "Kd" or value_checking == "kd":
                kd = kd + 0.01
