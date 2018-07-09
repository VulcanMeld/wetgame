import pygame

from pygame.locals import *

pygame.init()

background = (255, 255, 255)

screen_width = 800

screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

done = False  # Game state

wetman = pygame.image.load("images/wetman.png")
raindrop = pygame.image.load("images/raindrop.png")

screen.blit(wetman, (100, 100))
screen.blit(raindrop, (100, 300))
pygame.display.flip()

while not done:
    screen.fill(background)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # if event.type == K_RIGHT:
        # 	#
        # if event.type == K_LEFT:
    pygame.display.update()

pygame.quit()
