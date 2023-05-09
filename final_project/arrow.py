from Rectangle import *

def keypress(key, x, y):
	if G.ball.left > 0: #to detect the windo
		if key == GLUT_KEY_LEFT:
			G.ball_dir_x = -1
			G.keystates[0] = True
			G.increaseF = True

	if G.ball.right < 800: #to detect the windo
		if key == GLUT_KEY_RIGHT:
			G.ball_dir_x = 1
			G.keystates[1] = True
			G.increaseF = True

	if key == GLUT_KEY_UP:
		G.keystates[2] = True
		G.jumping = True

	if key == GLUT_KEY_DOWN:			 #TODO:remove 
		G.ball.top -= 30
		G.ball.bottom -= 30
	glutPostRedisplay()

def reset_keys(key,x,y):
	G.keystates = [False, False, False, False]
	G.increaseF = False
	glutPostRedisplay() # to redraw the scene
