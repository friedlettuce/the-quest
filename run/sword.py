import pygame


class Sword:

    def __init__(self, screen, rect):
        self.screen = screen

        self.image_r = pygame.transform.scale2x(
            pygame.image.load('../resources/items/weapon/anime_sword.png'))
        self.image_l = pygame.transform.flip(self.image_r, True, False)

        self.image_r = pygame.transform.rotate(self.image_r, -45)
        self.image_l = pygame.transform.rotate(self.image_l, 45)

        self.image = self.image_r

        self.rect = self.image.get_rect()
        self.rect.centerx = rect.centerx + 30
        self.rect.centery = rect.centery - 13

        self.center = float(self.rect.centerx)

    def face_right(self):
        self.image = self.image_r

    def face_left(self):
        self.image = self.image_l

    def blitme(self):
        self.rect.centerx = self.center
        self.screen.blit(self.image, self.rect)