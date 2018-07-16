import pygame
import random


class RainDrop(pygame.sprite.Sprite):

    raindrop_image = pygame.transform.scale2x(pygame.image.load("images/raindrop.png"))

    def __init__(self, screen_width):
        super().__init__()

        self.image = self.raindrop_image
        self.rect = self.image.get_rect()
        self.rect.x = random.uniform(0, screen_width - self.image.get_width())
        self.rect.y = 0
        self.v_y = 4 ** (1/random.uniform(1, 2))

    def update(self):
        self.rect.y += self.v_y
