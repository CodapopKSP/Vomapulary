import pygame
import sys
import random

blockSize = 40
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (200, 0, 0)
ORANGERED = (200, 60, 0)
ORANGE = (200, 120, 0)
YELLOWORANGE = (200, 160, 0)
YELLOW = (200, 200, 0)
GREEN = (0, 200, 0)
BLUE = (0, 0, 200)
MAGENTA = (200, 0, 200)
WINDOW_HEIGHT = 400
WINDOW_WIDTH = 400
weights = [50, 50, 10, 50, 10]
redChoices = [RED, ORANGERED, ORANGE]
orangeChoices = [WHITE, ORANGE, YELLOWORANGE, YELLOW, ORANGERED]
yellowChoices = [WHITE, YELLOW, YELLOWORANGE, GREEN]
greenChoices = [GREEN]

class Map:
    def __init__(self, seedPositionX, seedPositionY, seed2PositionX, seed2PositionY, mapSize):
        self.seedPositionX = seedPositionX
        self.seedPositionY = seedPositionY
        self.seed2PositionX = seed2PositionX
        self.seed2PositionY = seed2PositionY
        self.mapSize = mapSize
        self.createMap()
        self.blockSize = blockSize
    
    def createMap(self):
        self.mapSquares = []
        for x in range(0, self.mapSize):
            for y in range(0, self.mapSize):
                color = WHITE
                if (y == self.seedPositionY) and (x==self.seedPositionX):
                    color = RED
                if (y == self.seed2PositionY) and (x==self.seed2PositionX):
                    color = GREEN
                self.mapSquares.append([x, y, color])
        self.growSeed()
        
        '''
        finishedGrowing = False
        while finishedGrowing==False:
            self.growSeed()
            allFinished = True
            for pos in self.mapSquares:
                if pos[2] == WHITE:
                    allFinished = False
            finishedGrowing = allFinished'''

    def growSeed(self):
        for pos in self.mapSquares:
            if pos[2] == RED:
                for pos2 in self.mapSquares:
                    if pos2[2] == WHITE:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(redChoices, weights=weights[0:len(redChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == ORANGE or ORANGERED:
                for pos2 in self.mapSquares:
                    if pos2[2] == WHITE:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(orangeChoices, weights=weights[0:len(orangeChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == YELLOW or YELLOWORANGE:
                for pos2 in self.mapSquares:
                    if pos2[2] == WHITE:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(yellowChoices, weights=weights[0:len(yellowChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == GREEN:
                for pos2 in self.mapSquares:
                    if pos2[2] == WHITE:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(greenChoices, weights=weights[0:len(greenChoices)], k=1)
                            pos2[2] = position[0]


    
    def drawGrid(self):
        for pos in self.mapSquares:
            rect = pygame.Rect(pos[0]*self.blockSize, pos[1]*self.blockSize, self.blockSize, self.blockSize)
            pygame.draw.rect(SCREEN, pos[2], rect)



def main(map):
    global SCREEN, CLOCK
    pygame.init()
    SCREEN = pygame.display.set_mode((map.mapSize*blockSize, map.mapSize*blockSize))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)

    while True:
        map.drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()


map = Map(0,0,19,19,20)
main(map)