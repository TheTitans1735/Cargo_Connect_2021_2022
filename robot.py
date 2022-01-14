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

        self.WALL_MAX_ANGLE_X = 1440 # need to be measured
        self.WALL_MAX_ANGLE_Y = 1350 # need to be measured
        #max x= -1445 max y= -1365

        ######################## RESET WALL ###################################
    def reset_wall(self):
        self.wall_x_motor.run_until_stalled(-800,Stop.HOLD, duty_limit=5)
        self.wall_y_motor.run_until_stalled(-1200,Stop.HOLD, duty_limit=85)
        self.wall_x_motor.reset_angle(0)
        self.wall_y_motor.reset_angle(0)
        #now we know the wall is at the top left

    ######################### MOVE WALL #################################
    # move the wall to the point specified
    def move_wall_to_point(self, x:int,y:int):
        # make sure wall does not try to extend beyond boundries
        x = min( x, self.WALL_MAX_ANGLE_X)
        y = min( y, self.WALL_MAX_ANGLE_Y)
        x = max( x, 0)
        y = max( y, 0)
        self.wall_x_motor.run_target(100, x, then=Stop.HOLD, wait=False)
        self.wall_x_motor.run_target(100, y, then=Stop.HOLD, wait=False)
        print("x = " + str(self.wall_x_motor.angle()) + ", y = " + str(self.wall_y_motor.angle()))
        
    ######################## MEASURE WALL ###################################
    # ideally will be run only once to measure the angles of the wall extremes
    def measure_wall(self):
        self.reset_wall()
        max_x = self.wall_x_motor.run_until_stalled(800,Stop.HOLD, duty_limit=5)
        max_y = self.wall_y_motor.run_until_stalled(800,Stop.HOLD, duty_limit=85)
        self.write("max x= " + str(max_x) + " max y= " + str(max_y))
    ######################## WRITE ON SCREEN ###################################
    def write(self, my_text):
        self.ev3.screen.clear()
        self.ev3.screen.draw_text(1, 20, my_text, text_color=Color.BLACK, background_color=None)
        print(my_text)
###################### WRITE ON EV3 SCREEN WITH WRAP##########################
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

    def pid_gyro(self, Td):
        self.robot.reset() 
        self.gyro_sensor.reset_angle(0)
        #Td = 1000 # target distance
        Ts = 150 # target speed of robot in mm/s
        Kp = 3 #  the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        Ki = 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        Kd = 3 #  the Constant 'K' for the 'd' derivative term
        #print(robot.distance())
        while (self.robot.distance() < Td):
            error = self.gyro_sensor.angle() # proportional 
            print("distance: " + str(self.robot.distance()) + " gyro: " + str(self.gyro_sensor.angle()))
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
        
            correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1
        
            self.robot.drive(Ts, correction)

            lastError = error  
        
            #print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
            
        self.robot.stop()

    def pid_follow_line(self,line_sensor, distance, speed, Kp):
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
        DERIVATIVE_GAIN = 0.05
        INTEGRAL_GAIN = 0.008
        integral = 0
        derivative =0
        last_error = 0
        
        # Start following the line endlessly.
        #while True:
        while (self.robot.distance() < distance):
            # Calculate the deviation from the threshold.
            error = line_sensor.reflection() - threshold
            integral = integral + error
            derivative = error - last_error
            
            # Calculate the turn rate.
            turn_rate = PROPORTIONAL_GAIN * error + DERIVATIVE_GAIN * derivative + INTEGRAL_GAIN * integral
            
            # Set the drive base speed and turn rate.
            self.robot.drive(DRIVE_SPEED, turn_rate)
            print(self.robot.distance(),line_sensor.reflection(),error,integral,derivative,turn_rate) 
            #logger.log(error,integral,derivative,turn_rate)
            last_error = error
            # You can wait for a short time or do other things in this loop.
            self.wait(10)
        #print(logger)    
        self.robot.stop()

