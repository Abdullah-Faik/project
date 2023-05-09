from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from rec import *
from Plates import *
from arrow import *
from Ball import *
import Global

def init():
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# if frastom_top - ball.top <= 200:
	# 	frastom_bottom = frastom_bottom - ball_dir_y + 10
	# 	frastom_top = frastom_top - ball_dir_y + 10
	# else:
	# 	frastom_bottom += 1
	# 	frastom_top += 1
	glOrtho(0, 800,Global.frastom_bottom ,Global.frastom_top, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)

def draw():
	init()
	glColor3f(1.0, 1.0, 1.0)
	stairs()
	player()
	glLoadIdentity()
	glutSwapBuffers()

INTERVAL = 10
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
	glutSpecialUpFunc(reset_keys)
	glutMainLoop()

main()

