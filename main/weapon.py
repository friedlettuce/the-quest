import pygame
from pygame.sprite import Sprite
from animations import HitAnimation


class Weapon(Sprite):
    def __init__(self, screen, game_settings, rect, weapon):
        super().__init__()
        self.screen = screen
        self.xoffset = 15
        self.rotation = 45

        # Sets up state flags
        self.using = False
        self.hit = False
        self.toggled = False
        self.collision = False

        # Loads weapon img
        self.image_r = pygame.image.load(
            '../resources/items/weapon/' + weapon + '.png')
        self.image_l = pygame.transform.flip(self.image_r, True, False)
        # Tilts weapon
        self.image_r = pygame.transform.rotate(self.image_r, -self.rotation)
        self.image_l = pygame.transform.rotate(self.image_l, self.rotation)

        # Sets up init position/image
        self.image = self.image_r
        self.rect = self.image.get_rect()
        self.rect.centerx = rect.centerx + self.xoffset
        self.rect.centery = rect.centery

        self.damage = game_settings.setWeaponDamage(weapon)

        self.animation = HitAnimation(screen, game_settings)

    def face_right(self):
        self.image = self.image_r
        self.animation.right()

    def face_left(self):
        self.image = self.image_l
        self.animation.left()

    def update(self):
        self.animation.update()

    def blitme(self):
        if self.toggled:
            self.screen.blit(self.image, self.rect)

            if self.using:
                self.animation.blitme(self.rect)


class KnightWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='ks'):
        super().__init__(screen, game_settings, rect, weapon)

        # Rotation and positioning vars
        self.rotbase = 45
        self.rottarget = 60
        self.rotrate = 5

    def update(self, centerx, centery, facing_right):

        if self.using and self.toggled:
            if self.rotation != self.rottarget and not self.hit:
                self.rotation += self.rotrate

                self.image = pygame.transform.rotate(self.image, -self.rotrate)
            else:
                self.hit = True

                if self.rotation != self.rotbase:
                    self.rotation -= self.rotrate

                    self.image = pygame.transform.rotate(
                        self.image, self.rotrate)
                else:
                    self.using = False
                    self.hit = False

                    if facing_right:
                        self.image = self.image_r
                    else:
                        self.image = self.image_l

        self.rect.centerx = centerx
        self.rect.centery = centery

        if facing_right:
            self.rect.centerx += self.xoffset - (self.rotation - (self.rotbase + self.rotrate))
        else:
            self.rect.centerx -= self.xoffset - (self.rotation - (self.rotbase + self.rotrate))

        super().update()


class WizardWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='g'):
        super().__init__(screen, game_settings, rect, weapon)

        # Rotation and positioning vars
        self.rotbase = 45
        self.rottarget = 60
        self.rotrate = 5

    def update(self, centerx, centery, facing_right):

        if self.using and self.toggled:
            if self.rotation != self.rottarget and not self.hit:
                self.rotation += self.rotrate

                self.image = pygame.transform.rotate(self.image, -self.rotrate)
            else:
                self.hit = True

                if self.rotation != self.rotbase:
                    self.rotation -= self.rotrate

                    self.image = pygame.transform.rotate(
                        self.image, self.rotrate)
                else:
                    self.using = False
                    self.hit = False

                    if facing_right:
                        self.image = self.image_r
                    else:
                        self.image = self.image_l

        self.rect.centerx = centerx
        self.rect.centery = centery

        if facing_right:
            self.rect.centerx += self.xoffset - (self.rotation - (self.rotbase + self.rotrate))
        else:
            self.rect.centerx -= self.xoffset - (self.rotation - (self.rotbase + self.rotrate))

        super().update()


class ElfWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='d'):
        super().__init__(screen, game_settings, rect, weapon)

        # Rotation and positioning vars
        self.rotbase = 45
        self.rottarget = 60
        self.rotrate = 5

    def update(self, centerx, centery, facing_right):

        if self.using and self.toggled:
            if self.rotation != self.rottarget and not self.hit:
                self.rotation += self.rotrate

                self.image = pygame.transform.rotate(self.image, -self.rotrate)
            else:
                self.hit = True

                if self.rotation != self.rotbase:
                    self.rotation -= self.rotrate

                    self.image = pygame.transform.rotate(
                        self.image, self.rotrate)
                else:
                    self.using = False
                    self.hit = False

                    if facing_right:
                        self.image = self.image_r
                    else:
                        self.image = self.image_l

        self.rect.centerx = centerx
        self.rect.centery = centery

        if facing_right:
            self.rect.centerx += self.xoffset - (self.rotation - (self.rotbase + self.rotrate))
        else:
            self.rect.centerx -= self.xoffset - (self.rotation - (self.rotbase + self.rotrate))

        super().update()
