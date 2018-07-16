import pygame

from raindrop import RainDrop
from wetman import WetMan

pygame.init()
pygame.font.init()

BACKGROUND = (255, 255, 255)
FRAME_RATE = 60
MAN_SPEED = 5
FONT_COLOR = (0,0,0)

screen_width = 800
screen_height = 600

screen = pygame.display.set_mode((screen_width, screen_height))

font = pygame.font.Font(pygame.font.get_default_font(),20)


class WetGame(object):

    def __init__(self):
        self.done = False
        self.man_pos_x = 100
        self.man_pos_y = 100
        self.man_right = False
        self.man_left = False
        self.clock = pygame.time.Clock()
        self.raindrops = pygame.sprite.Group()
        self.wetman = pygame.sprite.Group()
        self.wetman.add(WetMan(screen_width, screen_height))


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

        score_message = 'Seconds Alive: ' + str(pygame.time.get_ticks()/1000)
        font_surface = font.render(score_message, False, FONT_COLOR)

        screen.blit(font_surface,(500,10))

        self.wetman.draw(screen)

        self.raindrops.draw(screen)

        pygame.display.flip()


    def game_loop(self):
        while not self.done:

            for event in pygame.event.get():
                self.handle_event(event)

            collision = pygame.sprite.spritecollideany((self.wetman.sprites())[0], self.raindrops)

            if collision is not None:
                self.done = True

            self.wetman.update(self.man_left, self.man_right)

            self.raindrops.update()
            self.raindrops.add(RainDrop(screen_width))

            self.draw()

            self.clock.tick(FRAME_RATE)


game = WetGame()
game.game_loop()

pygame.quit()



