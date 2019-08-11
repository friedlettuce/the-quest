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
        rect_anim = rect.copy()
        rect_anim.left = rect_anim.right

        self.screen.blit(self.image, rect_anim)
