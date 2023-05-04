from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import sys
import pygame
import random
s_t = 800
s_b = 0





direction=[0,1]
names=[0,1,2,3,4,5]
def texture_setup(texture_image_string, texture_name, width, height):
    glBindTexture(GL_TEXTURE_2D, texture_name)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_S, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_WRAP_T, GL_REPEAT)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MIN_FILTER, GL_NEAREST)
    glTexParameterf(GL_TEXTURE_2D, GL_TEXTURE_MAG_FILTER, GL_LINEAR)
    glTexImage2D(GL_TEXTURE_2D, 0, 3, width, height, 0, GL_RGBA, 
                GL_UNSIGNED_BYTE, texture_image_string)
    
man_path_array=['images/icyMan1.png','images/icyMan2.png','images/icyMan3.png']
man_path='images/icyMan.png'


def load_textures():

    global names,man_path
    glEnable(GL_TEXTURE_2D)
    images=[]
    textures=[]
    paths=["images/bk3.png","images/exitGame.png","images/gameover.png","images/icy2.png",man_path
	,'images/startPlay.png']

    for path in paths:
        images.append(pygame.image.load(path))
    
    for image in images:
        textures.append(pygame.image.tostring(image, "RGBA", True))
    
    glGenTextures(len(images),names)
    
    for i in range(len(images)):
        texture_setup(textures[i], names[i], images[i].get_width(), images[i].get_height())


def drawrec(rect,pos):
    glLoadIdentity()
    glTranslatef(pos[0], pos[1], 0.0)
    glBegin(GL_QUADS)
    glTexCoord2f(0, 0)
    glVertex2f(rect.left, rect.bottom)
    glTexCoord2f(1, 0)
    glVertex2f(rect.right, rect.bottom)
    glTexCoord2f(1, 1)
    glVertex2f(rect.right, rect.top)
    glTexCoord2f(0, 1)
    glVertex2f(rect.left, rect.top)
    glEnd()









class Rec(object):
	def __init__(self, t, b, r, l):
		self.top = t
		self.bottom = b
		self.right = r
		self.left = l
		self.direction = 1

wall=Rec(s_t + s_b,s_b,800,0)
gameo = Rec(600,200,550,200)
startplay = Rec(500,400,500,250)
exitgame = Rec(350,250,500,250)
ball = Rec(50, 0, 50, 0)
gamestart=False
gameover=False


def init():
	global s_t, s_b
	glClearColor(0.0, 0.0, 0.0, 0.0)
	glClear(GL_COLOR_BUFFER_BIT)
	glMatrixMode(GL_PROJECTION)
	glLoadIdentity()
	glOrtho(0, 800, s_b, s_t + s_b, -1.0, 1.0)
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
		glBindTexture(GL_TEXTURE_2D,names[3])
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
d_b_y = -5
d_b_x = 1
start = False

def keypress(key, x, y):
	global direction
	global b_x, b_y,gamestart,gameover,man_path_array,man_path
	if key == GLUT_KEY_UP:
		b_y += 200
		gamestart=True
		gameover=False
		man_path=man_path_array[0]

	elif key == GLUT_KEY_RIGHT:
		b_x += 10
		man_path=man_path_array[1]
		
	elif key == GLUT_KEY_LEFT:
		b_x -= 10
		man_path=man_path_array[2]
	
	manimg=pygame.image.load(man_path)
	stringimg=pygame.image.tostring(manimg,'RGBA',True)
	texture_setup(stringimg,names[4], manimg.get_width(),manimg.get_height())
def draw():
	global s_x, s_y, plates, i , b_x, b_y , d_b_y, d_b_x,gamestart,gameover
	init()
	glLoadIdentity()
	glTranslatef(b_x, b_y, 0.0)
	glBindTexture(GL_TEXTURE_2D,names[0])
	drawrec(wall,(0,0))
	if gameover:
		glBindTexture(GL_TEXTURE_2D,names[2])
		drawrec(gameo,(0,0))
	if gamestart==False and gameover==False:
		glBindTexture(GL_TEXTURE_2D,names[5])
		drawrec(startplay,(0,0))
		glBindTexture(GL_TEXTURE_2D,names[1])
		drawrec(exitgame,(0,0))
	if gamestart:
		stars()

		glBindTexture(GL_TEXTURE_2D,names[4])
		drawrec(ball, (b_x, b_y))
		
		for plate in plates:
			if b_x >= plate.left and b_x <= plate.right and b_y > plate.bottom and b_y <= plate.top:
				b_y += plate.top - b_y
				d_b_y = s_y
				b_x += s_x * plate.direction
				break
			else:
				d_b_x = -5
		if b_y > 0:
			b_y += d_b_x
		if b_y <=0:
			gameover=True
			gamestart=False
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
	load_textures()
	glutDisplayFunc(draw)
	glutTimerFunc(INTERVAL, game_timer, 1)
	glutKeyboardFunc(keypress)
	glutSpecialFunc(keypress)
	glutMainLoop()

main()