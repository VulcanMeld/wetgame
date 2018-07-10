import random
import pygame


raindrop_image = pygame.transform.scale2x(pygame.image.load("images/raindrop.png"))


class RainDrop(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = raindrop_image
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(1, 600)
        self.rect.y = 0

    def update(self):
        self.rect.y += 1
