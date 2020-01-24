#finds the best Xvel and Yvel For enemies 
#givin Cordinates PlayerX,Y and enemyX,Y


#find if something can fall from 0 to 600
#to do that see if one specific point is enclosed

def returnValues(boundaries,target_X,target_Y,current_X,current_Y,max_speed,maxJumpDistance,maxJumpHeight):

	ObjectState = 'Standing' #what it is doing currently, Falling,Standing
	ReturnableXvel = 0
	ReturnableYvel = 0

	#IF positioned over a line, and greater than that line, then object state changes to falling
	#if on a line then objectState changes to Standing

	#If can get to enemy by going in it's direction, then go in that direction by adding to the Xvel
	#If blocked then look for a way going the other direction # don't worry about this rn though.

	#see if there is a way jumping of the nearest platform


	#Xvel logic
	if target_X < current_X:
		ReturnableXvel = -max_speed
	elif target_X > current_X:
		ReturnableXvel = max_speed

	#Yvel logic
	if target_Y > current_Y:
		ReturnableYvel = max_speed/2
	elif target_Y < current_Y:
		ReturnableYvel = - max_speed/2

	return(ReturnableXvel,ReturnableYvel)
