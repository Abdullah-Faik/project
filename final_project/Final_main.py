from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random


class Rec:
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


def player_mover_x(player):  # x_movemet
    global factor, ball_x_velocity, ball_dir_x, increaseF, keystates

    ball_x_velocity = 0  # need to be تتفهم
    if increaseF:  # if the kay being pressed
        factor += 1
    else:
        factor = 1
    if keystates[0] == True and ball.left > 10:  # LEFT OR right
        ball_x_velocity += factor * 0.1 * ball_dir_x

    if keystates[1] == True and ball.right < 790:  # LEFT OR right
        ball_x_velocity += factor * 0.1 * ball_dir_x

    player.left += ball_x_velocity
    player.right += ball_x_velocity


def player_mover_y(player):  # y_movemet
    global frastom_top, frastom_bottom, dtime, ball_y_velocity, on_plate, jumping, moving_up, moving_down, plates, stair_step_x

    if jumping:
        ball_y_velocity = moving_up
        moving_up -= 10 * dtime
        if moving_up <= 0:
            jumping = False
        player.bottom += ball_y_velocity
        player.top = player.bottom + 20

    if jumping is False:
        for plate in plates:
            if (player.left + 10 >= plate.left and player.right - 10 <= plate.right
                    and plate.top >= player.bottom >= plate.bottom):
                ball_y_velocity = 0
                player.bottom = plate.top
                player.top = player.bottom + 20
                player.left += stair_step_x * plate.direction
                player.right += stair_step_x * plate.direction
                moving_up = 16
                on_plate = True
                moving_down = 0
                break
            elif (((plate.left <= player.right < plate.right) or
                   (plate.right >= player.left > plate.left)) and
                  plate.top <= player.top and plate.bottom >= player.bottom):
                plate.direction = -1 * plate.direction
            else:
                on_plate = False
        if player.bottom > frastom_bottom and on_plate == False:
            ball_y_velocity = moving_down
            moving_down += 1.85 * dtime
            player.bottom -= ball_y_velocity
            player.top = player.bottom + 20
    if ball.bottom <= frastom_bottom:
        ball.bottom = frastom_bottom
        ball.top = frastom_bottom + 20
        moving_up = 16
        moving_down = 0


def createPlate():
    if not plates:
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


def stairs():
    global plates, stair_step_x

    createPlate()
    for i in range(0, len(plates), 1):
        plates[i].right += stair_step_x * plates[i].direction
        plates[i].left += stair_step_x * plates[i].direction
        if plates[i].right >= 800:
            plates[i].direction = -1
        elif plates[i].left <= 0:
            plates[i].direction = 1
        plates[i].drawrec()


def player():
    global ball
    player_mover_x(ball)
    player_mover_y(ball)
    ball.drawrec()


def keypress(key, x, y):
    global ball_dir_x, jumping, increaseF, keystates

    if ball.left > 0:  # to detect the windo
        if key == GLUT_KEY_LEFT:
            ball_dir_x = -1
            keystates[0] = True
            increaseF = True

    if ball.right < 800:  # to detect the windo
        if key == GLUT_KEY_RIGHT:
            ball_dir_x = 1
            keystates[1] = True
            increaseF = True

    if key == GLUT_KEY_UP:
        keystates[2] = True
        jumping = True

    if key == GLUT_KEY_DOWN:  # TODO:remove
        ball.top -= 30
        ball.bottom -= 30
    glutPostRedisplay()


def reset_keys(key, x, y):
    global increaseF, keystates

    keystates = [False, False, False, False]
    increaseF = False
    glutPostRedisplay()  # to redraw the scene


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
    glOrtho(0, 800, frastom_bottom, frastom_top, -1.0, 1.0)  # left, right, bottom, top, near, far
    glMatrixMode(GL_MODELVIEW)


def draw():
    init()
    glColor3f(1.0, 1.0, 1.0)
    stairs()
    glColor(1, 0, 0)
    player()
    glLoadIdentity()
    glutSwapBuffers()


def game_timer(v):
    draw()
    glutTimerFunc(INTERVAL, game_timer, 1)


INTERVAL = 10

# frastom
frastom_top = 800
frastom_bottom = 0
g = 9.8

# ball
ball = Rec(20, 0, 510, 490)
factor = 1
dtime = .1
ball_y_velocity = 0
ball_x_velocity = 0
ball_dir_y = -1
ball_dir_x = 1
moving_up = 16
moving_down = 0
on_plate = False
jumping = False
increaseF = True

# keyboard
keystates = [False, False, False, False]

# plates
plates = []
stair_step_x = 2


def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(800, 800)
    glutInitWindowPosition(100, 10)
    glutCreateWindow(b"OpenGL - Working Ice Tower")
    glutDisplayFunc(draw)
    glutTimerFunc(INTERVAL, game_timer, 1)
    glutKeyboardFunc(keypress)
    glutSpecialFunc(keypress)
    glutSpecialUpFunc(reset_keys)
    glutMainLoop()


main()
