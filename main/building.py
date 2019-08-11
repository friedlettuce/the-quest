import pygame
from pygame.sprite import Sprite


class Building(Sprite):

    def __init__(self, screen, game_settings, path):
        super().__init__()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        yffset = 30

        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, (41, 66))
        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.w - 30
        self.rect.bottom = self.screen_rect.h - yffset

    def blitme(self):
        self.screen.blit(self.image, self.rect)