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
#player Death sprites
death_right_1 = pygame.image.load('sprites/playerblack-rightface-death-1.png')
death_right_2 = pygame.image.load('sprites/playerblack-rightface-death-2.png')
death_right_3 = pygame.image.load('sprites/playerblack-rightface-death-3.png')
death_right_4 = pygame.image.load('sprites/playerblack-rightface-death-4.png')
death_right_5 = pygame.image.load('sprites/playerblack-rightface-death-5.png')
death_right_6 = pygame.image.load('sprites/playerblack-rightface-death-6.png')
death_right_7 = pygame.image.load('sprites/playerblack-rightface-death-7.png')
death_right_8 = pygame.image.load('sprites/playerblack-rightface-death-8.png')
death_right_9 = pygame.image.load('sprites/playerblack-rightface-death-9.png')
death_right_10 = pygame.image.load('sprites/playerblack-rightface-death-10.png')
death_right_11 = pygame.image.load('sprites/playerblack-rightface-death-11.png')
death_right_12 = pygame.image.load('sprites/playerblack-rightface-death-12.png')

#enemy sprites
enemy_black = pygame.image.load('sprites/enemy-black.png')
enemy_black_dead = pygame.image.load('sprites/enemy-black-dead.png')
#hands
hand_color = pygame.image.load('sprites/hand-color.png')
hand_black = pygame.image.load('sprites/hand-black.png')
gun_color_right = pygame.image.load('sprites/gun-color-right.png')
gun_color_left = pygame.image.load('sprites/gun-color-left.png')
casing_1 =pygame.image.load('sprites/casing-stage-1.png')
casing_2 =pygame.image.load('sprites/casing-stage-2.png')
casing_3 =pygame.image.load('sprites/casing-stage-3.png')
casing_4 =pygame.image.load('sprites/casing-stage-4.png')
casing = casing_1

#inventory
item = 'Fist'
itemList = ['Fist','Gun']
currentItem = 0
#backgrounds
cloud_1 = pygame.image.load("sprites/cloud1.png")
cloud_3 = pygame.image.load("sprites/cloud2.png")

sky_bg_1 = pygame.image.load("backgrounds/sky-background-1.png")
sky_bg_2 = pygame.image.load("backgrounds/sky-background-2.png")
black_bg_1 = pygame.image.load("backgrounds/background-black-1.png")
black_bg_2 = pygame.image.load('backgrounds/background-black-2.png')
news_bg_1 = pygame.image.load('backgrounds/background-news-1.png')
war_bg_1 = pygame.image.load('backgrounds/war-background-1.png')
#pygame displays 
screen = pygame.display.set_mode((800,600))
#icon
pygame.display.set_icon(icon)

#clock
clock = pygame.time.Clock()

#all variables -----------------------------------------------

time = 0
Start = True

collision = False
backgroundX = 0
playerCameraX = 100

running = True
scene = 1

playerX = 100
playerY = 50
playerSpeed = 6
playerXvel = 0
playerYvel = 0
playerGravity = .15
playerJumpHeight = 8
playerFace = 'Right' 	# Right or Left
playerState = 'Happy'  #Happy or Sad (depressed)
playerJumpState = 'Falling' #Standing, Jumping
playerFallingState = 'Falling' #falling , Standing
playerSadness = 0
playerSadSpeed = 4
playerStuckSad = False
#hads for player
playerHandPosition_X = 0
playerHandPosition_Y = 0
playerPunchStage = 0 # 0 - 16 depending on where it is.
handY = 30

#Gun 
GunCasingStage = 0 #0 - 4 depending
casingX = 0
casingY = 0

#bad guy variables
enemies = 0
enemyList = []
enemyPositionX = []
enemyPositionY = []
enemyXvel = []
enemyXminPositions = []
enemyXmaxPositions = []
enemyX = []
enemyXchange = []
enemySpeed = 2
enemyState = []
enemySprite = []

#bullet variables
bullets = 0
bulletXposition = []
bulletYposition = []
bulletXvel = []
bulletSpeed = 30

#death variables
deathCount = 0

