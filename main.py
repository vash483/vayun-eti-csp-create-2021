#Eti AND VAYUN PROJECTS

import pygame
import os
import random
import time


#Display
WIDTH, HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("TBD")


#Image Loaders


#Background


def mainGame():
    runGame = True
    FPS = 60
    level = 1
    lives = 5
    gameClock = pygame.time.Clock()

    while runGame:
        #ensure game constantly runs
        gameClock.tick(FPS)

        #run Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame: False

mainGame()