import pygame

from sword import Sword

class Knight:

    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.transform.scale2x(pygame.image.load(
            '../resources/knight/knight_f_idle_anim_f0.png'))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx / 2
        self.rect.bottom = self.screen_rect.bottom - 58

        self.center = float(self.rect.centerx)

        self.moving_right = False
        self.moving_left = False
        self.facing_right = True

        self.frame = 0
        self.idle_frames_r = []
        self.idle_frames_l = []
        self.run_frames_f = []
        self.run_frames_b = []

        self.weapon = Sword(screen, self.rect)
        self.toggle_weapon = False

        # Stores frames for knight
        for i in range(4):
            frame_img = '../resources/knight/'

            # Removed pygame.transform.scale2x
            self.idle_frames_r.append(pygame.transform.scale2x(pygame.image.load
                (frame_img + 'knight_f_idle_anim_f' + str(i) + '.png')))
            self.run_frames_f.append(pygame.transform.scale2x(pygame.image.load
                (frame_img + 'knight_f_run_anim_f' + str(i) + '.png')))

        for img in self.run_frames_f:
            self.run_frames_b.append(pygame.transform.flip(img, True, False))
        for img in self.idle_frames_r:
            self.idle_frames_l.append(pygame.transform.flip(img, True, False))

    def use_weapon(self):
        self.weapon.using = True

    def update(self):

        if self.moving_right:
            self.image = self.run_frames_f[self.frame]

            if self.rect.centerx < self.screen_rect.width - 16:
                self.center += self.game_settings.player_speed
                self.weapon.center += self.game_settings.player_speed

        elif self.moving_left:
            self.image = self.run_frames_b[self.frame]

            if self.rect.centerx > 17:
                self.center -= self.game_settings.player_speed
                self.weapon.center -= self.game_settings.player_speed

        elif self.facing_right is False:
            self.image = self.idle_frames_l[self.frame]

        else:
            self.image = self.idle_frames_r[self.frame]

        self.rect.centerx = self.center
        self.frame += 1
        self.frame %= self.game_settings.anicycle

        self.weapon.update(self.facing_right)

    def blitme(self):
        if self.toggle_weapon:
            self.weapon.blitme()
        self.screen.blit(self.image, self.rect)
