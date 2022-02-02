from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media import ev3dev

class Robot:
    """all Robot actions """

    def __init__(self):
        # Define Robot
        self.ev3 = EV3Brick()
        # CONFIGURATION ILAN
        self.left_motor = Motor(Port.C, Direction.COUNTERCLOCKWISE)
        self.right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)
        self.robot = DriveBase(self.left_motor, self.right_motor, wheel_diameter=62.4, axle_track=122)
        self.robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)

        self.color_sensor_left = ColorSensor(Port.S2)
        self.color_sensor_right = ColorSensor(Port.S1)
        self.gyro_sensor= GyroSensor(Port.S3)
        self.wall_x_motor = Motor(Port.D) 
        self.wall_y_motor = Motor(Port.A,Direction.COUNTERCLOCKWISE) 

        #self.WALL_MAX_ANGLE_X = 1440 # need to be measured
        self.WALL_MAX_ANGLE_X = 870
        #self.WALL_MAX_ANGLE_Y = 1350 # need to be measured
        self.WALL_MAX_ANGLE_Y = 750
        #max x= -1445 max y= -1365

        ######################## RESET WALL ###################################
    def reset_wall(self):
        speed_x = -800
        speed_y = -1200
        # if upper_right:
        #     speed_x = -1 * speed_x
        #     speed_y = -1 * speed_y
        self.wall_y_motor.run_until_stalled(speed_y,Stop.HOLD, duty_limit=85)
        self.wall_x_motor.run_until_stalled(speed_x,Stop.HOLD, duty_limit=5)
        
        self.wall_x_motor.reset_angle(0)
        self.wall_y_motor.reset_angle(0)
        # if upper_right:
        #     self.wall_x_motor.reset_angle(self.WALL_MAX_ANGLE_X)
        #     self.wall_y_motor.reset_angle(self.WALL_MAX_ANGLE_Y)
        print("x = " + str(self.wall_x_motor.angle()) + ", y = " + str(self.wall_y_motor.angle()))

    ######################### MOVE WALL #################################
    def reset_wall_bottom_right(self):
        speed_x = 800
        speed_y = -1200
        # if upper_right:
        #     speed_x = -1 * speed_x
        #     speed_y = -1 * speed_y
        self.wall_x_motor.run_until_stalled(speed_x,Stop.HOLD, duty_limit=5)
        self.wall_y_motor.run_until_stalled(speed_y,Stop.HOLD, duty_limit=85)
        self.wall_x_motor.reset_angle(self.WALL_MAX_ANGLE_X)
        self.wall_y_motor.reset_angle(0)
        # if upper_right:
        #     self.wall_x_motor.reset_angle(self.WALL_MAX_ANGLE_X)
        #     self.wall_y_motor.reset_angle(self.WALL_MAX_ANGLE_Y)
        print("x = " + str(self.wall_x_motor.angle()) + ", y = " + str(self.wall_y_motor.angle()))
    #waiting for button and showing text - for debugging
    def wait_for_button(self,text,debug=True):
        self.write(text)
        if not debug:
            return
        while not any(self.ev3.buttons.pressed()):
            wait(10)
        wait(300)
        
    # move the wall to the point specified
    def move_wall_to_point(self, x:int,y:int, speed=-1000):
        # make sure wall does not try to extend beyond boundries
        #print("x = " + str(self.wall_x_motor.angle()) + ", y = " + str(self.wall_y_motor.angle()))
        x = min( x, self.WALL_MAX_ANGLE_X-10)
        y = min( y, self.WALL_MAX_ANGLE_Y-10)
        x = max( x, 10)
        y = max( y, 10)
        #print(str(x),str(y))
        self.wall_x_motor.run_target(speed, x, Stop.BRAKE, wait=True)
        self.wall_y_motor.run_target(speed, y, Stop.BRAKE, wait=True)
        # if y ended before x, wait for x to get to target
        # self.wall_x_motor.run_target(speed, x, Stop.HOLD, wait=True)
        # wait(3000)
    
    ######################## MEASURE WALL ###################################
    # ideally will be run only once to measure the angles of the wall extremes
    def measure_wall(self):
        self.reset_wall()
        max_x = self.wall_x_motor.run_until_stalled(800,Stop.HOLD, duty_limit=20)
        max_y = self.wall_y_motor.run_until_stalled(800,Stop.HOLD, duty_limit=1)
        self.write("max x= " + str(max_x) + " max y= " + str(max_y))
        self.wall_y_motor.stop()
        self.wall_x_motor.stop()

    ######################## WRITE ON SCREEN ###################################
    def write(self, my_text):
        self.ev3.screen.clear()
        self.ev3.screen.draw_text(1, 1, my_text, text_color=Color.BLACK, background_color=None)
        print(my_text)

    ###################### WRITE ON EV3 SCREEN WITH WRAP########################
    def write2(self, my_text):
        self.ev3.screen.clear()
        current_line = ""
        current_y=1
        for elem in my_text:
            if ev3dev.Font.DEFAULT.text_width(current_line + " ") > self.ev3.screen.width:   
                #we need to write this line
                self.ev3.screen.draw_text(current_y, 1, current_line, text_color=Color.BLACK, background_color=None)        
                current_line = ""
                current_y = current_y + ev3dev.Font.DEFAULT.text_height(my_text) + 1
            current_line = current_line + elem
        print(my_text)
    
    def beep(self):
        self.ev3.speaker.beep()

    
    def say(self, text, voice='m1', volume=100):
        self.ev3.speaker.set_volume(volume)
        self.ev3.speaker.set_speech_options(voice)
        self.ev3.speaker.say(text)

    def pid_gyro(self,Td, Ts = 150, Forward_Is_True = True, Kp = 3, Ki= 0.025, Kd = 3):
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
        while (abs(self.robot.distance()) < Td*10):
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


