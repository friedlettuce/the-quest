import pygame

from weapons.sword import Sword

class Knight:

    def __init__(self, game_settings, screen):
        self.screen = screen
        self.game_settings = game_settings

        self.image = pygame.image.load(
            '../resources/knight/knight_f_idle_anim_f0.png')
        # self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.scale(self.image, (24, 42))

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx / 3
        self.rect.bottom = self.screen_rect.bottom - 32

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

            # Loads and resizes for idle frames facing right
            temp_frame = pygame.image.load(
                frame_img + 'knight_f_idle_anim_f' + str(i) + '.png')
            temp_frame = pygame.transform.scale(temp_frame, (24, 42))
            self.idle_frames_r.append(temp_frame)
            # self.idle_frames_r[i] = pygame.transform.scale2x(self.idle_frames_r[i])

            temp_frame = pygame.image.load(
                frame_img + 'knight_f_run_anim_f' + str(i) + '.png')
            temp_frame = pygame.transform.scale(temp_frame, (24, 42))
            self.run_frames_f.append(temp_frame)
            # self.run_frames_f[i] = pygame.transform.scale2x(self.run_frames_f[i])

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
