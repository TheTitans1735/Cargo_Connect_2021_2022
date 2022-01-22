#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, ColorSensor,GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media import ev3dev

ev3 = EV3Brick()
        # CONFIGURATION ILAN
left_motor = Motor(Port.B, Direction.CLOCKWISE)
right_motor = Motor(Port.C, Direction.CLOCKWISE)
robot = DriveBase(left_motor, right_motor, wheel_diameter=56, axle_track=146)
robot.settings(straight_speed=200, straight_acceleration=100, turn_rate=100)
color_sensor_left = ColorSensor(Port.S1)
color_sensor_right = ColorSensor(Port.S2)
gyro_sensor= GyroSensor(Port.S3)
arm_motor = Motor(Port.A)
################################PID GYRO##############################################
def pid_gyro(Td, Ts = 100, Kp = 1.3, Ki= 0.025, Kd = 3):
        robot.reset() 
        gyro_sensor.reset_angle(0)
        #Td = 1000 # target distance
        #Ts = 150 # target speed of robot in mm/s
        #Kp = 3 #  the Constant 'K' for the 'p' proportional controller

        integral = 0 # initialize
        #Ki = 0.025 #  the Constant 'K' for the 'i' integral term

        derivative = 0 # initialize
        lastError = 0 # initialize
        #Kd = 3 #  the Constant 'K' for the 'd' derivative term
        #print(robot.distance())
        while (robot.distance() < Td):
            error = gyro_sensor.angle() # proportional 
            print("distance: " + str(robot.distance()) + " gyro: " + str(gyro_sensor.angle()))
            if (error == 0):
                integral = 0
            else:
                integral = integral + error    
            derivative = error - lastError  
        
            correction = (Kp*(error) + Ki*(integral) + Kd*derivative) * -1
        
            robot.drive(Ts, correction)

            lastError = error  
        
            #print("error " + str(error) + "; integral " + str(integral) + "; correction " + str(correction)  )    
            
        robot.stop()


robot.drive(50,0)
#  robot.straight(500)

wait(10000)
robot.stop()