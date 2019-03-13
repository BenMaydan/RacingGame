import pygame
from pygame.locals import *
import random
from objects import Car, Laser, EnemyCar, EnemyLaser, spawnEnemyCar
import drawings
import time
import random
import os
import sys

pygame.init()
pygame.display.set_caption("Racing Game! Oh SHIT, That's The Wrong Name! Made by Ben Maydan")
screen = pygame.display.set_mode((800, 600))
BLACK = (0, 0, 0)
GRAY = (169,169,169)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
running = True
clock = pygame.time.Clock()
basicfont = pygame.font.SysFont(None, 12)


#GROUPS OF SPRITES
allSpritesList = pygame.sprite.Group()
carList = pygame.sprite.Group()
enemyCarList = pygame.sprite.Group()
lasersList = pygame.sprite.Group()
enemyLasersList = pygame.sprite.Group()


#HOW CAR LOOKS IN GAME
widthOfCar = 65
heightOfCar = 80
playerCar = Car(widthOfCar, heightOfCar, 445, 520, carList, 25, 1)
carList.add(playerCar)
allSpritesList.add(playerCar)


#First Enemy Car
widthOfCar = 120
heightOfCar = 80
howOftenCarShoots = random.randrange(4, 8)
enemyCar = EnemyCar(widthOfCar, heightOfCar, howOftenCarShoots)
randomX = random.randrange(200, 700)
randomY = random.randrange(20, 50)
enemyCar.rect.x = randomX
enemyCar.rect.y = randomY
enemyCarList.add(enemyCar)
allSpritesList.add(enemyCar)


#Drawing stuff
surface = pygame.Surface((50, 50))
rect = surface.get_rect()
screen.blit(surface, (400, 300))
startingPointFirstRoadLine = -595
drawings.initialDrawing(screen, GREEN, GRAY, WHITE, carList, startingPointFirstRoadLine)


