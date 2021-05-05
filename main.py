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


#Font
pygame.font.init()


#mainPlayer


#mainEnemies

def mainGame():
    runGame = True
    test = True;
    FPS = 60
    level = 1
    lives = 5
    # change font later on to be more mainstream/ cleaner/ professional
    mainFont = pygame.font.SysFont("comicsans", 50)
    gameClock = pygame.time.Clock()

    def GameWindow():
        WINDOW.blit((0.0))
        #show Text
        livesLabel = mainFont.render(f"Lives: {lives}", 1, (255,255,255) )
        levelLabel = mainFont.render(f"Level: {level}", 1, (255, 255, 255))

        # show Levels and Lives
        WINDOW.blit(livesLabel, (10, 10))
        WINDOW.blit(WIDTH- levelLabel.get_width()-10, 10)

        pygame.display.update()
    while runGame:
        #ensure game constantly runs
        gameClock.tick(FPS)

        #run Game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                runGame: False

mainGame()