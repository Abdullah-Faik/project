from Rectangle import *
from random import randint
# import G

def createPlate():
	if G.plates == []:
		x = randint(0, 600)
		right = (randint(100, 200)) + x
		left= x
		top = 100
		bottom = 90
		rec = Rec(top,bottom,right,left)
		G.plates.append(rec)

	if G.plates[-1].top <= G.frastom_top - 100:
		x = randint(0, 600)
		right = (randint(100, 200)) + x
		left= x
		top = G.plates[-1].top + 100
		bottom = G.plates[-1].bottom + 100
		rec = Rec(top,bottom,right,left)
		G.plates.append(rec)
		
def stairs():
	createPlate()
	for i in range(0,len(G.plates),1):
		G.plates[i].right += G.stair_step_x * G.plates[i].direction
		G.plates[i].left += G.stair_step_x * G.plates[i].direction
		if G.plates[i].right >= 800:
			G.plates[i].direction = -1
		elif G.plates[i].left <= 0:
			G.plates[i].direction = 1
		G.plates[i].drawrec()
