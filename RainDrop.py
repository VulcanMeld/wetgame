import random
import pygame


class RainDrop(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("images/raindrop.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1,600)
        self.rect.y = 0



