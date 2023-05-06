from rec import *
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from plates import *

ball_x = 400 # ball x position in the middle of the screen when 
ball_y = 0 # ball y position in the middle of the screen when
ball_dir_y = -10 # ball y direction
ball_dir_x = -10 # ball x direction
ball = Rec(0, 20 ,510, 490) # ball rec

def detector():
        global ball, ball_dir_x, ball_dir_y, stair_step_x
        for plate in plates:
                if ball.top >= plate.bottom and ball.bottom <= plate.top and ball.right >= plate.left and ball.left <= plate.right:
                        ball.left += plate.direction * stair_step_x
                        ball.right += plate.direction * stair_step_x
                        break
                else:
                        ball.top += ball_dir_y
                        ball.bottom += ball_dir_y
                        ball.left += ball_dir_x
                        ball.right += ball_dir_x
        if ball.bottom >= frastom_bottom:
                ball.top += ball_dir_y
                ball.bottom += ball_dir_y
        if ball.bottom <= frastom_bottom:
                ball.bottom = frastom_bottom
                ball.top = frastom_bottom + 20

def ball1():
        detector()
        drawrec(ball)