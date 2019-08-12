import pygame
from pygame.sprite import Sprite
from animations import Animation


class Weapon(Sprite):

    def __init__(self, screen, game_settings, rect, weapon):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.xoffset = 15
        self.rotation = 45

        # Sets up state flags
        self.using = False
        self.hit = False
        self.toggled = False
        self.collision = False

        # Rotation and positioning vars
        self.rotbase = 45
        self.rottarget = 60
        self.rotrate = 5

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
        self.rect.left = rect.right
        self.rect.centery = rect.centery

        self.damage = game_settings.setWeaponDamage(weapon)

        self.animation = Animation(screen, game_settings.hit_path,
                         game_settings.hit_frames, game_settings.hit_size)

    def face_right(self):
        self.image = self.image_r
        self.animation.right()

    def face_left(self):
        self.image = self.image_l
        self.animation.left()

    def rotating(self, facing_right):

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

    def update(self, rect, centery, facing_right):
        self.rotating(facing_right)
        self.rect.centery = centery

        if facing_right:
            self.rect.centerx = rect.right - ((rect.centerx - rect.right) / 3)
        else:
            self.rect.centerx = rect.left + ((rect.left - rect.centerx) / 3)

        self.animation.update()

    def blitme(self):
        if self.toggled:
            self.screen.blit(self.image, self.rect)

            if self.using:
                rect_anim = self.rect.copy()
                rect_anim.left = rect_anim.right
                self.animation.blitme(rect_anim)


class KnightWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='ks'):
        super().__init__(screen, game_settings, rect, weapon)


class WizardWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='g'):
        super().__init__(screen, game_settings, rect, weapon)
        self.using_spell = False
        self.blit_spell = False

        self.ice = Animation(self.rect, screen, game_settings)

    def reset(self):
        self.using_spell = False
        self.blit_spell = False
        self.ice.reset(self.rect)

    def update(self, rect, centery, facing_right):
        super().update()

        if self.using_spell and not self.ice_collision:
            if facing_right:
                self.ice.rect.centerx += self.game_settings.ice_speed
            else:
                self.ice.rect.centerx -= self.game_settings.ice_speed

        if (self.rect.right < self.screen.get_rect().left or
                self.rect.left > self.screen.get_rect().right or
                self.ice.finished):
            self.reset()

    def blitme(self):
        super().blitme()

        if self.blit_spell:
            self.ice.blitme()


class ElfWeapon(Weapon):

    def __init__(self, screen, game_settings, rect, weapon='d'):
        super().__init__(screen, game_settings, rect, weapon)
