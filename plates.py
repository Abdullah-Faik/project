from rec import *
frastom_top = 800
frastom_bottom = 0
import random
plates = []
stair_step_x = 5 # moving plates	in x direction
stair_step_y = -1 # moving plates in y direction make them fall
def createPlate():
	global plates, plates_pos
	if plates == []:
		right = (random.randint(100, 200))
		x = random.randint(0, 800 - right)
		left= x
		right += x
		rec = Rec(150,140,left,right)
		plates.append(rec)

	if plates[-1].top <= frastom_top - 150:
		right = (random.randint(100, 200))
		x = random.randint(0, 800 - right)
		left= x
		right += x
		rec = Rec(150,140,left,right)
		plates.append(rec)

def stairs():
	global plates , stair_step_x, stair_step_y
	createPlate()
	for i in range(0,len(plates),1):
		drawrec(plates[i])
		# plates[i].top += stair_step_y 
		# plates[i].bottom += stair_step_y 
		plates[i].left += stair_step_x * plates[i].direction
		plates[i].right += stair_step_x * plates[i].direction
		if plates[i].right >= 800:
			plates[i].direction = -1
		elif plates[i].left <= 0:
		 	plates[i].direction = 1
		# if plates[i].top <= 0:
		# 	plates_pos.remove(plates_pos[i])
