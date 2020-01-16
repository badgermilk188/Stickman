import pygame
import random
from pygame import mixer


'''
starts out running away from police
doesn't make jump
has flashbacks

Has color - then if gets depressed turns dark

'''
pygame.init()


#All image and sound loads
icon = pygame.image.load ('sprites/icon.png')

#sprites-----------------
playerBlackLeft = pygame.image.load("sprites/playerblack-leftface.png")
playerBlackRight = pygame.image.load("sprites/playerblack-rightface.png")
playerColorLeft = pygame.image.load("sprites/playercolor-leftface.png")
playerColorRight = pygame.image.load("sprites/playercolor-rightface.png")

#backgrounds
cloud_1 = pygame.image.load("sprites/cloud1.png")
cloud_3 = pygame.image.load("sprites/cloud2.png")

sky_bg_1 = pygame.image.load("backgrounds/sky-background-1.png")
sky_bg_2 = pygame.image.load("backgrounds/sky-background-2.png")
black_bg_1 = pygame.image.load("backgrounds/background-black-1.png")
#pygame displays 
screen = pygame.display.set_mode((800,600))
#icon
pygame.display.set_icon(icon)

#all variables -----------------------------------------------


backgroundX = 0
playerCameraX = 100

running = True
scene = 1

playerX = 100
playerY = 50
playerSpeed = 4
playerXvel = 0
playerYvel = 0
playerGravity = .15
playerJumpHeight = 8
playerFace = 'Right' 	# Right or Left
playerState = 'Happy'  #Happy or Sad (depressed)
playerJumpState = 'Falling' #Standing, Jumping
playerFallingState = 'Falling' #falling , Standing
playerSadness = 0


#Scene boundries -----------------Lists of Tuples----------(X1,Y1,X2,Y2) (left to right , top to bottom)
scene_1_boundry = [(0,431,589,700),(802,485,1530,700)]   
scene_2_boundry = [(0,507,386,700),(540,0,1088,306),(542,499,1089,700),(1269,424,1990,700),(2300,419,2600,700),(2547,0,2600,700)]
#Display functions-----------------------------------------------------
def background(s):
	screen.blit(s,(backgroundX,0))

def boundry(scene_Boundry):
	global playerCameraX, playerX, playerJumpState, playerY, playerFallingState, playerYvel, playerXvel

	if playerCameraX <= 0:
		playerX = 0
		playerCameraX = 0


	for line in scene_Boundry:
		X1,Y1,X2,Y2 = line[0]-32,line[1]-64,line[2]-32,line[3]-64
		print (playerCameraX,X2,X1)		


		if playerCameraX > X1 and playerCameraX < X2 and playerY >Y1 and playerY < Y1+10: #standing on things
			
			playerY = Y1
			playerJumpState = 'Standing'
			playerFallingState = 'Standing'
			playerYvel = 0
		elif playerCameraX > X1 and playerCameraX < X2 and playerY>Y2 and playerY < Y2 -10: #bumping head on things
			playerY = Y2
			playerYvel = 0
		if playerY > Y1 and playerY < Y2 and playerCameraX <X2 and playerCameraX > X1 and playerXvel < 0: #left
			playerXvel = 0
		elif playerY > Y1 and playerY < Y2 and playerCameraX <X2 and playerCameraX > X1 and playerXvel > 0: #right
			playerXvel = 0
			

	if playerYvel < -10:
		playerYvel = -10
	if playerY > 620:
		death()



def blitPlayer():
	#player logic
	if playerFace is 'Right' and playerState is 'Happy':
		player = playerColorRight
	elif playerFace is 'Right' and playerState is 'Sad':
		player = playerBlackRight
	elif playerFace is 'Left' and playerState is 'Happy':
		player = playerColorLeft
	else:
		player = playerBlackLeft
	screen.blit(player,(playerX,playerY))
def cameraScroll(xmax,xmin = 0):
	global playerX, playerCameraX, playerXvel, playerSpeed, backgroundX

		
	if playerCameraX < xmin+368:
		playerX += playerXvel
		playerCameraX += playerXvel
		backgroundX = xmin

	elif playerCameraX >= xmin+368 and playerCameraX <= xmax-432:
		backgroundX -= playerXvel
		playerCameraX += playerXvel

	elif playerCameraX > xmax-432:
		playerCameraX += playerXvel
		playerX += playerXvel
		backgroundX = -xmax+800
def death():
	global playerY, playerState, playerSadness, playerSpeed

	if playerState is 'Sad':
		playerSpeed = playerSpeed*2
	playerY = 0
	playerState = 'Happy'
	playerSadness = 0
def set():
	global playerX,playerY, playerSpeed,playerXvel,playerYvel
	global playerGravity,playerJumpHeight,playerFace,playerState
	global playerFallingState,playerSadness, backgroundX, playerCameraX
	backgroundX = 0
	playerCameraX = 100
	playerX = 100
	playerY = 50
	playerSpeed = 4
	playerXvel = 0
	playerYvel = 0
	playerGravity = .15
	playerJumpHeight = 8
	playerFace = 'Right' 	# Right or Left
	playerState = 'Happy'  #Happy or Sad (depressed)
	playerJumpState = 'Falling' #Standing, Jumping
	playerFallingState = 'Falling' #falling , Standing
	playerSadness = 0

def win(condition,amount,condition2 = 'none',amount2 = 600): #condition is either X or Y
	global playerCameraX,playerY, scene

	if condition is 'X' and condition is 'none':
		if playerCameraX > amount:
			scene += 1
			set()

	elif condition is 'Y' and condition is 'none':
		if playerY > amount:
			scene += 1
			set()
	else:
		if playerCameraX > amount and playerY > amount2:
			scene += 1
			set()


#ALL SCENES -  ------------------------------------------

def scene_1():
	boundry(scene_1_boundry)
	background(sky_bg_1)
	blitPlayer()
	cameraScroll(1500)
	win('X',1500)


def scene_2():
	boundry(scene_2_boundry)
	background(sky_bg_2)
	blitPlayer()
	cameraScroll(2600)
#mainloop --  -----------------------------------------------------------
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				playerFace = 'Left'
				playerXvel -= playerSpeed
			if event.key == pygame.K_RIGHT:	
				playerFace = 'Right'
				playerXvel += playerSpeed
			if playerJumpState is 'Standing' and event.key == pygame.K_UP:
				playerJumpState = 'Jumping'
				playerYvel = playerJumpHeight
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerXvel = 0


	if playerJumpState is 'Jumping':
		playerYvel -= playerGravity
		if playerYvel >= playerJumpHeight:
			playerYvel = 0
			playerJumpState = 'Standing'

	playerSadness += .1
	if playerSadness > 100:
		if playerState is 'Happy':
			playerSpeed = playerSpeed/2
		playerState = 'Sad'

	if playerFallingState is 'Falling':
		playerYvel -= playerGravity
	elif playerFallingState is 'Standing':
		playerFallingState = 'Falling'


	if playerJumpState is 'Falling':
		playerFallingState = 'Falling'

	playerY -= int(playerYvel)

	if scene == 2:
		scene_2()
	elif scene == 1:
		scene_1()

	pygame.display.update()
