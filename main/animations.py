import pygame


class Animation:

    def __init__(self, screen, path, frames, size):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.frames = frames
        self.frame = 0

        self.image = ''
        self.frames_l = []
        self.frames_r = []

        self.facing_right = True

        for frame in range(self.frames):
            self.frames_r.append((
                pygame.transform.scale(
                    pygame.image.load(path + str(frame) + '.png'), size)))

            flipped_frame = pygame.transform.flip(self.frames_r[frame], 0, 0)
            self.frames_l.append(flipped_frame)

        self.image = self.frames_r[self.frame]

    def left(self):
        self.facing_right = False

    def right(self):
        self.facing_right = True

    def update(self):
        self.frame += 1
        self.frame %= self.frames

        if self.facing_right:
            self.image = self.frames_r[self.frame]
        else:
            self.image = self.frames_l[self.frame]

    def blitme(self, rect):
        self.screen.blit(self.image, rect)


class Ice(Animation):

    def __int__(self, rect, game_settings):
        super().__init__(game_settings.screen,
                         game_settings.frames, game_settings.size)
        self.rect = rect
        self.finished = False
        self.collision = False

        self.ice_speed = game_settings.ice_speed
        self.ice_damage = game_settings.ice_damage

    def reset(self, rect):
        self.rect = rect
        self.finished = False
        self.collision = False
        self.collisionRect = 0

    def collision(self, collisionRect):
        if self.facing_right:
            self.rect.right = self.collisionRect.left
        else:
            self.rect.left = self.collisionRect.right

    def update(self):
        super().update()

        if not self.finished:
            if self.facing_right:
                self.rect.right = self.collisionRect.left
            else:
                self.rect.left = self.collisionRect.right

    def blitme(self):
        self.screen.blit(self.image, self.rect)



