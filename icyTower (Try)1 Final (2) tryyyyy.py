from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import random
import sys
from PIL import Image
from PIL.Image import *
# -------------------------------------------------

WINDOW_WIDTH = 600
WINDOW_HEIGHT = 800
windowBottom = 0
texNum = 7
barrier_width = 150   # we will make it random between range if we want
barrier_hieght = 30
dTime = 0.2
j = False 
iyVelocity = 60
yVelocity = iyVelocity
onBar = False
time_interval = 10 # try  2,5,7 msec
gameStart = False
barLeft = 0
barRight = 0
barScore = 0
ig = 9.8
g = ig
highScore = 0
searchRng = 15
barsTopList = []
downBars = False
val = 0
valDecRatio = 0.2
barCount = 0
moveX = 0
factor = 2
gameOver = False

class RECTA:
    def __init__(self, left, bottom, right, top):
        self.left = left
        self.bottom = bottom
        self.right = right
        self.top = top

randList = []
for i in range(0, 100):   #used to random the posation of the plate(right posation) and  0 to 50 chnge the speed
    randList.append(random.randrange(0,10, 1))

wall = RECTA(0, 0, WINDOW_WIDTH, WINDOW_HEIGHT)
gameO = RECTA(50, 200, 550, 600)
icyPic = RECTA(0, 0, 600, 800)
startPlay = RECTA(150, 170, 450, 270)
exitGame = RECTA(150, 50, 450, 150)

moveX = 0
playerLeft = 200
playerRight = 250
playerBottom = 0
player = RECTA(playerLeft, playerBottom, playerRight, playerBottom + 60)  # initial position of the bats


# ixVelocity = 2
# xVelocity = ixVelocity

incs = False


# Initialization
def init():
    #height is varaing
    global windowBottom
    # glEnable(GL_TEXTURE_2D)
    glClearColor(0.0, 0.0, 0.0, 0)
    glClear(GL_COLOR_BUFFER_BIT)
    # glShadeModel(GL_SMOOTH)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0, 600, 0,800, 0.0000000000001, -1)  # l,r,b,t,n,f
    glMatrixMode(GL_MODELVIEW)
    # glLoadIdentity()  # not necessary
    # glEnable(GL_DEPTH_TEST)  # try this


# def reshape(w, h): #until now don't know
#         # WINDOW_WIDTH = w
#         # WINDOW_HEIGHT = h
#         # glViewport(0, 0, 600, 900)


moveWindow = False
def DrawRectangle(rect):
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def DrawPlayerRectangle(rect):
    glLoadIdentity()
    glColor4f(1, 1, 0, 1)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()

def DrawBackGRectangle(rect):
    glColor4f(0,0, 0, 0)
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()

