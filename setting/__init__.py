import pygame
import os
import random
import time
pygame.font.init()

SNOW = (255, 250, 250)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
colors = [RED, GREEN, BLUE, SNOW, YELLOW]
screen_width = 800
screen_height = 600

FPS = 100
level = 1
lives = 6
player_speed = 5
main_font = pygame.font.SysFont("Arial", 40, 2)

lives_label = main_font.render(f"Lives: {lives}", 1, (YELLOW), 4)
levels_label = main_font.render(f"Level: {level}", 1, (YELLOW), 4)

#load image
enemy_1 = pygame.image.load(os.path.join("enemies", "1.png"))
enemy_2 = pygame.image.load(os.path.join("enemies", "2.png"))
enemy_3 = pygame.image.load(os.path.join("enemies", "3.png"))
enemy_4 = pygame.image.load(os.path.join("enemies", "4.png"))
enemy_5 = pygame.image.load(os.path.join("enemies", "5.png"))

player_img = pygame.image.load("player.png")  #player image

BG = pygame.image.load("background.png")   #Background

icon = pygame.image.load("monster.png")   #change the icon

pygame.display.set_icon(icon)

bullet = pygame.image.load("bullet.png")   #bullet

pygame.display.set_caption("An Ordinary Day In Space")


