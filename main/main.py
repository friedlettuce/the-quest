import sys, pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf

from background import ForestBackground, WelcomeScreen
import characters


def character_creation(char_select):
    '''
    if char_select == 'wizard':
        print('Choose green staff[g] or red staff[r]')
    elif char_select == 'elf':
        print('Choose axe[a], baton[b], cleaver[c], duel sword[d]')
    elif char_select == 'knight':
        print('Choose big sword[bs], big hammer[bh], knight sword[ks]')
    else:
        exit(1)
    '''
    # weapon = input('-> ').lower()
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
    clock = pygame.time.Clock()
    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dungeon Capture")

    welc_screen = WelcomeScreen(screen, game_settings)
    forrest = ForestBackground(game_settings, screen)

    char_select = ''
    # Setup for character
    while True:
        char_select = gf.check_welc(welc_screen)
        if char_select:
            char_select = char_select.lower()
            weapon = character_creation(char_select.lower())
            break
        welc_screen.draw()
        pygame.display.flip()

    if char_select == 'wizard':
        player = characters.Wizard(game_settings, screen, weapon)
    elif char_select == 'elf':
        player = characters.Hero(game_settings, screen, 'elf', weapon)
    else:
        player = characters.Hero(game_settings, screen, 'knight', weapon)

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

