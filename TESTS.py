#!/usr/bin/env pybricks-micropython

from pybricks.hubs import EV3Brick
from robot import *
# Write code here
ilan = Robot()

ilan.reset_wall_bottom_right()

    # הזרוע נכנסת למשאית
ilan.move_wall_to_point(720, 70)
ilan.beep()
print("going")


# שמים את הזרוע
wait(4000)

# הרובוט נוסע אל הקו 
ilan.pid_gyro(20,100)

# הרובוט עוקב אחרי הקו עד לגשר, ושם את המשאיות בגשר
ilan.pid_follow_line(ilan.color_sensor_right,45,120,1.3, True)
ilan.move_wall_to_point(720, 0)
ilan.move_wall_to_point(0, 0)
# ilan.pid_follow_line(ilan.color_sensor_right, 10, 120, 1.3, True)
# ilan.move_wall_to_point(720, 200)
# ilan.pid_follow_line(ilan.color_sensor_right, 18, 120, 1.3, True)

# # מרים את הקיר ומוריד את הגשר הראשון
# ilan.move_wall_to_point(720, ilan.WALL_MAX_ANGLE_Y)
# ilan.pid_follow_line(ilan.color_sensor_right,15,100,1.3, True)

# # מוריד את הזרוע
# ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
# ilan.reset_wall()

# # מוריד את הקיר השני
# ilan.pid_follow_line(ilan.color_sensor_right,10,100,1.3, True)
# ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X, 100)
# ilan.robot.straight(-100)