import pygame


class WetMan(pygame.sprite.Sprite):

    wetman_image = pygame.transform.scale2x(pygame.image.load("images/wetman.png"))

    def __init__(self, screen_width, screen_height):
        super().__init__()

        self.image = self.wetman_image
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = screen_height - self.image.get_height()

        self.v_x = 3

        self.bounds = (0, screen_width - self.image.get_width())

    def update(self, move_left, move_right):

        if move_left:
            self.rect.x -= self.v_x

        if move_right:
            self.rect.x += self.v_x

        if self.rect.x < self.bounds[0]:
            self.rect.x = self.bounds[0]
        elif self.rect.x > self.bounds[1]:
            self.rect.x = self.bounds[1]
