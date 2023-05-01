from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
s_t = 800
s_b = 0

class Rec(object):
	def __init__(self, t, b, r, l):
		self.top = t
		self.bottom = b
		self.right = r
		self.left = l
		self.direction = 1  # 1 for right, -1 for left

def drawrec(rec, pos):
	glLoadIdentity()
	glTranslatef(pos[0], pos[1], 0.0)
	glBegin(GL_QUADS)
	glVertex2f(rec.left, rec.bottom)
	glVertex2f(rec.right, rec.bottom)
	glVertex2f(rec.right, rec.top)
	glVertex2f(rec.left, rec.top)
	glEnd()

def init():
	global s_t, s_b
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, 800, s_b, s_t + s_b, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)

	gluLookAt(0, b_y, -1, 0, b_y, 0, 0, 1, 0)

	
def reshape(h):
        s_t= h
        glViewport(0, 0, 800, s_t)

	



def createPlate():
	if plates == []:
		plates.append(Rec(790,800, min(random.randint(400, 750),450), max(random.randint(0,300), 250)))
	if plates[-1].top <= 650:
		plates.append(Rec(800, 790,min(random.randint(400, 750),450), max(random.randint(0,300), 250)))
def check_plates():
	pass


def stars():
	createPlate()
	for plate in plates:
		drawrec(plate, (0,0))
		plate.top += s_y
		plate.bottom += s_y
		plate.left += s_x * plate.direction
		plate.right += s_x * plate.direction
		if plate.right >= 800:
			plate.direction = -1
		elif plate.left <= 0:
			plate.direction = 1
		if plate.top <= 0:
			plates.remove(plate)
s_x = 1
s_y = -1
b_x = 400
b_y = 0
plates = []
i = 0
d_b_x = -5
start = False

def keypress(key, x, y):
	global b_x, b_y
	if key == GLUT_KEY_UP:
		b_y += 200
		start = True
	elif key == GLUT_KEY_RIGHT:
		b_x += 10
	elif key == GLUT_KEY_LEFT:
		b_x -= 10
	glutPostRedisplay()
def draw():
	global s_x, s_y, plates, i , b_x, b_y
	init()
	glColor3f(1.0, 1.0, 1.0)
	stars()
	glLoadIdentity()
	glColor3f(1.0, 0, 0)
	glTranslatef(b_x, b_y, 0.0)  # move to center of the screen
	ball = Rec(20, 0, 20, 0)
	drawrec(ball, (b_x, b_y))
	gluLookAt(b_x, b_y, -1, b_x, b_y, 0, 0, 1, 0)
	for plate in plates:
		if b_x >= plate.left and b_x <= plate.right and b_y > plate.bottom and b_y <= plate.top:
				b_y += plate.top - b_y
				d_b_x = s_y
				break
		else:
			d_b_x = -5
	if b_y > 0:
		b_y += d_b_x
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
	glutCreateWindow("OpenGL - First window demo")
	glutDisplayFunc(draw)
	glutTimerFunc(INTERVAL, game_timer, 1)
	glutKeyboardFunc(keypress)
	glutSpecialFunc(keypress)
	glutMainLoop()

main()
