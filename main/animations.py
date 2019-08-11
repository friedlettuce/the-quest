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
        rect_anim = rect
        if self.facing_right:
            rect_anim.centerx = int(rect_anim.centerx +
                                    (rect_anim.centerx / 6))
            '''rect_anim.centery = int(rect_anim.centery +
                                    (rect_anim.centery / 30))'''

        self.screen.blit(self.image, rect)


class HitAnimation(Animation):

    def __init__(self, screen, game_settings):
        super().__init__(screen, game_settings.hit_path,
                         game_settings.hit_frames, game_settings.hit_size,)