#Scene boundries -----------------Lists of Tuples----------(X1,Y1,X2,Y2) (left to right , top to bottom)
scene_1_boundry = [(0,431,589,700),(802,485,1530,700)]   
scene_2_boundry = [(0,507,386,700),(540,0,1088,306),(542,499,1089,700),(1269,424,1990,700),(2300,419,2600,700),(2547,0,2600,700)]
scene_3_boundry = [(0,0,81,600),(0,548,2500,548),(584,0,1718,380)]
scene_4_boundry = [(0,557,1000,700),(452,279,480,371),(758,281,1000,700),(352,0,1000,279)]
scene_6_boundry = [(0,517,393,600),(393,587,1399,600),(1398,534,2068,600),(1494,474,1578,550),(1746,474,1837,550),(2208,530,2904,600),
					(2657,455,2767,535),(2897,452,3834,600),(2950,376,3112,455),(3275,301,3293,337),(3292,245,3662,275),(4034,543,4206,600),
					(4350,465,6100,600),(5499,0,6000,342)]
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
			
		if playerCameraX > X1 and playerCameraX < X2 and playerY >Y1 and playerY < Y1+15: #standing on things
			
			playerY = Y1
			playerJumpState = 'Standing'
			playerFallingState = 'Standing'
			playerYvel = 0
		#elif playerCameraX > X1 and playerCameraX < X2 and playerY<Y2 and playerY > Y2 -10: #bumping head on things
		#	playerY = Y2
		#	playerYvel = 0
		if playerY > Y1 and playerY < Y2 and playerCameraX <X2 and playerCameraX > X1 and playerXvel < 0: #left
			wallCollision()

		elif playerY > Y1 and playerY < Y2 and playerCameraX <X2 and playerCameraX > X1 and playerXvel > 0: #right
			wallCollision()
			

	if playerYvel < -10:
		playerYvel = -10
	if playerY > 620:
		death()

def blitPlayer():
	global playerHandPosition_X, playerHandPosition_Y,handY, playerPunchStage, casingY,casingX,GunCasingStage, casing
	#player logic and hand X logic
	if deathCount == 0:
		if playerFace is 'Right' and playerState is 'Happy':
			player = playerColorRight
			if item is 'Fist':
				hand = hand_color
			elif item is 'Gun':
				hand = gun_color_right
			playerHandPosition_X = playerX + 36
		elif playerFace is 'Right' and playerState is 'Sad':
			player = playerBlackRight
			if item is 'Fist':
				hand = hand_black
			elif item is 'Gun':
				hand = gun_color_right
			
			playerHandPosition_X = playerX + 36
		elif playerFace is 'Left' and playerState is 'Happy':
			player = playerColorLeft
			if item is 'Fist':
				hand = hand_color
			elif item is 'Gun':
				hand = gun_color_left
			playerHandPosition_X = playerX + 8
		else:
			player = playerBlackLeft
			if item is 'Fist':
				hand = hand_black
			elif item is 'Gun':
				hand = gun_color_left
			playerHandPosition_X = playerX + 8

		#hand Y logic
		
		if playerYvel > 0:
			if handY >21:
				handY -= 1
		elif playerYvel < playerGravity:
			if handY <31:
				handY += .5

		else:
			handY = 26
		# punch logic
		if item is 'Fist':
			if playerPunchStage > 0 and playerPunchStage <= 8:
				if playerFace is 'Left':
					playerHandPosition_X -= playerPunchStage*2
					playerPunchStage +=1
				if playerFace is 'Right':
					playerHandPosition_X += playerPunchStage*2
					playerPunchStage +=1
			if playerPunchStage > 8:
				if playerFace is 'Left':
					playerHandPosition_X += playerPunchStage
					playerPunchStage +=1
				if playerFace is 'Right':
					playerHandPosition_X -= playerPunchStage
					playerPunchStage +=1

				if playerPunchStage == 10:
					playerPunchStage = 0

		playerHandPosition_Y = playerY+handY
		#gun logic
		if item is 'Gun':
			casingX = playerHandPosition_X + 10
			casingY = playerHandPosition_Y
			if GunCasingStage  >0 and GunCasingStage <= 4:
				casing = casing_1
				GunCasingStage += 1

			elif GunCasingStage > 4 and GunCasingStage <=8:
				casing = casing_2
				GunCasingStage += 1
			elif GunCasingStage >8 and GunCasingStage <= 12:
				casing = casing_3
				GunCasingStage += 1
			elif GunCasingStage > 12 and GunCasingStage<=16:
				casing = casing_4
				GunCasingStage += 1
			
			if GunCasingStage > 16:
				GunCasingStage = 0
			if GunCasingStage > 10:
				casingY += GunCasingStage*1.5
			elif GunCasingStage < 8:
				casingY -= GunCasingStage*1.5
			else:
				casingY += GunCasingStage
			if playerFace is 'Right':
				casingX += GunCasingStage
			else:
				casingX -= GunCasingStage
		screen.blit(hand,(playerHandPosition_X,playerHandPosition_Y))
	elif deathCount > 0:
		player = suicide()
	screen.blit(player,(playerX,playerY))
	
	if GunCasingStage>0 and item is 'Gun':
		screen.blit(casing,(casingX,casingY))
