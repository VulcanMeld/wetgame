import pygame
from pygame import Color, Rect

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

ingame_score_font = pygame.font.Font(pygame.font.get_default_font(), 20)
endgame_score_font = pygame.font.Font(pygame.font.get_default_font(), 32)


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

        self.score = 0
        self.game_over = False

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

        self.wetman.draw(screen)

        self.raindrops.draw(screen)

        if not self.game_over:
            score_message = 'Seconds Alive: ' + str(self.score/1000)
            font_surface = ingame_score_font.render(score_message, True, FONT_COLOR)

            screen.blit(font_surface,(500,10))
        else:
            score_message = 'You stayed alive for {:.2f} seconds!'.format(self.score/1000)
            font_surface = endgame_score_font.render(score_message, True, FONT_COLOR)

            pygame.draw.rect(screen, Color("black"), Rect(screen_width/2 - 150, screen_height/2 - 100, 300, 200))
            pygame.draw.rect(screen, Color("white"), Rect(screen_width/2 - 148, screen_height/2 - 98, 296, 196))
            screen.blit(font_surface, (
                screen_width/2 - font_surface.get_width()/2,
                screen_height/2 - font_surface.get_height()/2
            ))

        pygame.display.flip()

    def game_loop(self):
        while not self.done:

            for event in pygame.event.get():
                self.handle_event(event)

            if not self.game_over:
                self.score = pygame.time.get_ticks()

                collision = pygame.sprite.spritecollideany((self.wetman.sprites())[0], self.raindrops)
                if collision is not None:
                    self.game_over = True

                self.wetman.update(self.man_left, self.man_right)

            self.raindrops.update()
            self.raindrops.add(RainDrop(screen_width))

            self.draw()

            self.clock.tick(FRAME_RATE)


game = WetGame()
game.game_loop()

pygame.quit()



