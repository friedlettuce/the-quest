import pygame
import building
import os


class WelcomeScreen:

    def __init__(self, screen, game_settings):
        self.screen = screen
        self.background = Landscape(game_settings, screen,
                                    game_settings.forestFile)

        pygame.mixer.music.load('resources/backgrounds/Lost-Jungle.wav')
        pygame.mixer.music.play(-1)

        large_text = pygame.font.SysFont('harrington', 75, True)
        self.text = large_text.render("The Quest", True, (128, 128, 128))
        self.textRect = self.text.get_rect()
        self.textRect.center = ((game_settings.screen_width / 2),
                                (game_settings.screen_height / 2) - 30)

        offset = int(game_settings.screen_width * .09765625)

        self.wbutton = Button(game_settings, screen, 'wizard')
        self.wbutton.rect.centery = self.screen.get_rect().centery + 140
        self.wbutton.rect.centerx = int(self.screen.get_rect().right / 3) + offset

        self.kbutton = Button(game_settings, screen, 'knight')
        self.kbutton.rect.centery = self.screen.get_rect().centery + 140
        # Setting equal to centerx of screen was offset left, just added half distance between wizard pos.
        self.kbutton.rect.centerx = int(self.screen.get_rect().right / 2) + offset

        self.ebutton = Button(game_settings, screen, 'elf')
        self.ebutton.rect.centery = self.screen.get_rect().centery + 140
        self.ebutton.rect.centerx = int(self.screen.get_rect().right * 2/3) + offset

        self.char_buttons = [self.wbutton, self.kbutton, self.ebutton]

    def draw(self):
        self.background.blitme()
        self.screen.blit(self.text, self.textRect)
        self.wbutton.blitme()
        self.kbutton.blitme()
        self.ebutton.blitme()


class ForestBackground:

    def __init__(self, game_settings, screen):
        self.landscape1 = Landscape(game_settings, screen,
                                    game_settings.forestFile)
        self.landscape2 = Landscape(game_settings, screen,
                                    game_settings.forestFile)
        self.landscape2.rect.left = self.landscape2.right()

        if os.path.exists('resources/backgrounds/nature1.wav'):
            print("Path exists")
        else:
            print("Path non-existent")
        pygame.mixer.music.load('resources/backgrounds/nature1.wav')
        pygame.mixer.music.play(-1)

        self.moving_left = self.moving_right = False
        self.speed = 0

    def left(self, speed):
        self.moving_left = True
        self.speed = speed

    def right(self, speed):
        self.moving_right = True
        self.speed = speed

    def update(self):
        if self.moving_right:
            self.landscape1.rect.centerx += self.speed
            self.landscape2.rect.centerx += self.speed

            if self.landscape1.rect.left <= self.landscape1.screen_rect.left:
                self.landscape1.rect.left = self.landscape1.right()
            elif self.landscape2.rect.left <= self.landscape2.screen_rect.left:
                self.landscape2.rect.left = self.landscape2.right()

        elif self.moving_left:
            self.landscape1.rect.centerx -= self.speed
            self.landscape2.rect.centerx -= self.speed

            if self.landscape1.rect.right >= self.landscape1.screen_rect.right:
                self.landscape1.rect.right = self.landscape1.left()
            elif self.landscape2.rect.right >= self.landscape2.screen_rect.right:
                self.landscape2.rect.right = self.landscape1.left()

    def blitme(self):
        self.landscape1.blitme()
        self.landscape2.blitme()
        # self.new_building.blitme()


class Landscape:

    def __init__(self, game_settings, screen, file):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.image = pygame.transform.scale(
            pygame.image.load(file),
            [game_settings.screen_width, game_settings.screen_height])

        self.rect = self.image.get_rect()
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

    def right(self):
        return self.screen_rect.left
    def left(self):
        return self.screen_rect.right

    def blitme(self):
        self.screen.blit(self.image, self.rect)


class Button:

    def __init__(self, game_settings, screen, msg):
        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.button_color = game_settings.button_color
        self.text_color = game_settings.btxt_color
        self.font = pygame.font.SysFont(None, game_settings.button_font)
        self.text = msg

        self.rect = pygame.Rect(0, 0, game_settings.button_width,
                                game_settings.button_height)
        self.rect.center = self.screen_rect.center

        self.msg_image = self.font.render(
            msg, True, self.text_color, self.button_color)

    def blitme(self):
        self.screen.blit(self.msg_image, self.rect)
