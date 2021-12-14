
from time import sleep
from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_B, OUTPUT_C, MoveDifferential, SpeedPercent, SpeedRPM, follow_for_ms
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3
from ev3dev2.sensor.lego import ColorSensor, GyroSensor, TouchSensor
from ev3dev2.led import Leds
from ev3dev2.wheel import Wheel
from ev3dev2.sound import Sound


# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.

# Use constants for directions

# LEFT
l = 1

# RIGHT
r = -1

class ILAN_TIRE(Wheel):
    """
    part number 44309
    comes in set 31313
    """
    def __init__(self):
        Wheel.__init__(self, 62.4, 20)


class Robot:
    """all Robot actions """
    STUD_MM = 8
    wheel_distance = 80
    def __init__(self, ):
        """initialize Robot members """

        # Create your objects here.
        # self.ev3 = EV3Brick()
        # self.left_wheel = Motor(Port.B)
        # self.right_wheel = Motor(Port.C)
        # self.wall_up_down = Motor(Port.A)
        # self.wall_left_right = Motor(Port.D)
        # self.right_color_sensor = ColorSensor(INPUT_1)
        # self.left_color_sensor = ColorSensor(INPUT_2)
        self.drive = MoveDifferential(OUTPUT_B , OUTPUT_C , ILAN_TIRE,  self.wheel_distance)
        self.drive.gyro = GyroSensor(INPUT_3)
        self.drive.gyro.calibrate()
        self.speaker = Sound()
        print('success!')
    
    def move_wall(self, Vertical=0, horizontal=0):
        """up = +
         down = -
         right = +
         left = - """
        self.drive.gyro.calibrate()
        self.wall_up_down.dc(-1 * Vertical)
        self.wall_left_right.dc(horizontal)

    def run_cm(self, centimeter, speed=40):
        """drive straight by centimeter"""
        self.drive.gyro.calibrate()
        self.drive.on_for_distance(SpeedPercent(speed), -10 * centimeter)
        # self.drive.follow_gyro_angle(
        #             kp=11.3, ki=0.05, kd=3.2,
        #             speed=SpeedPercent(-1 * speed),
        #             target_angle=0,
        #             follow_for=follow_for_ms,
        #             ms=4500
        #         )

    def turn_left(self, angle, speed=40):
        """right = r = +
           left = l = - """
        self.drive.gyro.calibrate()
        self.drive.turn_left(SpeedPercent(speed), angle, brake=True, block=True, error_margin=2, use_gyro=True)

        
    def turn_right(self, angle, speed=40):
        """right = r = +
           left = l = - """
        self.drive.gyro.calibrate()
        self.drive.turn_right(SpeedPercent(speed), angle, brake=True, block=True, error_margin=2, use_gyro=True)

    
    def say(self, text):
        """ilan say the text"""
        self.speaker.speak(text)
        print(text)
    
    def beep(self):
        self.speaker.beep()
