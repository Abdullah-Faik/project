from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

import sys
import random
s_t = 800
s_b = 0
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class Rec(object):
	def __init__(self, t, b, r, l):
		self.top = t
		self.bottom = b
		self.right = r
		self.left = l
		self.direction = 1

def drawrec(rec):
	glLoadIdentity()
	glBegin(GL_QUADS)
	glVertex2f(rec.left, rec.bottom)
	glVertex2f(rec.right, rec.bottom)
	glVertex2f(rec.right, rec.top)
	glVertex2f(rec.left, rec.top)
	glEnd()

ball_x = 400 # ball x position in the middle of the screen when 
ball_y = 0 # ball y position in the middle of the screen when
ball_dir_y = -10 # ball y direction
ball_dir_x = -10 # ball x direction
ball = Rec(0, 20 ,510, 490) # ball rec
from rec import *
frastom_top = 800
frastom_bottom = 0
import random
plates = []
stair_step_x = 5 # moving plates	in x direction
stair_step_y = -1 # moving plates in y direction make them fall
def createPlate():
	global plates, plates_pos
	if plates == []:
		right = (random.randint(100, 200))
		x = random.randint(0, 800 - right)
		left= x
		right += x
		rec = Rec(150,140,left,right)
		plates.append(rec)

	if plates[-1].top <= frastom_top - 150:
		right = (random.randint(100, 200))
		x = random.randint(0, 800 - right)
		left= x
		right += x
		rec = Rec(150,140,left,right)
		plates.append(rec)

def stairs():
	global plates , stair_step_x, stair_step_y
	createPlate()
	for i in range(0,len(plates),1):
		drawrec(plates[i])
		# plates[i].top += stair_step_y 
		# plates[i].bottom += stair_step_y 
		plates[i].left += stair_step_x * plates[i].direction
		plates[i].right += stair_step_x * plates[i].direction
		if plates[i].right >= 800:
			plates[i].direction = -1
		elif plates[i].left <= 0:
		 	plates[i].direction = 1
		# if plates[i].top <= 0:
		# 	plates_pos.remove(plates_pos[i])

def detector():
        for plate in plates:
                if ball.top >= plate.bottom and ball.bottom <= plate.top and ball.right >= plate.left and ball.left <= plate.right:
                        ball.left += plate.direction * stair_step_x
                        ball.right += plate.direction * stair_step_x
                        ball.top += stair_step_y
                        ball.bottom += stair_step_y
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

def init():
	global frastom_top, frastom_bottom, frastom_y,ball_dir_y , ball_y, ball_x, ball_dir_x, ball_radius, plates, plates_pos
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	if frastom_top - ball_y <= 200:
		frastom_bottom = frastom_bottom -ball_dir_y + 10
		frastom_top = frastom_top -ball_dir_y + 10
	else:
		frastom_bottom += 2
		frastom_top += 2
	glOrtho(0, 800,frastom_bottom ,frastom_top, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)



start = False # start game
frastom_y = 0 # falling y

def keypress(key, x, y):
	global ball_x, ball_y
	if key == GLUT_KEY_UP:
		ball_y += 200
	elif key == GLUT_KEY_RIGHT and ball_x <= s_t - 30:
		ball_x -= ball_dir_x
	elif key == GLUT_KEY_LEFT and ball_x > 0:
		ball_x += ball_dir_x
	elif key == GLUT_KEY_DOWN:
		ball_y -= 100
	glutPostRedisplay() # this function is used to redraw the screen after any event like moving the ball


def draw():
	global stair_step_x, stair_Step_y, plates, i , ball_x, ball_y , ball_dir_y, ball_dir_x , start, allower , frastom_y
	init()
	glColor3f(1.0, 1.0, 1.0)
	stairs()
	glLoadIdentity()
	glColor3f(1.0, 0, 0)
	glTranslatef(ball_x, frastom_bottom, 0.0)
	  # move to center of the screen
	ball1()
	glutSwapBuffers()


INTERVAL = 1000
def game_timer(v):
	draw()
	glutTimerFunc(INTERVAL, game_timer, 1)

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(100, 100)
	glutCreateWindow (b"OpenGL - First window demo")
	glutDisplayFunc(draw)
	glutTimerFunc(INTERVAL, game_timer, 1)
	glutKeyboardFunc(keypress)
	glutSpecialFunc(keypress)
	glutMainLoop()

main()

