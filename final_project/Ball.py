from rec import *
import Global
ball = Rec(20, 0 ,510, 490)
def player_mover_x(player):
	# x movemet
	ball_x_velocity = 0 # need to be تتفهم 
	if Global.increaseF == True: # if the kay being pressed 
		Global.factor += 1
	else:
		Global.factor = 1

	if Global.keystates[0] == True or Global.keystates[1] == True : # LEFT OR right 
		Global.ball_x_velocity += Global.factor * 0.25 * Global.ball_dir_x
	
	player.left += ball_x_velocity
	player.right += ball_x_velocity


def player_mover_y(player):
	
	if Global.jumping == True:
		Global.ball_y_velocity = Global.moving_up 
		Global.moving_up -= 10 * Global.dtime
		if Global.moving_up <= 0:
			Global.jumping = False
		player.bottom += Global.ball_y_velocity
		player.top = player.bottom + 20

	if Global.jumping is False and Global.land == False:
		for plate in Global.plates:
			if (player.left + 10 >= plate.left and player.right - 10 <= plate.right 
			and player.bottom <= plate.top and player.bottom >= plate.bottom):
				player.bottom = plate.top
				player.top = player.bottom + 20
				player.left += Global.stair_step_x * plate.direction
				player.right += Global.stair_step_x * plate.direction
				Global.ball_y_velocity = 0
				Global.land = True 	#لو مش مهمه اسمح
				break
			elif (((plate.left <= player.right and plate.right > player.right) or  
			(plate.right >= player.left and plate.left < player.left)) and
			plate.top <= player.top and plate.bottom >= player.bottom):
				plate.direction = -1 * plate.direction

		if Global.land == False and player.bottom > Global.frastom_bottom:
			Global.ball_y_velocity = Global.moving_down
			Global.moving_down += 10 * Global.dtime
			player.bottom -= Global.ball_y_velocity
			player.top = player.bottom + 20

#TODO: المفروض لما يطلع من برا الطبق يقع 

def player():
	global ball
	player_mover_x(ball)
	player_mover_y(ball)
	Global.ball.drawrec()
			
				






















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
