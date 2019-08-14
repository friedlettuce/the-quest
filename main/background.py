import pygame
from building import Building


class Background:

    def __init__(self, game_settings, screen, file):
        self.landscape1 = Landscape(game_settings, screen, file)
        self.landscape2 = Landscape(game_settings, screen, file)
        self.landscape2.rect.left = self.landscape2.right()

        self.moving_left = self.moving_right = False
        self.speed = 0

    def left(self, speed):
        self.moving_left = True
        self.speed = speed

    def right(self, speed):
        self.moving_right = True
        self.speed = speed

    def update(self):
        if self.moving_right:
            self.landscape1.rect.centerx += self.speed
            self.landscape2.rect.centerx += self.speed

            if self.landscape1.rect.left <= self.landscape1.screen_rect.left:
                self.landscape1.rect.left = self.landscape1.right()
            elif self.landscape2.rect.left <= self.landscape2.screen_rect.left:
                self.landscape2.rect.left = self.landscape2.right()

        elif self.moving_left:
            self.landscape1.rect.centerx -= self.speed
            self.landscape2.rect.centerx -= self.speed

            if self.landscape1.rect.right >= self.landscape1.screen_rect.right:
                self.landscape1.rect.right = self.landscape1.left()
            elif self.landscape2.rect.right >= self.landscape2.screen_rect.right:
                self.landscape2.rect.right = self.landscape1.left()

    def blitme(self):
        self.landscape1.blitme()
        self.landscape2.blitme()
        # self.new_building.blitme()


class Landscape:

    def __init__(self, game_settings, screen, file):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.transform.scale(
            pygame.image.load(file),
            [game_settings.screen_width, game_settings.screen_height])
        self.image = pygame.transform.scale(
            pygame.image.load(file),
            [game_settings.screen_width, game_settings.screen_height])

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def right(self):
        return self.screen_rect.left
    def left(self):
        return self.screen_rect.right

    def blitme(self):
        self.screen.blit(self.image, self.rect)
