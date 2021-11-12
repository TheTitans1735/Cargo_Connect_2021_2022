from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Use constants for directions

# LEFT
l = 1

# RIGHT
r = -1

class Robot:
    """all Robot actions """

    def __init__(self, wheel_diameter=62.4, axle_track=80):
        """initialize Robot members """

        # Create your objects here.
        self.ev3 = EV3Brick()
        self.left_wheel = Motor(Port.B)
        self.right_wheel = Motor(Port.C)
        self.wall_up_down = Motor(Port.A)
        self.wall_left_right = Motor(Port.D)
        self.right_color_sensor = ColorSensor(Port.S1)
        self.left_color_sensor = ColorSensor(Port.S2)
        self.gyro_sensor = GyroSensor(Port.S3)
        self.drive = DriveBase(self.right_wheel , self.left_wheel , wheel_diameter, axle_track)
        print('success!')
    
    def move_wall(self, Vertical=0, horizontal=0):
        """up = +
         down = -
         right = +
         left = - """

        self.wall_up_down.dc(-1 * Vertical)
        self.wall_left_right.dc(horizontal)

    def run_cm(self, centimeter):
        """drive straight by centimeter"""
        self.drive.straight(-10 * centimeter)

    def turn(self, direction, angle):
        """right = r = +
           left = l = - """
        deg = angle * 4 / 3
        self.drive.turn(direction * deg)
    
    def say(self, text):
        """ilan say the text"""
        self.ev3.speaker.say(text)
    
    def beep(self):
        self.ev3.speaker.beep()
