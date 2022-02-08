#!/usr/bin/env pybricks-micropython


from pybricks.hubs import EV3Brick
from robot import *
# # Write code here
ilan = Robot()
# def test_wall():
#     debug=False
#     ilan.wait_for_button("10. wall reset", debug)
#     ilan.reset_wall()
#     ilan.wait_for_button("20. max x max y", debug)
#     ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X,ilan.WALL_MAX_ANGLE_Y)
#     ilan.wait_for_button("30. max x, 0", debug)
#     ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X,0)
#     ilan.wait_for_button("40. max x, max y", debug)
#     ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X,ilan.WALL_MAX_ANGLE_Y)
#     ilan.wait_for_button("50. 0, max y", debug)
#     ilan.move_wall_to_point(0,ilan.WALL_MAX_ANGLE_Y)
#     ilan.wait_for_button("60. 300,300", debug)
#     ilan.move_wall_to_point(300,300)
#     for i in range(1,30):
#         x = randint(0,ilan.WALL_MAX_ANGLE_X)
#         y = randint(0,ilan.WALL_MAX_ANGLE_Y)
#         ilan.write("x=" +str(x) + " y=" + str(y))
#         ilan.move_wall_to_point(x,y)
#         wait(1000)


# # test_wall
# def move_wall_up():
#     ilan.reset_wall()
#     ilan.move_wall_to_point(ilan.WALL_MAX_ANGLE_X/2,200)


# move_wall_up()
# while ilan.color_sensor_right.color() != Color.BLACK:
#     ilan.right_motor.run(-80)
#     ilan.left_motor.run(-100)
#     wait(100)
# ilan.right_motor.brake()
# ilan.left_motor.brake()

