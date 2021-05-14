#Eti AND VAYUN PROJECTS

import pygame
import os
import time
import random
import sys
pygame.font.init()

WIDTH, HEIGHT = 800, 800
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fruit Dash")

# Load images
RED_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_red_small.png"))
GREEN_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_green_small.png"))
BLUE_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_blue_small.png"))

# Player player
YELLOW_SPACE_SHIP = pygame.image.load(os.path.join("assets", "pixel_ship_yellow.png"))

# Lasers
RED_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_red.png"))
GREEN_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_green.png"))
BLUE_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_blue.png"))
YELLOW_LASER = pygame.image.load(os.path.join("assets", "pixel_laser_yellow.png"))

# Background
BACKGROUND = pygame.transform.scale(pygame.image.load(os.path.join("assets", "background-black.png")), (WIDTH, HEIGHT))

class Monkey:
	def __init__(self, x, y, health=100):
		self.x = x
		self.y = y
		self.health = health
		self.monkey_img = None
		self.banana_img = None
		self.lasers = []
		self.cool_down_counter = 0

		

	def draw(self, window):
		window.blit(self.monkey_img, (self.x, self.y))

	def get_width(self):
		return self.monkey_img.get_width()

	def get_height(self):
		return self.monkey_img.get_height()


class Player(Monkey):
	def __init__(self, x, y, health =100):
		super(). __init__(x, y, health)
		self.monkey_img = YELLOW_SPACE_SHIP
		self.banana_img = YELLOW_LASER
		self.mask = pygame.mask.from_surface(self.monkey_img)
		self.max_health = health


class Enemy(Monkey):

	COLOR_MAP = {
				"red" : (RED_SPACE_SHIP, RED_LASER),
				"green" : (GREEN_SPACE_SHIP, GREEN_LASER),
				"blue" : (BLUE_SPACE_SHIP, BLUE_LASER)
	}
	def __init__(self, x, y, color, health=100):
		super().__init__(x, y, health)
		self.monkey_img, self.laser_img = self.COLOR_MAP[color]
		self.mask = pygame.mask.from_surface(self.monkey_img)

	def move(self, vel):
		self.y += vel



def main():
    run = True
    FPS = 60
    level = 1
    lives = 5
    game_font = pygame.font.SysFont("comicsans", 50)

    enemies = []
    wave_length = 5
    enemy_vel = 1
    
    player_vel = 5

    player = Player(300, 650)

    clock = pygame.time.Clock()

    def redraw_window():
    	WIN.blit(BACKGROUND,(0,0))
    	lives_label = game_font.render(f"Lives: {lives}", 1, (255,255,255))
    	level_label = game_font.render(f"Level: {level}", 1, (255,255,255))

    	WIN.blit(level_label,(10,10))
    	WIN.blit(lives_label,(WIDTH - level_label.get_width() - 10,10))
'''

        for enemy in enemies:
            enemy.draw(WIN)

    	player.draw(WIN)


        for
    	pygame.display.update()
'''

while run:
        #ensure game constantly runs
    clock.tick(FPS)

    if len(enemies) == 0:
        level += 1
        wave_length += 5
        for i in range(wave_length):
            enemy = Enemy(random.randrange(50, WIDTH-100), random.randrange(-1500, -100), random.choice(["red", "blue", "green"]))
            enemies.append(enemy)

        

        #run Game
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
            pygame.quit()
            sys.exit()
            exit()

    key_controls = pygame.key.get_pressed()
    if key_controls[pygame.K_a]and player.x - player_vel > 0: #moving left
        player.x -= player_vel
    if key_controls[pygame.K_d]and player.x + player_vel + player.get_width() < WIDTH: #moving right
        player.x += player_vel
    if key_controls[pygame.K_w]and player.y - player_vel > 0: #moving up
        player.y -= player_vel
    if key_controls[pygame.K_s] and player.y + player_vel + player.get_height() < HEIGHT: #moving down
        player.y += player_vel

    for enemy in enemies:
        enemy.move(enemy_vel)

    redraw_window()

               
main()
