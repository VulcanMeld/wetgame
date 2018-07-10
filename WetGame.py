import pygame

from pygame.locals import *

pygame.init()

BACKGROUND = (255, 255, 255)
FRAME_RATE = 60
MAN_SPEED = 5

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

wetman = pygame.image.load("images/wetman.png")
width_wetman = wetman.get_width()



class WetGame(object):

    def __init__(self):
        self.done = False
        self.man_pos_x = 100
        self.man_pos_y = 100
        self.man_right = False
        self.man_left = False
        self.clock = pygame.time.Clock()

    def handle_event(self, event):
        if event.type == pygame.QUIT:
            self.done = True
        elif event.type == pygame.KEYDOWN or event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                self.man_right = event.type == pygame.KEYDOWN
            elif event.key == pygame.K_LEFT:
                self.man_left = event.type == pygame.KEYDOWN

    def draw(self):
        screen.fill(BACKGROUND)

        screen.blit(wetman, (self.man_pos_x, self.man_pos_y))
        screen.blit(raindrop, (100, 300))

        pygame.display.flip()

    def game_loop(self):
        while not self.done:

            for event in pygame.event.get():
                self.handle_event(event)

            if self.man_right:
                self.man_pos_x += MAN_SPEED
                if self.man_pos_x > screen_width - width_wetman:
                    self.man_pos_x = screen_width - width_wetman

            if self.man_left:
                self.man_pos_x -= MAN_SPEED
                if self.man_pos_x < 0:
                    self.man_pos_x = 0

            self.draw()

            self.clock.tick(FRAME_RATE)


game = WetGame()
game.game_loop()

pygame.quit()



