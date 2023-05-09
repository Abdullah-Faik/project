from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import math

j = False


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


coins = []
plates = []
stair_step_x = 2  # moving plates in x direction


def createPlate():
    if plates == []:
        x = random.randint(0, 600)
        right = (random.randint(100, 200)) + x
        left = x
        top = 100
        bottom = 90
        rec = Rec(top, bottom, right, left)
        plates.append(rec)

    if plates[-1].top <= frastom_top - 100:
        x = random.randint(0, 600)
        right = (random.randint(100, 200)) + x
        left = x
        top = plates[-1].top + 100
        bottom = plates[-1].bottom + 100
        rec = Rec(top, bottom, right, left)
        plates.append(rec)


def drawText(string, x, y):
    glLineWidth(2)
    glColor(1, 1, 0)  # Yellow Color
    glLoadIdentity()  # remove the previous transformations
    # glScale(0.13,0.13,1)  # Try this line
    glTranslate(x, y, 0)  # try comment this line
    glScale(0.13, 0.13, 1)
    string = string.encode()  # conversion from Unicode string to byte string
    glutStrokeString(GLUT_STROKE_ROMAN, string)  # Stroke font


def stairs():
    global plates, stair_step_x, coins
    createPlate()
    for i in range(0, len(plates), 1):
        plates[i].right += stair_step_x * plates[i].direction
        plates[i].left += stair_step_x * plates[i].direction
        if plates[i].right >= 800:
            plates[i].direction = -1
        elif plates[i].left <= 0:
            plates[i].direction = 1
        drawrec(plates[i])


dtime = .1
ball_y_velocity = 0
ball_x_velocity = 0
ball_dir_y = -1
land = False
jumping = 20
ball = Rec(0, 20, 510, 490)
increaseF = 0
increaseY = 0


# def falling(ball):
# 	global ball_dir_y , ball_y_velocity , land , jumping
# 	ball_y_velocity = 0
# 	if ball.bottom > frastom_bottom:
# 		jumping -= 9.8 * dtime
# 		ball_dir_y += jumping
# 		ball.bottom += ball_dir_y
# 		ball.top += ball_dir_y
# 		land = False
def moving_ball(ball):
    global ball_dir_y, ball_y_velocity, jumping, land, increaseF, increaseY, factor, ball_x_velocity, j
    ball_x_velocity = 0
    on_plate = False
    if increaseF:
        factor += 1
    else:
        factor = 2

    if increaseY:
        factY = factor
    else:
        factY = 0

    if keystates[1]:
        if ball.right <= 800:
            ball_x_velocity += factor * 0.25
    if keystates[0]:
        if ball.left >= 0:
            ball_x_velocity -= factor * 0.25
    if not on_plate:
        if keystates[2] and not j:
            ball_y_velocity = 6
            j = False
        else:
            ball_y_velocity -= 9.8 * dtime
        ball.bottom += ball_y_velocity * dtime
        ball.top = ball.bottom + 20
        ball_dir_y = -1
        land = True
    else:
        ball_y_velocity = 0

    ball.left += ball_x_velocity
    ball.right += ball_x_velocity

    if ball.bottom < frastom_bottom:
        ball.bottom = frastom_bottom
        ball.top = frastom_bottom + 20
        ball_y_velocity = max(0, ball_y_velocity)
        jumping = 20
        land = True
        j = False
def create_ball(ball):
    global ball_dir_y, ball_x_velocity, ball_y_velocity, land, jumping, j
    print(ball_dir_y, ball_y_velocity)
    for plate in plates:
        if ball.left + 10 >= plate.left and ball.right - 10 <= plate.right and ball.bottom <= plate.top and ball.bottom >= plate.bottom:
            ball.bottom += (plate.top - ball.bottom)
            ball.top = ball.bottom + 20
            ball.left += stair_step_x * plate.direction
            ball.right += stair_step_x * plate.direction
            ball_y_velocity = 0
            jumping = 20
            land = True
            j = False
            break
        elif (((plate.left <= ball.right and plate.right > ball.right) or
               (plate.right >= ball.left and plate.left < ball.left)) and
              plate.top <= ball.top and plate.bottom >= ball.bottom):
            plate.direction = -1 * plate.direction

    drawrec(ball)


frastom_top = 800
frastom_bottom = 0
frastom_y = 1


def init():
    global frastom_top, frastom_bottom, frastom_y
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
    glOrtho(0, 800, frastom_bottom, frastom_top, -1.0, 1.0)  # left, right, bottom, top, near, far
    glMatrixMode(GL_MODELVIEW)


increaseF = False
srart = False
keystates = [False, False, False, False]
factor = 1


def keypress(key, x, y):
    global srart, key_pressed, ball, land, keystates, increaseF, increaseY, j
    global land
    if ball.left > 0:  # to detect the windo
        if key == GLUT_KEY_LEFT:
            keystates[0] = True
    if ball.right < 800:  # to detect the windo
        if key == GLUT_KEY_RIGHT:
            keystates[1] = True
    if keystates[0] == True or keystates[1] == True:
        increaseF = True
    if key == GLUT_KEY_UP:
        keystates[2] = True
        j = True
    if key == GLUT_KEY_DOWN:  # remove this
        ball.top -= 30
        ball.bottom -= 30
    glutPostRedisplay()


def reset_keys(key, x, y):
    global keystates, increaseF, factor, ball_x_velocity, increaseY
    keystates = [False, False, False, False]
    increaseF = False
    glutPostRedisplay()


def draw():
    init()
    glColor3f(1.0, 1.0, 1.0)
    stairs()
    glLoadIdentity()
    moving_ball(ball)
    create_ball(ball)
    print(factor, increaseF)
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
    glutCreateWindow(b"OpenGL - First window demo")
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    glutKeyboardFunc(keypress)
    glutSpecialFunc(keypress)
    glutSpecialUpFunc(reset_keys)
    glutMainLoop()


main()