def cameraScroll(xmax,xmin = 0):
	global playerX, playerCameraX, playerXvel, playerSpeed, backgroundX

		
	if playerCameraX <= xmin+368:
		playerX += playerXvel
		if playerX > 368:
			playerX = 368
		playerCameraX += playerXvel
		backgroundX = xmin
	elif playerCameraX > xmin+368 and playerCameraX < xmax-432:
		backgroundX -= playerXvel
		playerCameraX += playerXvel
		
			

	elif playerCameraX >= xmax-432:
		playerCameraX += playerXvel
		playerX += playerXvel
		if playerX < 368:
			playerX = 368
		backgroundX = -xmax+800


def death():
	global playerY, playerState, playerSadness, playerSpeed

	if playerState is 'Sad':
		playerSpeed = playerSpeed*2
	playerY = 0
	playerState = 'Happy'
	playerSadness = 0
def nextScene():
	global scene, Start
	scene += 1
	Start = True
def set():
	global playerX,playerY, playerXvel,playerYvel
	global playerFace,playerState,playerStuckSad
	global playerFallingState,playerSadness, backgroundX, playerCameraX
	global enemies, enemyList, enemyPositionX, enemyPositionY, enemyXvel,enemySprite
	global enemyXminPositions, enemyXmaxPositions, enemyX, enemyXchange, enemyState

	backgroundX = 0
	playerCameraX = 100
	playerX = 100
	playerY = 100
	playerSpeed = 6
	playerXvel = 0
	playerYvel = 0
	playerFace = 'Right' 	# Right or Left
	playerState = 'Happy'  #Happy or Sad (depressed)
	playerJumpState = 'Falling' #Standing, Jumping
	playerFallingState = 'Falling' #falling , Standing
	playerSadness = 0
	playerStuckSad = False
	enemies = 0
	enemyList = []
	enemyPositionX = []
	enemyPositionY = []
	enemyXvel = []
	enemyXminPositions = []
	enemyXmaxPositions = []
	enemyX = []
	enemyXchange = []
	enemyState = []
	enemySprite = []
	deathCount = 0 

def setPlayerPosition(x,y):
	global playerX, playerY, playerCameraX
	playerY = y
	playerX = x 
	playerCameraX = x