def DrawGameOverRectangle(rect):
    glLoadIdentity()
    glColor4f(1, 0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def DrawIcyRectangle(rect):
    glColor4f(0, 0, 1, 0)
    glLoadIdentity()
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def DrawStartRectangle(rect):
    glLoadIdentity()
    glColor4f(0, 0, 0, 0)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()


def DrawExitRectangle(rect):
    glLoadIdentity()
    glColor4f(0, 1, 1, 0)
    glBegin(GL_QUADS)
    glVertex(rect.left, rect.bottom, 0)  # Left - Bottom
    glVertex(rect.right, rect.bottom, 0)
    glVertex(rect.right, rect.top, 0)
    glVertex(rect.left, rect.top, 0)
    glEnd()

# Key Board Messages
def keyboard(key, x, y):  #used for end and start the game onley
    global barScore, barBottom, barCount, valDecRatio, gameStart, downBars, gameOver

    if key == b"q":
        sys.exit(0)

    if gameStart == False:

        if key == b"s":
            gameStart = True
            downBars = False
            gameOver = False
        
        # if key == b"r":
        #     randList.clear()
        #     for i in range(0, 100):
        #         randList.append(random.randrange(0, WINDOW_WIDTH - barrier_width, 1))
        #     barsTopList.clear()



            # barScore = 0
            # barBottom = 110
            # barCount = 0
            # valDecRatio = 0.2   # this is why the player flay  gletsh


def Timer(v):
    Display()
    glutTimerFunc(time_interval, Timer, 1)


increaseF = False
keystates = [] #l ,r,
for i in range(0,5):
    keystates.append(False)
def arrow_keys(key, x, y): #to make the bool true if you press on buttom
    global j
    global increaseF
    global keystates

    if gameStart:

        if player.left > 0: #to detect the windo
            if key == GLUT_KEY_LEFT:
                keystates[0] = True

        if player.right < WINDOW_WIDTH: #to detect the windo
            if key == GLUT_KEY_RIGHT:
                keystates[1] = True
                
        if keystates[0] == True or keystates[1] == True:
            increaseF = True
            
        if key == GLUT_KEY_UP:
            keystates[2] = True
            j = True


def keys_up(key,x,y):    #use to get the list of bool  false agine
    global keystates
    global increaseF
    keystates = [False,False,False,False,False]
    increaseF = False

def jump():
    global yVelocity, playerBottom, j, player, onBar, barLeft, barRight, barsTopList, barCount, barScore, g, dTime, highScore

    onBar = False
    if player.bottom > 220:
        yVelocity -= 2*valDecRatio
    # if factor >= 30 or factor <= -30:
    #     g = 2
    #     dTime = 0.3
    else:
        g = ig
        dTime = 0.2
    yVelocity -= g * dTime
    playerBottom += yVelocity * dTime

    for i in range(barCount, barCount+10):  # من الاخر بيبص علي البلطات اللي علي الشاشه لو واقع عليها او هيقع عليها (عدد البلاط مش هيعدي 10 في الشاشه  )
        if yVelocity < 0:
            if player.bottom >=barsTopList[i] and (player.left <= (randList[i] + barrier_width) and player.right >= randList[i]):
                if playerBottom <= barsTopList[i]:
                    playerBottom = barsTopList[i]
                    onBar = True
                    barScore = (i + 1) * 5
                    print(barScore)
                    barLeft = randList[i]
                    barRight = randList[i] + barrier_width
                    yVelocity = iyVelocity
                    j = False
    print(yVelocity,playerBottom,keystates[2])
    if highScore < barScore: #for inceres the score
        highScore = barScore


    if playerBottom <= 0:  # for make the player not fall dwon if he didn't jump on the frist plat
        playerBottom = 0
        yVelocity = iyVelocity
        j = False
    barsTopList.clear() # important for dropping down the Barriers




def Display():
    global playerLeft,playerRight,playerBottom,player,j,moveWindow,windowBottom,barsTopList,onBar,yVelocity
    global barLeft,barRight,downBars,val,valDecRatio,barCount,moveX,incMoveXR,incMoveXL,factor,gameStart
    global randList,restartGame,gameOver,highScore

    barBottom = 110

    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    # glMatrixMode(GL_MODELVIEW)
    glColor(1, 0, 1)  # White color
    glLoadIdentity()
    DrawBackGRectangle(wall)

    if gameOver:
        DrawGameOverRectangle(gameO)

    if gameStart == False and gameOver == False:
        DrawIcyRectangle(icyPic)
        DrawStartRectangle(startPlay)
        DrawExitRectangle(exitGame)
    
    if gameStart:
        for i in range(0, randList.__len__()):
            left = randList[i]  #to know the left posation from the random in lest
            barrier = RECTA(left, barBottom, left + barrier_width, barBottom + barrier_hieght) #l b r t to creat object of plate
            if downBars: # drop down the Barriers ## to game over
                if player.bottom <= 0:
                    val = 0
                    gameStart = False
                    gameOver = True
            barrier.bottom -= val
            barrier.top -= val
            if barsTopList.__len__() < randList.__len__():
                barsTopList.append(barrier.top)
            glColor(1, 0, 1)
            DrawRectangle(barrier)
            barBottom += 110

        if onBar:  # When out of bar left and right edges  # detect when fall down
            if player.left > barRight or player.right < barLeft:
                playerBottom -= 9
                for i in range(barCount, barCount+searchRng):
                    if player.bottom >= barsTopList[i] and (player.left <= (randList[i] + barrier_width) and player.right >= randList[i]):
                        if playerBottom <= barsTopList[i]:
                            playerBottom = barsTopList[i]
                if playerBottom <= 0:
                    playerBottom = 0


    # drop down the Barriers
        if player.top >= barsTopList[1]:
            val += valDecRatio
            if player.top >= (0.9*WINDOW_HEIGHT):
                val += 3
        if val != 0: #for game over
            downBars = True
            if onBar and player.top >= barsTopList[1]:
                playerBottom -= valDecRatio
                for i in range(0,barsTopList.__len__()):
                    if barsTopList[i] < 0:
                        if i > barCount:
                            barCount = i
                            print(barCount)
                            if (barCount % 3) == 0:
                                valDecRatio *= 1.25
                                print(valDecRatio)
                barsTopList.clear()


        score = "Score"
        Text(score,20,640)
        scoreNum = str(barScore)
        Text(scoreNum,50,600)

        HighScore = "High Score"
        Text(HighScore,20,710)
        HighScoreNum = str(highScore)
        Text(HighScoreNum,50,670)
        
        if j:
            jump()

        if increaseF:
            factor += 1
        else:
            factor = 2

        if keystates[1]:
            if player.right < WINDOW_WIDTH:
                moveX += factor 
        
        if keystates[0]:
            if player.left > 0:
                moveX -= factor
    
        glLoadIdentity()
        DrawPlayerRectangle(player)
        player = RECTA(playerLeft + moveX, playerBottom, playerRight + moveX, playerBottom + 60)

    
    
    glutSwapBuffers()
def Text(string ,x,y):
    glLineWidth(3)
    glColor(1,1,1)
    glLoadIdentity()
    glTranslate(x,y,0)
    glScale(0.19,0.19,1)
    string = string.encode()
    for c in string:
        glutStrokeCharacter(GLUT_STROKE_ROMAN,c)
        
def main():
    glutInit()
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB)
    glutInitWindowSize(WINDOW_WIDTH, WINDOW_HEIGHT)
    glutInitWindowPosition(0, 0)
    glutCreateWindow(b"Egyptian Icy Tower :D");
    glutDisplayFunc(Display)
    # glutReshapeFunc(reshape)
    glutTimerFunc(time_interval, Timer, 1)
    glutKeyboardFunc(keyboard)
    glutSpecialFunc(arrow_keys)
    glutSpecialUpFunc(keys_up)
    init()
    glutMainLoop()
main()
