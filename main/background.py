import pygame
from building import Building


class Background:

    def __init__(self, game_settings, screen, file):

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.transform.scale(
            pygame.image.load(file),
            [game_settings.screen_width, game_settings.screen_height])

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # building_path = '../resources/building/castle/2/Asset 24.png'
        # self.new_building = Building(screen, game_settings, building_path)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        # self.new_building.blitme()