def suicide(): #140 frames?
	global deathCount
	deathCount += 1 
	returnSurface = death_right_1
	
	if deathCount > 0 and deathCount <= 10:
		returnSurface = death_right_1
	elif deathCount > 10 and deathCount <= 20:
		returnSurface = death_right_2
	elif deathCount> 20 and deathCount <= 30:
		returnSurface = death_right_3
	elif deathCount > 30 and deathCount <= 40:
		returnSurface = death_right_4
	elif deathCount > 40 and deathCount <= 50:
		returnSurface = death_right_5
	elif deathCount > 50 and deathCount <= 60:
		returnSurface = death_right_6
	elif deathCount > 60 and deathCount <= 70:
		returnSurface = death_right_7
	elif deathCount > 70 and deathCount <= 80:
		returnSurface = death_right_8
	elif deathCount > 80 and deathCount <= 90:
		returnSurface = death_right_9
	elif deathCount > 90 and deathCount <= 100:
		returnSurface = death_right_10
	elif deathCount > 100 and deathCount <= 110:
		returnSurface = death_right_11
	elif deathCount > 110:
		if deathCount >= 140:
			deathCount = 0
			death()
		returnSurface = death_right_12
	if playerFace is 'Left':
		return pygame.transform.flip(returnSurface,True,False)
	else:
		return returnSurface

def start():
	global Start
	if Start == True:
		Start = False
		return True



def createEnemy(x,y,paceX,paceX2):
	global enemies
	enemyPositionX.append(x)
	enemyX.append(x)
	enemyPositionY.append(y)
	enemyXvel.append(enemySpeed)
	enemyXminPositions.append(paceX)
	enemyXmaxPositions.append(paceX2)
	enemyXchange.append(0)
	enemyState.append('Alive')
	enemySprite.append(enemy_black)
	enemies+= 1

def blitEnemy():
	for i in range(enemies):
		screen.blit(enemySprite[i],(enemyX[i],enemyPositionY[i]))

def createBullet(x,y,direction):

	bulletXposition.append(x)
	bulletYposition.append(y)
	if direction is 'Left':
		bulletXvel.append(-bulletSpeed)	
	if direction is 'Right':
		bulletXvel.append(bulletSpeed)

def isCollision(hitbox_X,hitbox_Y, hitbox_X2, hitbox_Y2, objectX, objectY):

	if objectX >= hitbox_X and objectX <= hitbox_X2 and objectY >= hitbox_Y and objectY <= hitbox_Y2:
		return True


def wallCollision():
	global collision, playerXvel
	collision = True
	playerXvel = -playerXvel
def win(condition,amount,condition2 = 'none',amount2 = 600): #condition is either X or Y


	if condition is 'X' and condition2 is 'none':
		if playerCameraX > amount:
			return True

	elif condition is 'Y' and condition2 is 'none':
		if playerY > amount:
			return True
	else:
		if playerCameraX > amount and playerY > amount2:
			return True


#ALL SCENES -  ------------------------------------------

def scene_1():
	if start():
		set()
	boundry(scene_1_boundry)
	background(sky_bg_1)
	blitPlayer()
	cameraScroll(1500)
	if win('X',1500):
		nextScene()
		

def scene_2():
	if start():
		set()
		setPlayerPosition(15,430)
	boundry(scene_2_boundry)
	background(sky_bg_2)
	blitEnemy()
	blitPlayer()
	cameraScroll(2600)
	if win('X',1950,'Y',600):
		nextScene()
		
	
def scene_3():
	if start():
		set()
		createEnemy(1000,482,920,1080)
		global playerStuckSad
		playerStuckSad = True
	boundry(scene_3_boundry)
	background(black_bg_1)
	blitEnemy()
	blitPlayer() 
	cameraScroll(2400)
	if win('X',2400):
		nextScene()
		
def scene_4():
	if start():
		set()
		createEnemy(380,490,330,430)
		global playerStuckSad
		playerStuckSad = True
	boundry(scene_4_boundry)
	background(black_bg_2)
	blitEnemy()
	blitPlayer()
	cameraScroll(1000)
	if deathCount == 139:
		nextScene()
def scene_5():
	global time
	#use time variable here to 3600 or something 
	if start():
		set()
	background(news_bg_1)
	time += 1
	if time == 800:
		time = 0
		nextScene()
def scene_6():
	if start():
		set()
	boundry(scene_6_boundry)
	background(war_bg_1)
	blitPlayer()
	cameraScroll(6000)

