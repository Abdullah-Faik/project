from rec import *
import random
import Global
def createPlate():
	if Global.plates == []:
		x = random.randint(0, 600)
		right = (random.randint(100, 200)) + x
		left= x
		top = 100
		bottom = 90
		rec = Rec(top,bottom,right,left)
		Global.plates.append(rec)

	if Global.plates[-1].top <= Global.frastom_top - 100:
		x = random.randint(0, 600)
		right = (random.randint(100, 200)) + x
		left= x
		top = Global.plates[-1].top + 100
		bottom = Global.plates[-1].bottom + 100
		rec = Rec(top,bottom,right,left)
		Global.plates.append(rec)
		
def stairs():
	createPlate()
	for i in range(0,len(Global.plates),1):
		Global.plates[i].right += Global.stair_step_x * Global.plates[i].direction
		Global.plates[i].left += Global.stair_step_x * Global.plates[i].direction
		if Global.plates[i].right >= 800:
			Global.plates[i].direction = -1
		elif Global.plates[i].left <= 0:
			Global.plates[i].direction = 1
		Global.plates[i].drawrec()
