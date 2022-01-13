import sys, pygame
from pygame.sprite import Group
import os

from settings import Settings
import game_functions as gf

from background import ForestBackground, WelcomeScreen
import characters


def character_creation(char_select):
    weapon = '' # input('-> ').lower()
    if char_select == 'wizard':
        weapon = 'g'
    elif char_select == 'elf':
        weapon = 'd'
    elif char_select == 'knight':
        'ks'

    return weapon


def run_game():
    player = ''
    mobs = Group()

    pygame.init()
    pygame.mixer.init()
    clock = pygame.time.Clock()
    game_settings = Settings()

    print(os.getcwd())

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dungeon Capture")

    welc_screen = WelcomeScreen(screen, game_settings)

    char_select = ''
    # Setup for character
    while True:
        char_select = gf.check_welc(welc_screen)
        if char_select:
            print(char_select)
            weapon = character_creation(char_select)
            break
        welc_screen.draw()
        pygame.display.flip()

    if char_select == 'wizard':
        player = characters.Wizard(game_settings, screen, weapon)
    elif char_select == 'elf':
        player = characters.Hero(game_settings, screen, 'elf', weapon)
    else:
        player = characters.Hero(game_settings, screen, 'knight', weapon)

    pygame.mixer.music.unload()
    forrest = ForestBackground(game_settings, screen)

    while True:

        gf.check_events(forrest, player, mobs)

        for mob in mobs.sprites():
            player.check_collision(mob)
        player.update()
        forrest.update()

        if player.hp <= 0:
            game_settings.playing = False

        gf.update_mobs(game_settings, screen, mobs, player)

        gf.update_screen(game_settings, screen, clock, forrest, player, mobs)


run_game()