#mainloop --  -----------------------------------------------------------
while running:

	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False
		if event.type == pygame.KEYDOWN:
			if deathCount == 0:
				if event.key == pygame.K_LEFT or event.key == pygame.K_a:
					playerFace = 'Left'
					playerXvel = -playerSpeed
				if event.key == pygame.K_RIGHT or event.key == pygame.K_d:	
					playerFace = 'Right'
					playerXvel = playerSpeed
				if playerJumpState is 'Standing' and event.key == pygame.K_UP or playerJumpState is 'Standing' and event.key == pygame.K_w :
					playerJumpState = 'Jumping'
					playerYvel = playerJumpHeight
				if playerPunchStage == 0 and event.key== pygame.K_SPACE:
					if item =='Fist':
						playerPunchStage = 1
					elif item is 'Gun' and GunCasingStage ==0:
						GunCasingStage = 1 
						bullets+= 1
						createBullet(playerX,playerY,playerFace)
				if event.key == pygame.K_q:
					if currentItem < len(itemList)-1:
						currentItem += 1
					else:
						currentItem = 0
					item = itemList[currentItem]
				if event.key == pygame.K_r:
					if playerState is 'Sad':
						deathCount = 1
		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT or event.key == pygame.K_a or event.key == pygame.K_d:
				playerXvel = 0


	if playerJumpState is 'Jumping':
		playerYvel -= playerGravity
		if playerYvel >= playerJumpHeight:
			playerYvel = 0
			playerJumpState = 'Standing'
	if playerStuckSad:
		playerState = 'Sad'
		playerSpeed = playerSadSpeed
	else:
		playerSadness += .1
		if playerSadness > 100:
			if playerState is 'Happy':
				playerSpeed = playerSadSpeed
				playerXvel = 0
			playerState = 'Sad'


	if playerFallingState is 'Falling':
		playerYvel -= playerGravity
	elif playerFallingState is 'Standing':
		playerFallingState = 'Falling'


	if playerJumpState is 'Falling':
		playerFallingState = 'Falling'
	if collision:
		playerXvel = 0
		collision = False
	playerY -= int(playerYvel)
	#bullet logic
	removeBullets = 0
	for i in range(bullets):
		bulletXposition[i] += bulletXvel[i]

	if bullets > 0:
		if bulletXposition[0] >8000 or bulletXposition[0] < -100:
			bulletXposition.pop(0)
			bulletYposition.pop(0)
			bulletXvel.pop(0)
			removeBullets += 1
		bullets -= removeBullets
	# enemy logic
	for i in range(enemies):
		if enemyState[i] is 'Alive':
			enemyXmin = enemyXminPositions[i]
			enemyXmax = enemyXmaxPositions[i]
			
			enemyX[i] = enemyPositionX[i]+ backgroundX 
			enemyX[i] += enemyXchange[i]
			enemyXchange[i] += enemyXvel[i]

			if enemyPositionX[i] + enemyXchange[i] > enemyXmax:
				enemyXvel[i] = -enemySpeed
			elif enemyPositionX[i] + enemyXchange[i] <enemyXmin:
				enemyXvel[i] = enemySpeed 

			#enemy hitboxes
			X1,X2,Y1,Y2 = enemyX[i]-32,enemyX[i]+32,enemyPositionY[i],enemyPositionY[i]+64
			#bullet collision
			for x in range(bullets):
				if isCollision(X1,Y1,X2,Y2,bulletXposition[x],bulletYposition[x]):
					
					#bulletXposition[x] <= X2 and bulletXposition[x] >= X1 and bulletYposition[x] >= Y1 and bulletYposition[x] <= Y2 or 
					enemyState[i] = 'Dead'
			#player kill collisions
			if playerX > X1 and playerX < X2 and playerY > Y1 and playerY < Y2:
				death()

		elif enemyState[i] is 'Dead':
			enemySprite[i] = enemy_black_dead
			enemyX[i] = enemyPositionX[i] + backgroundX


	if scene == 1:
		scene_1()
	elif scene == 2:
		scene_2()
	elif scene == 3:
		scene_3()
	elif scene == 4:
		scene_4()
	elif scene == 5:
		scene_5()
	elif scene == 6:
		scene_6()

	pygame.display.update()
	clock.tick(60)
