from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from rec import *
from bal import *
from plates import *
import sys
import random
s_t = 800
s_b = 0


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
	glTranslatef(ball_x, frastom_bottom, 0.0)  # move to center of the screen
	ball()
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

