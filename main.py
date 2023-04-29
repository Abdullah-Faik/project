from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random

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
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, 800, 0, 800, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)

	gluLookAt(0, b_y, -1, 0, b_y, 0, 0, 1, 0)


def createPlate():
	if plates == []:
		plates.append(Rec(800, 790, random.randint(400, 750), random.randint(0,300)))
	if plates[-1].top <= 650:
		plates.append(Rec(800, 790, random.randint(400, 800), random.randint(0,350)))

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
d_b_x = -3
start = False

def keypress(key, x, y):
	global b_x, b_y
	if key == b'w':
		b_y += 400
		start = True
	elif key == b's':
		b_y -= 10
	elif key == b'a':
		b_x -= 10
	elif key == b'd':
		b_x += 10
	glutPostRedisplay()
def draw():
	global s_x, s_y, plates, i , b_x, b_y
	init()
	glColor3f(1.0, 1.0, 1.0)
	stars()
	glLoadIdentity()
	glColor3f(1.0, 0, 0)
	# update the camera position to follow the ball
	gluLookAt(b_x, b_y, -1, b_x, b_y, 0, 0, 1, 0)
	glTranslatef(b_x, b_y, 0.0)  # move to center of the screen
	ball = Rec(20, 0, 20, 0)
	drawrec(ball, (b_x, b_y))
    # check for collisions with plates
	for plate in plates:
		if b_x >= plate.left and b_x <= plate.right and b_y >= plate.bottom and b_y <= plate.top:
				d_b_x = s_y
				break
		else:
			d_b_x = -3
	if b_y > 0:
		b_y += d_b_x
	glutSwapBuffers()

def main():
	glutInit()
	glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
	glutInitWindowSize(800, 800)
	glutInitWindowPosition(100, 100)
	glutCreateWindow("OpenGL - First window demo")
	glutDisplayFunc(draw)
	glutKeyboardFunc(keypress)
	glutIdleFunc(draw)
	glutMainLoop()

main()