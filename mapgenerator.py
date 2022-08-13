import pygame
import sys
import random

#grass=#00AA33

blockSize = 32
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
weights = [70, 1, 1, 2, 2]


class Map:
    def __init__(self, seedPositionX, seedPositionY, mapSize):
        



        self.seedPositionX = seedPositionX
        self.seedPositionY = seedPositionY
        self.mapSize = mapSize
        self.blockSize = blockSize

        pygame.init()
        self.SCREEN = pygame.display.set_mode((self.mapSize*blockSize, self.mapSize*blockSize))
        self.CLOCK = pygame.time.Clock()
        self.NONE = pygame.image.load('grass.png').convert()
        self.NONE.get_rect()

        self.GRASS = pygame.image.load('grass.png').convert()
        self.GRASS.get_rect()
        self.PINKFLOWER = pygame.image.load('pinkflower.png').convert()
        self.PINKFLOWER.get_rect()
        self.YELLOWFLOWER = pygame.image.load('yellowflower.png').convert()
        self.YELLOWFLOWER.get_rect()
        self.SMALLROCKS = pygame.image.load('smallstones.png').convert()
        self.SMALLROCKS.get_rect()
        self.LARGEROCKS = pygame.image.load('largestone.png').convert()
        self.LARGEROCKS.get_rect()
        self.STUMP = pygame.image.load('treestump.png').convert()
        self.STUMP.get_rect()


        self.redChoices = [self.GRASS, self.GRASS, self.PINKFLOWER, self.SMALLROCKS, self.YELLOWFLOWER]
        self.orangeChoices = [self.GRASS, self.PINKFLOWER, self.STUMP, self.LARGEROCKS]
        self.yellowChoices = [self.GRASS, self.YELLOWFLOWER, self.GRASS, self.LARGEROCKS]
        self.greenChoices = [self.GRASS, self.GRASS, self.GRASS, self.GRASS, self.STUMP]

        self.createMap()
        
    
    def createMap(self):
        self.mapSquares = []
        for x in range(0, self.mapSize):
            for y in range(0, self.mapSize):
                color = self.GRASS
                if (y == self.seedPositionY) and (x==self.seedPositionX):
                    color = self.GRASS
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
            if pos[2] == self.GRASS:
                for pos2 in self.mapSquares:
                    if pos2[2] == self.GRASS:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(self.redChoices, weights=weights[0:len(self.redChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == self.PINKFLOWER:
                for pos2 in self.mapSquares:
                    if pos2[2] == self.GRASS:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(self.orangeChoices, weights=weights[0:len(self.orangeChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == self.YELLOWFLOWER:
                for pos2 in self.mapSquares:
                    if pos2[2] == self.GRASS:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(self.yellowChoices, weights=weights[0:len(self.yellowChoices)], k=1)
                            pos2[2] = position[0]
            if pos[2] == self.SMALLROCKS:
                for pos2 in self.mapSquares:
                    if pos2[2] == self.GRASS:
                        if (pos != pos2) and (abs(pos[0] - pos2[0]) <=1) and (abs(pos[1] - pos2[1]) <=1) and ((abs(pos[0] - pos2[0]) - abs(pos[1] - pos2[1])) != 0):
                            position = random.choices(self.greenChoices, weights=weights[0:len(self.greenChoices)], k=1)
                            pos2[2] = position[0]


    
    def drawGrid(self):
        for pos in self.mapSquares:
            rect = pygame.Rect(pos[0]*self.blockSize, pos[1]*self.blockSize, self.blockSize, self.blockSize)
            #pygame.draw.rect(SCREEN, pos[2], rect)
            self.SCREEN.blit(pos[2], rect)



def main(map):
    while True:
        map.drawGrid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pygame.display.update()


map = Map(5,5,10)
main(map)