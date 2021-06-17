"""  Using Pygame and Learning It. Space Invader ---- Pygame """
import math
# importing pygame module
import pygame
import random
from pygame import mixer

# initialize the pygame
pygame.init()

# create the screen
# set_mode(width,height)
""" 
--------------------------------->
				800
								|
								|
								|
								|
							600	|
								|
								|
								|
								~
			370 -->375				
"""
screen = pygame.display.set_mode((800,600))


# Background 
background = pygame.image.load('background.png')



# Sound
mixer.music.load("background.wav")
mixer.music.play(-1)


""" Changing Title, logo & Background """
# label
pygame.display.set_caption("Space Invaders")



# logo image
icon = pygame.image.load('galaxy.png')
pygame.display.set_icon(icon)


# Player 
playerImg = pygame.image.load('player.png')
playerX = 370 #left to right  
playerY = 480 #top to bottom  #adding=bottom,#sub=top
playerX_change = 0


# Enemy 
enemyImg = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []

num_of_enemies = 6
for i in range(num_of_enemies):
	enemyImg.append(pygame.image.load('enemy.png'))
	enemyX.append(random.randint(0,735)) #left to right  
	enemyY.append(random.randint(50,150)) #top to bottom  #adding=bottom,#sub=top
	enemyX_change.append(2)
	enemyY_change.append(40)
 


# Bullet 
# "ready" can't see the bullet on screen 
#  "fire" bullet currently moving
bulletImg = pygame.image.load('bullet.png')
bulletX = 0 #left to right  
bulletY = 480 #top to bottom  #adding=bottom,#sub=top
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


# Score 
score_value = 0 
font = pygame.font.Font('freesansbold.ttf',32)
textX = 10
textY = 10 


def showScore(x, y):
	score = font.render("Score : " +str(score_value), True, (255,255,255))
	screen.blit(score, (x,y))

# Game over logic 
over_font = pygame.font.Font('freesansbold.ttf',64)
def game_over_text():
	over_text =over_font.render("GAME OVER", True, (255,255,255))
	screen.blit(over_text, (200,250))



# why creating func? -->
def player(x,y):
	""" blit(means to draw) is the process to render the game object onto the surface 
		It takes in 2 values(img,(co-ordinates))"""
	screen.blit(playerImg, (x, y))

def enemy(x,y):
	""" blit(means to draw) is the process to render the game object onto the surface 
		It takes in 2 values(img,(co-ordinates))"""
	screen.blit(enemyImg[i], (x, y))

def fireBullet(x,y):
	global bullet_state
	bullet_state = "fire"
	screen.blit(bulletImg, (x+16,y+10))

def inCollision(enemyX, enemyY, bulletX, bulletY):
	distance = math.sqrt(math.pow(enemyX-bulletX,2))+ (math.pow(enemyY-bulletY,2))
	if distance <27:
		return True 
	else:
		return False



# game loop
running = True
while running:
	""" setting up the screen so that everything comes above the screen later"""
	screen.fill((0,0,0))
	# background image 
	screen.blit(background, (0,0))


	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running=False


		# if keystroke is pressed check whether it's right or left 
		if event.type == pygame.KEYDOWN:
			print("Key Stroke has been pressed")
			if event.key == pygame.K_LEFT:
				playerX_change = -5
				print("Left arrow is being pressed")
			if event.key == pygame.K_RIGHT:
				playerX_change = 5
				print("Right arrow is being pressed")

			if event.key == pygame.K_SPACE:
				if bullet_state is "ready":
					bulletSound = mixer.Sound("laser.wav")
					bulletSound.play()
					bulletX = playerX
					fireBullet(bulletX, bulletY)

		if event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
				playerX_change = 0



	# Checking for boundaries for spaceship
	playerX +=playerX_change
	if playerX <=0 :
		playerX = 0 
	elif playerX>=736:
		playerX = 736



	# Checking for boundaries for enemy 
	for i in range(num_of_enemies):

		# game over logic
		if enemyY[i] >430:
			for j in range(num_of_enemies):
				enemyY[j] = 2000 
			game_over_text()
			break

		enemyX[i] +=enemyX_change[i]
		if enemyX[i] <=0 :
			enemyX_change[i] = 2
			enemyY[i] += enemyY_change[i]
		elif enemyX[i]>=736:
			enemyX_change[i] = -2
			enemyY[i]+=enemyY_change[i]

		# Collision 
		collision = inCollision(enemyX[i], enemyY[i],bulletX, bulletY)
		if collision:
			explosionSound = mixer.Sound("explosion.wav")
			explosionSound.play()
			bulletY = 480 
			bullet_state = "ready"
			score_value +=1
			print(score_value)
			enemyX[i] = random.randint(0,800) #left to right  
			enemyY[i] =  random.randint(50,150) #top to bottom  #adding=bottom,#sub=top

		enemy(enemyX[i], enemyY[i])


	# bullet movement 
	if bulletY<=0:
		bulletY = 480
		bullet_state = "ready"
	if bullet_state is "fire":
		fireBullet(bulletX, bulletY)
		bulletY -= bulletY_change


	


	# calling player inside the game loop because we want 
	# the player to be seen on screen.
	player(playerX, playerY)
	showScore(textX, textY)
	pygame.display.update()