######################## PID FOLLOW LINE ###################################

    def pid_follow_line(self,line_sensor, distance, speed, Kp = 1.3, Ki = 0.01, Kd = 0.07, white_is_right = True):
        self.robot.reset() 
        # Calculate the light threshold. Choose values based on your measurements.
        #6,71
        BLACK = 6
        WHITE = 71
        threshold = (BLACK + WHITE) / 2
        self.robot.reset()
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
            # You can wait for a short time or do other things in this loop.
            wait(10)
        #print(logger)    
        self.robot.stop()


######################## PID FOLLOW RIGHT LINE UNTIL LEFT DETECT LINE ###################################

    def pid_follow_right_line_until_left_detect_line(self, speed, lines_till_stop, Kp, white_is_right):
        self.robot.reset() 
        # Calculate the light threshold. Choose values based on your measurements.
        #6,71
        BLACK = 6
        WHITE = 71
        threshold = (BLACK + WHITE) / 2
        self.robot.reset()
        #logger = DataLog('error', 'integral','derivative','turn_rate')
        # Set the drive speed at 100 millimeters per second.
        DRIVE_SPEED = speed

        # Set the gain of the proportional line controller. This means that for every
        # percentage point of light deviating from the threshold, we set the turn
        # rate of the drivebase to 1.2 degrees per second.

        # For example, if the light value deviates from the threshold by 10, the robot
        # steers at 10*1.2 = 12 degrees per second.
        PROPORTIONAL_GAIN = Kp
        DERIVATIVE_GAIN = 0.07
        INTEGRAL_GAIN = 0.01
        integral = 0
        derivative =0
        last_error = 0

        color_counter = 0
        last_color = 0
        # Start following the line endlessly.
        #while True:
        while (color_counter < lines_till_stop):
            # Calculate the deviation from the threshold.
            error = self.color_sensor_right.reflection() - threshold
            integral = integral + error
            derivative = error - last_error
            
            # Calculate the turn rate.
            turn_rate = PROPORTIONAL_GAIN * error + DERIVATIVE_GAIN * derivative + INTEGRAL_GAIN * integral
            if white_is_right:
                turn_rate = turn_rate * -1
            # Set the drive base speed and turn rate.
            self.robot.drive(DRIVE_SPEED, turn_rate)
            print("distance = " , self.robot.distance() , "  |  reflection = " , self.color_sensor_right.reflection() , "  |  error = " , error ,
                "  |  integral = " , integral , "  |  derivative = " , derivative , "  |  turn_rate = " , turn_rate, 
                "  |  gyro = ", self.gyro_sensor.angle(), " | rcolor = ", str(self.color_sensor_left.reflection()))
            last_error = error
            # You can wait for a short time or do other things in this loop.
            wait(5)            

            if (self.color_sensor_left.reflection() <= 30 and last_color >= 60):
                color_counter += 1
                self.beep()
                self.write("Line " + str(color_counter) + " Detected")

            last_color = self.color_sensor_left.reflection()
            self.write("Color: " + str(last_color))

        #print(logger)    
        self.robot.stop()


    def run_straight(self, distance):
        self.robot.straight(distance * 10)

######################## TURN ###################################
    def turn(self, angle, speed=100):
        self.gyro_sensor.reset_angle(0)
        wait(500)

        #פנייה ימינה - זווית פנייה חיובית
        if angle > 0:

            #נוסע כמעט עד ערך הזווית במהירות מלאה
            while self.gyro_sensor.angle() <= angle * 0.8:
                self.right_motor.run(speed=(-1 * speed))
                self.left_motor.run(speed=speed)
            self.right_motor.brake()
            self.left_motor.brake()

            #נוסע את שארית ערך הזווית במהירות מופחתת - פי 0.2
            while self.gyro_sensor.angle() < angle:
                self.right_motor.run(speed=(-0.2 * speed))
                self.left_motor.run(speed=speed*0.2)
            self.right_motor.brake()
            self.left_motor.brake()
            
            #תיקון איטי נוסף למקרה שצריך
            while self.gyro_sensor.angle() > angle:
                self.right_motor.run(20)
                self.left_motor.run(-20)
                wait(10)  

        #פנייה שמאלה - זווית פנייה שלילית
        elif angle < 0:  
            
            #נוסע כמעט עד ערך הזווית במהירות מלאה, הגלגלים נעים בכיוון הפוך
            while self.gyro_sensor.angle() >= angle * 0.8:
                self.right_motor.run(speed=(speed))
                self.left_motor.run(speed=speed*-1)
            self.right_motor.brake()
            self.left_motor.brake()

            #נוסע את שארית ערך הזווית במהירות מופחתת - פי 0.2
            while self.gyro_sensor.angle() > angle:
                self.right_motor.run(speed=(0.2 * speed))
                self.left_motor.run(speed=speed*-0.2)
            self.right_motor.brake()
            self.left_motor.brake()

            #תיקון איטי נוסף למקרה שצריך
            while self.gyro_sensor.angle() > angle:
                self.right_motor.run(-20)
                self.left_motor.run(20)
                wait(10)  
   
        self.right_motor.brake()
        self.left_motor.brake()
        # self.robot.stop()
        print("Gyro angle:" + str(self.gyro_sensor.angle())) 
