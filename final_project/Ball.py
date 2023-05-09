from Rectangle import *
# import G as G

G.ball = Rec(20, 0 ,510, 490)

def player_mover_x(player):
	# x movemet
	G.ball_x_velocity = 0 # need to be تتفهم 
	if G.increaseF == True: # if the kay being pressed 
		G.factor += 1
	else:
		G.factor = 1

	if G.keystates[0] == True and  player.left > 10: # LEFT OR right 
			G.ball_x_velocity += G.factor * 0.1 * G.ball_dir_x

	if G.keystates[1] == True and player.right < 790:# LEFT OR right 
			G.ball_x_velocity += G.factor * 0.1 * G.ball_dir_x
	
	player.left +=G.ball_x_velocity
	player.right += G.ball_x_velocity


def player_mover_y(player):
	
	if G.jumping == True:
		G.ball_y_velocity = G.moving_up 
		G.moving_up -= 10 * G.dtime
		if G.moving_up <= 0:
			G.jumping = False
		player.bottom += G.ball_y_velocity
		player.top = player.bottom + 20

	if G.jumping is False :	#and G.land == False
		for plate in G.plates:
			if (player.left + 10 >= plate.left and player.right - 10 <= plate.right 
			and plate.top >= player.bottom >= plate.bottom):
				
				player.bottom = plate.top
				player.top = player.bottom + 20
				player.left += G.stair_step_x * plate.direction
				player.right += G.stair_step_x * plate.direction

				G.moving_up = 16
				G.moving_down = 0
				G.ball_y_velocity = 0
				G.on_plate = True 	#لو مش مهمه اسمح
				break
			elif (((plate.left <= player.right < plate.right) or
                   (plate.right >= player.left > plate.left)) and
                  plate.top <= player.top and plate.bottom >= player.bottom):
				plate.direction = -1 * plate.direction
			else:
				G.on_plate = False
		if player.bottom > G.frastom_bottom and G.on_plate == False:
			G.ball_y_velocity = G.moving_down
			G.moving_down += 1.85 * G.dtime 
			player.bottom -= G.ball_y_velocity
			player.top = player.bottom + 20
	if G.ball.bottom <= G.frastom_bottom:
		G.ball.bottom = G.frastom_bottom
		G.ball.top = G.frastom_bottom + 20
		G.moving_up = 16
		G.moving_down = 0

#TODO: المفروض لما يطلع من برا الطبق يقع 

def player():
	# global ball
	player_mover_x(G.ball)
	player_mover_y(G.ball)
	G.ball.drawrec()
			
				






















# def moving_ball_0(ball):
# 	ball_x_velocity = 0
# 	print(ball.bottom, "ball_!")
# 	if factor_increaser:
# 		factor += 1
# 	else:
# 		factor = 2

# 	if increaseY:
# 		factY = factor
# 	else:
# 		factY = 0

# 	if keystates[1]:
# 		if ball.right <= 800:
# 			ball_x_velocity += factor * 0.25
# 	if keystates[0]:
# 		if ball.left >= 0:
# 			ball_x_velocity -= factor * 0.25
# 	if j and not land:
# 		jumping -= 9.8 * dtime
# 		ball_y_velocity += jumping * dtime
	
# 	if ball.bottom < frastom_bottom:
# 		ball_y_velocity = 0
# 		land = True
# 		ball.bottom = frastom_bottom
# 		ball.top = frastom_bottom + 20
# 		jumping = 20
# 		j = False
# 	ball.bottom += ball_y_velocity
# 	ball.top = ball.bottom + 20
# 	ball.left += ball_x_velocity
# 	ball.right += ball_x_velocity
# 	print(jumping,keystates[2],j,ball.top)

# def create_ball(ball):
# 	for plate in plates:
# 		if ball.left + 10 >= plate.left and ball.right - 10 <= plate.right and ball.bottom <= plate.top and ball.bottom >= plate.bottom:
# 			ball.bottom += (plate.top - ball.bottom)
# 			ball.top = ball.bottom + 20
# 			ball.left += stair_step_x * plate.direction
# 			ball.right += stair_step_x * plate.direction
# 			ball_y_velocity = 0
# 			jumping=20
# 			land = True
# 			j = False
# 			break
# 		elif (((plate.left <= ball.right and plate.right > ball.right) or  
# 			(plate.right >= ball.left and plate.left < ball.left)) and
# 			plate.top <= ball.top and plate.bottom >= ball.bottom):
# 			plate.direction = -1 * plate.direction
# 	print(ball.top)
