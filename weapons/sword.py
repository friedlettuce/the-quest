import pygame


class Sword:

    def __init__(self, screen, rect):
        self.screen = screen

        self.image_r = pygame.transform.scale2x(
            pygame.image.load(
                '../resources/items/weapon/anime_sword.png'))
        self.image_l = pygame.transform.flip(self.image_r, True, False)

        self.rotation = 45

        self.image_r_o = pygame.transform.rotate(self.image_r, -self.rotation)
        self.image_l_o = pygame.transform.rotate(self.image_l, self.rotation)
        self.image_r = self.image_r_o
        self.image_l = self.image_l_o

        self.image = self.image_r_o

        self.rect = self.image.get_rect()
        self.rect.centerx = rect.centerx + 30
        self.rect.centery = rect.centery - 10

        self.center = float(self.rect.centerx)

        self.using = False
        self.hit = False

    def face_right(self, pcx):
        self.image = self.image_r
        self.center = pcx + 30

    def face_left(self, pcx):
        self.image = self.image_l
        self.center = pcx - 30

    def update(self, facing_right):
        if self.using:
            if self.rotation != 90 and not self.hit:
                self.rotation += 15

                self.image = pygame.transform.rotate(self.image, 15)
            else:
                self.hit = True

                if self.rotation != 45:
                    self.rotation -- 15

                    self.image = pygame.transform.rotate(self.image, -15)

                else:
                    self.using = False

        self.rect.centerx = self.center

    def blitme(self):
        self.screen.blit(self.image, self.rect)