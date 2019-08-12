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


class IceSpell(Animation):

    def __init__(self, screen, rect, game_settings):
        super().__init__(screen, game_settings.ice_path,
                         game_settings.ice_frames, game_settings.ice_size)

        self.rect = rect.copy()
        self.finished = False
        self.collision = False
        self.collisionRect = 0

        self.speed = game_settings.ice_speed

    def reset(self, rect):
        self.rect = rect.copy()
        self.frame = 0
        self.finished = False
        self.collision = False

    def collisionRectSet(self, collisionRect):
        self.rect.centerx = collisionRect.centerx

    def update(self):
        if (self.rect.right < self.screen.get_rect().left or
                self.rect.left > self.screen.get_rect().right):
            self.finished = True

        if not self.finished:
            if self.facing_right:
                self.image = self.frames_r[self.frame]
            else:
                self.image = self.frames_l[self.frame]

            if self.frame == 10:
                self.finished = True

            if not self.collision:
                if self.facing_right:
                    self.rect.centerx += self.speed
                else:
                    self.rect.centerx -= self.speed

        self.frame += 1

    def blitme(self):
        self.screen.blit(self.image, self.rect)



