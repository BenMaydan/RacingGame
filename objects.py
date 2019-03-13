import pygame
import time
import random
import threading


class Laser(pygame.sprite.Sprite):
		"""
		Timer class
		"""
		def __init__(self, width, height):
			super().__init__()

			self.image = pygame.Surface([width, height])
			self.rect = self.image.get_rect()
			self.width = width
			self.height = height


		def update(self):
			"""
			Shoots the bullet
			"""
			self.rect.y -= 8


		def collided_with(self, sprite):
			"""
			Checks collision of the laser with another sprite
			"""
			return self.rect.colliderect(sprite.rect)


class Car(pygame.sprite.Sprite):
	"""
	Car that drives around on the road
	"""
	points = 0

	def __init__(self, width, height, xCord, yCord, carList, health, healthLostEveryHit):
		super().__init__()
		
		self.image = pygame.Surface([width, height])
		self.image = pygame.image.load("CarSprite.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, [width, height])
		self.rect = self.image.get_rect()
		self.rect.x = 445
		self.rect.y = 520

		self.health = {'hp':health, 'hitSomething':0}
		self.healthLostEveryHit = healthLostEveryHit


	def moveRight(self, pixels):
		self.rect.x += pixels
 

	def moveLeft(self, pixels):
		self.rect.x -= pixels


	def moveUp(self, pixels):
		self.rect.y -= pixels


	def moveDown(self, pixels):
		self.rect.y += pixels


	def collided_with(self, sprite):
			"""
			Checks collision of the laser with another sprite
			"""
			return self.rect.colliderect(sprite.rect)


	def loseHealth(self):
		"""
		Detracts health from the player car
		"""
		self.health['hp'] -= self.healthLostEveryHit


	def getHealth(self):
		return self.health['hp']


	def getPoints(self):
		return self.points


	def gainPoint(self):
		self.points += 1


class EnemyLaser(pygame.sprite.Group):
	"""
	Enemy laser for the enemy cars
	"""
	def __init__(self, width, height):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.rect = self.image.get_rect()
		self.width = width
		self.height = height


	def update(self):
		"""
		Pretty muuch only updates at random times
		/When the randomness occurs
		"""
		self.rect.y -= 8


	def collided_with(self, sprite):
			"""
			Checks collision of the laser with another sprite
			"""
			return self.rect.colliderect(sprite.rect)


class EnemyCar(pygame.sprite.Sprite):
	"""
	Enemy car sprite
	"""

	def __init__(self, width, height, howOftenShoot):
		super().__init__()
		self.image = pygame.Surface([width, height])
		self.image = pygame.image.load("EnemyCar.png").convert_alpha()
		self.image = pygame.transform.scale(self.image, [width, height])
		self.rect = self.image.get_rect()
		self.howOftenShoot = howOftenShoot

		self.width = width
		self.height = height


	def moveRight(self):
		"""
		Moves right a random amount of pixels
		"""
		randomAmount = random.randrange(0, 11)
		self.rect.x += randomAmount


	def moveLeft(self):
		"""
		Moves left a random amount of pixels
		"""
		randomAmount = random.randrange(0, 11)
		self.rect.x -= randomAmount


	def moveUp(self):
		"""
		Moves up a random amount of pixels
		"""
		randomAmount = random.randrange(0, 11)
		self.rect.y -= randomAmount


	def moveDown(self):
		"""
		Moves down a random amount of pixels
		"""
		randomAmount = random.randrange(0, 11)
		self.rect.y += randomAmount


	def newRect(self):
		"""
		Updates the rect of the car
		"""
		self.rect = self.image.get_rect()


	def collided_with(self, sprite):
		"""
		Checks collision of the laser with another sprite
		"""
		return self.rect.colliderect(sprite.rect)


def spawnEnemyCar(allSpritesList, enemyCarList):
	"""
	Spawns a sprite every (insert number) of seconds
	"""
	randomAmountOfCars = random.randrange(0, 1)
	#print('Random amount of cars:', randomAmountOfCars)
	for y in range(2):
		enemyCar = EnemyCar(120, 80, 1)
		enemyCar.image = pygame.image.load("EnemyCar.png").convert_alpha()
		enemyCar.image = pygame.transform.scale(enemyCar.image, [enemyCar.width, enemyCar.height])
		randomX = random.randrange(200, 700)
		randomY = random.randrange(20, 50)
		#print('Random x current car:', randomX)
		enemyCar.rect.x = randomX
		enemyCar.rect.y = randomY
		enemyCarList.update()
		enemyCarList.add(enemyCar)
		allSpritesList.add(enemyCar)


