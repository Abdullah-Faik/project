from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Plates import *
class Rec():
	def __init__(self, t, b, r, l):
		self.top = t
		self.bottom = b
		self.right = r
		self.left = l
		self.direction = 1

	def drawrec(self):
		glLoadIdentity()
		glBegin(GL_QUADS)
		glVertex2f(self.left, self.bottom)
		glVertex2f(self.right, self.bottom)
		glVertex2f(self.right, self.top)
		glVertex2f(self.left, self.top)
		glEnd()
