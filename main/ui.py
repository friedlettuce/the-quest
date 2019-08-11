import pygame


class UI:

    def __init__(self, screen, game_settings, mana=False):
        empty_bar = '../resources/ui/EmptyBar.png'
        health_bar = '../resources/ui/RedBar.png'
        mana_bar = '../resources/ui/BlueBar.png'
        self.mana = mana
        xffset = yffset = 10

        self.emptyHB = Bar(screen, game_settings, empty_bar, xffset, yffset)
        self.healthBar = Bar(screen, game_settings, health_bar, xffset, yffset)

        if self.mana:
            self.emptyMB = Bar(screen, game_settings, empty_bar,
                           xffset + self.healthBar.rect.w, yffset)
            self.manaBar = Bar(screen, game_settings, mana_bar,
                           xffset + self.healthBar.rect.w, yffset)

    def blitme(self, areah, aream=0):
        self.emptyHB.blitme()
        self.healthBar.blitdec(areah)
        if self.mana:
            self.emptyMB.blitme()
            self.manaBar.blitdec(aream)


class Bar:

    def __init__(self, screen, game_settings, bar, xffset, yffset):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.image.load(bar)
        self.image = pygame.transform.scale(
            self.image, (game_settings.statusBarX, game_settings.statusBarY))
        self.rect = self.image.get_rect()

        self.rect.left = xffset
        self.rect.centery = self.screen_rect.height - yffset

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def blitdec(self, area):
        self.screen.blit(self.image, self.rect,
                         (0, 0, int(self.rect.w * area), self.rect.h))