SPAWNCAREVENT, t = pygame.USEREVENT+1, 1000
pygame.time.set_timer(SPAWNCAREVENT, t)
while running:
	#Main Event loop
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_ESCAPE:
				running = False
			if event.key == K_SPACE:
				laser = Laser(7, 35)
				#Loads the image onto the screen and changes position
				laser.image = pygame.image.load("redlaser.png").convert_alpha()
				laser.image = pygame.transform.scale(laser.image, [laser.width, laser.height])
				laser.rect.x = playerCar.rect.x
				laser.rect.y = playerCar.rect.y
				#Adds to sprites list
				lasersList.add(laser)
				allSpritesList.add(laser)
		#Called every 3000 milliseconds
		elif event.type == SPAWNCAREVENT:
			#SPAWNS enemy cars every (insert number) seconds
			if len(enemyCarList) <= 30:
				spawnEnemyCar(allSpritesList, enemyCarList)
			else:
				pass
		elif event.type == QUIT:
			running = False



	keys = pygame.key.get_pressed()
	#booster
	moveUp = 7 if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else 5
	moveDown = 5 if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else 3
	moveSideways = 6 if keys[pygame.K_LSHIFT] or keys[pygame.K_RSHIFT] else 4

	#Enemy car moveable is only for testing
	enemyCarMoveable = True

	if keys[pygame.K_LEFT] or keys[pygame.K_a]:
		if playerCar.rect.x > 3:
			playerCar.moveLeft(moveSideways)
			#print('X Cord:' + str(playerCar.rect.x) + '. Y Cord:' + str(playerCar.rect.y))
		else:
			pass

	if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
		if playerCar.rect.x < 733:
			playerCar.moveRight(moveSideways)
			#print('X Cord:' + str(playerCar.rect.x) + '. Y Cord:' + str(playerCar.rect.y))
		else:
			pass


	if keys[pygame.K_UP] or keys[pygame.K_w]:
		if playerCar.rect.y > 4:
			playerCar.moveUp(moveUp)
			#print('X Cord:' + str(playerCar.rect.x) + '. Y Cord:' + str(playerCar.rect.y))
		else:
			startingPointFirstRoadLine += 5


	if keys[pygame.K_DOWN] or keys[pygame.K_s]:
		if playerCar.rect.y < 523:
			playerCar.moveDown(moveDown)
			#print('X Cord:' + str(playerCar.rect.x) + '. Y Cord:' + str(playerCar.rect.y))
		else:
			startingPointFirstRoadLine -= 3



	#These two four loops underneath remove the laser/enemyLaser if they are out of bounds and if it hits an enemy car
	for laser in lasersList:
		if laser.rect.y > 4:
			#Checks collision of laser with enemy car
			for enemyCar in enemyCarList:
				if laser.collided_with(enemyCar):
					laser.kill()
					enemyCar.kill()
					playerCar.gainPoint()
					os.system('clear')
					print("Hitpoints Left:", playerCar.getHealth())
					print("Player car's points:", playerCar.getPoints())

		else:
			lasersList.remove(laser)
			allSpritesList.remove(laser)

	for enemyLaser in enemyLasersList:
		if enemyLaser.rect.x > 3 or enemyLaser.rect.x < 735 or enemyLaser.rect.y > 5 or enemyLaser.rect.y <525:
			#Checks collision of enemy laser with player car
			pass
		else:
			enemyLasersList.remove(enemyLaser)
			allSpritesList.remove(enemyLaser)


	for enemyCar in enemyCarList:
		if enemyCar.collided_with(playerCar):
			#Checks to make sure the car has enough health to destroy another car
			if playerCar.health['hp'] > 0:
				enemyCar.kill()
				playerCar.loseHealth()
				playerCar.gainPoint()
				os.system('clear')
				print("Hitpoints Left:", playerCar.getHealth())
				print("Points Gained:", playerCar.getPoints())
			else:
				playerCar.kill()
				enemyCar.kill()
				os.system('clear')
				for x in range(80):
					print('YOU DIED. OMEEGA LOLLLLL!')
					pygame.quit()
				sys.exit()


	#Loads the enemy lasers a random amount
	#Adds enemy lasers to the sprites lists
	#Changes starting position of enemy laser to the position of the enemy car
	#Sets position of enemy laser because position of enemy car is random over the time of the game
	#Then finally (SUPPOSED TO) shoot the laser forward (or backward depending on the way you look) a random amount
	randomAmount = random.randrange(3, 5)
	for x in range(randomAmount):
		enemyLaser = EnemyLaser(7, 35)
		#Loads the image onto the screen and changes position
		enemyLaser.image = pygame.image.load("redlaser.png").convert_alpha()
		enemyLaser.image = pygame.transform.scale(enemyLaser.image, [enemyLaser.width, enemyLaser.height])
		enemyLaser.rect.x = enemyCar.rect.x
		enemyLaser.rect.y = enemyCar.rect.y
		#Adds to sprites list
		enemyLasersList.add(enemyLaser)
		allSpritesList.add(enemyLaser)
		
		#Shoots enemy lasers forward a random amount
		for y in range(20):
			enemyLasersList.update()



	#Draws everything on the screen
	#Including grass, road, and road lines

	ground = pygame.draw.rect(screen, GREEN, [0, 0, 800, 600])
	#Stuff having to do with placement of the road and road lines
	xCordRoad = 250
	xCordRoadLines = 400
	spaceBetweenRoadLines = 55
	road = pygame.draw.rect(screen, GRAY, [xCordRoad, 0, 300, 600])
	firstRoadLine = [xCordRoadLines, startingPointFirstRoadLine, 10, 35]
	roadLines = [firstRoadLine]
	#print(firstRoadLine)
	roadLines = [firstRoadLine for x in range(40)]
	pygame.draw.rect(screen, WHITE, roadLines[0])
	for line in roadLines:
		line[1] += spaceBetweenRoadLines
		pygame.draw.rect(screen, WHITE, line)


	#Update screen
	carList.draw(screen)
	enemyCarList.draw(screen)
	allSpritesList.draw(screen)
	allSpritesList.update()
	pygame.display.flip()


	#Frames per second
	clock.tick(144)


pygame.quit()