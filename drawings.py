import pygame


def initialDrawing(screen, colorOfGround, colorOfRoad, colorOfRoadLines, carList, startingPointFirstRoadLine):
	"""
	Draws the first thing the user sees when he starts the game
	"""

	#All of this crap below is the initial drawing of the entire game
	ground = pygame.draw.rect(screen, colorOfGround, [0, 0, 800, 600])
	#Stuff having to do with placement of the road and road lines
	xCordRoad = 250
	xCordRoadLines = 400
	spaceBetweenRoadLines = 55
	road = pygame.draw.rect(screen, colorOfRoad, [xCordRoad, 0, 300, 600])
	firstRoadLine = [xCordRoadLines, startingPointFirstRoadLine, 10, 35]
	roadLines = [firstRoadLine]
	#print(firstRoadLine)
	roadLines = [firstRoadLine for x in range(40)]
	pygame.draw.rect(screen, colorOfRoadLines, roadLines[0])
	for line in roadLines:
		line[1] += spaceBetweenRoadLines
		pygame.draw.rect(screen, colorOfRoadLines, line)
	carList.draw(screen)
	#Update screen
	pygame.display.flip()