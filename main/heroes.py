import pygame

from weapon import KnightWeapon, WizardWeapon, ElfWeapon


class Player:

    def __init__(self, game_settings, screen, hero):
        self.screen = screen
        self.game_settings = game_settings
        self.hero = hero

        self.moving_right = False
        self.moving_left = False
        self.facing_right = True

        self.frame = 0
        self.idle_frames_r = []
        self.idle_frames_l = []
        self.run_frames_f = []
        self.run_frames_b = []

        self.image = ''
        self.load_frames()

        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = self.screen_rect.centerx / 3
        self.rect.bottom = self.screen_rect.bottom - 32

        self.center = float(self.rect.centerx)

    def load_frames(self):
        self.image = pygame.image.load(
            '../resources/' + self.hero + '/' + self.hero + '_m_idle_f0.png')
        # self.image = pygame.transform.scale2x(self.image)
        self.image = pygame.transform.scale(self.image, (24, 42))

        # Stores frames for knight
        for i in range(4):
            frame_img = '../resources/' + self.hero + '/'

            # Loads and resizes for idle frames facing right
            temp_frame = pygame.image.load(
                frame_img + self.hero + '_m_idle_f' + str(i) + '.png')
            temp_frame = pygame.transform.scale(temp_frame, (24, 42))
            self.idle_frames_r.append(temp_frame)
            # self.idle_frames_r[i] = pygame.transform.scale2x(self.idle_frames_r[i])

            temp_frame = pygame.image.load(
                frame_img + self.hero + '_m_run_f' + str(i) + '.png')
            temp_frame = pygame.transform.scale(temp_frame, (24, 42))
            self.run_frames_f.append(temp_frame)
            # self.run_frames_f[i] = pygame.transform.scale2x(self.run_frames_f[i])

        for img in self.run_frames_f:
            self.run_frames_b.append(pygame.transform.flip(img, True, False))
        for img in self.idle_frames_r:
            self.idle_frames_l.append(pygame.transform.flip(img, True, False))

    def right(self):
        self.moving_right = self.facing_right = True
        self.moving_left = False
        self.weapon.face_right()

    def left(self):
        self.moving_right = self.facing_right = False
        self.moving_left = True
        self.weapon.face_left()

    def use_weapon(self):
        self.weapon.using = True

    def update(self):

        if self.moving_right:
            self.image = self.run_frames_f[self.frame]

            if self.rect.centerx < self.screen_rect.width - 16:
                self.center += self.game_settings.player_speed

        elif self.moving_left:
            self.image = self.run_frames_b[self.frame]

            if self.rect.centerx > 17:
                self.center -= self.game_settings.player_speed

        elif self.facing_right is False:
            self.image = self.idle_frames_l[self.frame]

        else:
            self.image = self.idle_frames_r[self.frame]

        self.rect.centerx = self.center
        self.frame += 1
        self.frame %= self.game_settings.anicycle

        self.weapon.update(
            self.rect.centerx, self.rect.centery, self.facing_right)

    def blitme(self):
        self.weapon.blitme()
        self.screen.blit(self.image, self.rect)


class Knight(Player):

    def __init__(self, game_settings, screen, weapon, hero='knight'):
        super().__init__(game_settings, screen, hero)
        self.weapon = ''

        if weapon == 'ks' or weapon == 'bh' or weapon == 'ks':
            self.weapon = KnightWeapon(screen, self.rect, weapon)
        else:
            self.weapon = KnightWeapon(screen, self.rect)


class Wizard(Player):

    def __init__(self, game_settings, screen, weapon, hero='wizard'):
        super().__init__(game_settings, screen, hero)
        self.weapon = ''

        if weapon == 'g' or weapon == 'r':
            self.weapon = WizardWeapon(screen, self.rect, weapon)
        else:
            self.weapon = WizardWeapon(screen, self.rect)

    def update(self):
        '''self.weapon.update(
            self.rect.centerx, self.rect.centery, self.facing_right)'''
        super().update()


class Elf(Player):

    def __init__(self, game_settings, screen, weapon, hero='elf'):
        super().__init__(game_settings, screen, hero)
        self.weapon = ''

        if weapon == 'a' or weapon == 'b' or weapon == 'c' or weapon == 'd':
            self.weapon = ElfWeapon(screen, self.rect, weapon)
        else:
            self.weapon = ElfWeapon(screen, self.rect)

    def update(self):
        '''self.weapon.update(
            self.rect.centerx, self.rect.centery, self.facing_right)'''
        super().update()
