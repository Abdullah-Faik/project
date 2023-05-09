import Global
from rec import Rec
def keypress(key, x, y):
	if Global.ball.left > 0: #to detect the windo
		if key == GLUT_KEY_LEFT:
			Global.ball_dir_x = -1
			Global.keystates[0] = True
			Global.increaseF = True

	if Global.ball.right < 800: #to detect the windo
		if key == GLUT_KEY_RIGHT:
			Global.ball_dir_x = 1
			Global.keystates[1] = True
			Global.increaseF = True

	if key == GLUT_KEY_UP:
		Global.keystates[2] = True
		Global.jumping = True

	if key == GLUT_KEY_DOWN:			 #TODO:remove 
		Global.ball.top -= 30
		Global.ball.bottom -= 30
	glutPostRedisplay()

def reset_keys(key,x,y):
	Global.keystates = [False, False, False, False]
	Global.increaseF = False
	glutPostRedisplay() # to redraw the scene
