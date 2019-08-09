import sys, pygame
from settings import Settings
import game_functions as gf

from background import Background

from characters.knight import Knight


def run_game():
    pygame.init()
    clock = pygame.time.Clock()
    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dungeon Capture")

    forrest = Background(
        game_settings, screen, '../resources/backgrounds/country.png')

    player = Knight(game_settings, screen)

    while True:

        gf.check_events(player)
        player.update()
        gf.update_screen(game_settings, screen, clock, forrest, player)


run_game()
