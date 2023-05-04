from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import random
s_t = 800
s_b = 0
frastom_top = 800
frastom_bottom = 0

"""class
class Rec(object):
@description: This class is used to create a rectangle
@attributes: top, bottom, right, left, direction
@methods: __init__
"""

class Rec(object):
	def __init__(self, t, b, r, l):
		self.top = t
		self.bottom = b
		self.right = r
		self.left = l
		self.direction = 1
e_x = 0
y_e_c  = 0
e_z = 0
c_x = 0
c_z = -1
def look_at():
    global e_x, y_e_c, e_z, c_x, c_z
    gluLookAt(
	e_x, y_e_c, e_z,    #eye
	c_x, y_e_c, c_z,    #center
	0, 1, 0                #up
    )
"""drawrec(rec, pos):
@description: This function is used to draw a ree_x = 0
y_e_c  = 0
e_z = 1
c_x = 0
c_z = 0ctangle
@attributes: rec, pos
@rec: a rectangle
@pos: position of the rectangle
@methods: drawrec
"""
def drawrec(rec, pos):
	glLoadIdentity()
	look_at()
	glTranslatef(pos[0], pos[1], 0.0)
	glBegin(GL_QUADS)
	glVertex2f(rec.left, rec.bottom)
	glVertex2f(rec.right, rec.bottom)
	glVertex2f(rec.right, rec.top)
	glVertex2f(rec.left, rec.top)
	glEnd()


""" init():
@description: This function is used to initialize the screen
@attributes: s_t, s_b, frastom_top, frastom_bottom, f_y
@frastom_top: frastom top 
@frastom_bottom: frastom bottom
@f_y: frastom  movemwnt in direction y 
@methods: init
"""
def init():
	global frastom_top, frastom_bottom, f_y
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	# frastom_bottom += 2
	# frastom_top += 2
	glOrtho(0, 800,frastom_bottom ,frastom_top, -1.0, 1.0) # left, right, bottom, top, near, far
	glMatrixMode(GL_MODELVIEW)



#the camera look at parameters
"""createPlate():
@description: This function is used to draw the frastom
@attributes: plates, plates_pos,
@plates: list of plates
@plates_pos: list of plates positions
"""
def createPlate():
	global plates, plates_pos
	if plates == []:	
		plates.append(Rec(150,140, min(random.randint(400, 750),450), max(random.randint(0,300), 250)))
		plates_pos.append(random.randint(-400 + (plates[-1].right - plates[-1].left) // 2,400 - (plates[-1].right - plates[-1].left) // 2))
	if plates[-1].top <= frastom_top:
		plates.append(Rec(plates[-1].top + 150 ,plates[-1].bottom + 150 ,min(random.randint(400, 750),450), max(random.randint(0,300), 250)))
		print("---",frastom_top)
		plates_pos.append(random.randint(int(-400 +(plates[-1].right - plates[-1].left) / 2),int (400 - (plates[-1].right - plates[-1].left) / 2)))


"""stairs
@description: This function is used to draw the plates and create new plate
and it's responsible for the movement of the plates in x direction
"""
def stairs():
	global plates 
	createPlate()
	for i in range(0,len(plates),1):
		drawrec(plates[i], (plates_pos[i],0))
		# plates[i].top += s_y
		# plates[i].bottom += s_y
		plates[i].left += s_x * plates[i].direction
		plates[i].right += s_x * plates[i].direction
		if plates[i].right + plates_pos[i] >= 800:
			plates[i].direction = -1
		elif plates[i].left + plates_pos[i] <= 0:
			plates[i].direction = 1
		#if plates[i].top <= 0:
			# plates.remove(plates[i])
			# plates_pos.remove(plates_pos[i])


s_x = 5 # moving plates	in x direction
s_y = -1 # moving plates in y direction make them fall
b_x = 400 # ball x position in the middle of the screen when 
b_y = 0 # ball y position in the middle of the screen when
plates = [] # list of plates
plates_pos = [] # list of plates positions
i = 0 # index of plates
d_b_y = -10 # ball y direction
d_b_x = -10 # ball x direction
start = False # start game
f_y = 0 # falling y


"""keypress(key):
@description: This function is responsible for the movement of the ball using the keyboard
@attributes:key, b_x, b_y, d_b_x, d_b_y
@key: key pressed
"""
def keypress(key, x, y):
	global b_x, b_y
	if key == GLUT_KEY_UP and b_y <= frastom_top - 200:
		b_y += 200
	elif key == GLUT_KEY_RIGHT and b_x <= s_t - 30:
		b_x -= d_b_x
	elif key == GLUT_KEY_LEFT and b_x > 0:
		b_x += d_b_x
	elif key == GLUT_KEY_DOWN:
		b_y -= 100
	glutPostRedisplay() # this function is used to redraw the screen after any event like moving the ball


def draw():
	global s_x, s_y, plates, i , b_x, b_y , d_b_y, d_b_x , start, allower , f_y , y_e_c , frastom_top , frastom_bottom
	init()
	glColor3f(1.0, 1.0, 1.0)
	stairs()
	glLoadIdentity()
	look_at()
	glColor3f(1.0, 0, 0)
	glTranslatef(b_x, frastom_bottom, 0.0)  # move to center of the screen
	ball = Rec(20, 0, 20, 0)
	drawrec(ball, (b_x, b_y))
	print(frastom_top,"--", y_e_c)
	for i in range(0,len(plates),1):
		if b_x + 10 >= (plates[i].left + plates_pos[i]) and (b_x + 10 <= plates[i].right + plates_pos[i] ) and b_y >= plates[i].bottom and b_y <= plates[i].top:
				b_y += plates[i].top - b_y
				d_b_y = s_y
				b_x += s_x * plates[i].direction
				allower = 1
				break
		else:
			d_b_y = -5
	if b_y - frastom_bottom > 0:
		b_y += d_b_y
	else :
		b_y = frastom_bottom
	f_y += 1
	y_e_c += 5

	if y_e_c >= 400:
		frastom_top += 5
		frastom_bottom += 5
	glutSwapBuffers()


INTERVAL = 100
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

