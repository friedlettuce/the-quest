import sys, pygame
from pygame.sprite import Group

from settings import Settings
import game_functions as gf

from background import Background
import characters


def character_creation():
    print("Wizard, Elf, or Knight")
    char_select = input('-> ').lower()

    if char_select == 'wizard':
        print('Choose green staff[g] or red staff[r]')
    elif char_select == 'elf':
        print('Choose axe[a], baton[b], cleaver[c], duel sword[d]')
    elif char_select == 'knight':
        print('Choose big sword[bs], big hammer[bh], knight sword[ks]')
    else:
        exit(1)

    weapon = input('-> ').lower()
    return char_select, weapon


def run_game():
    char_select, weapon = character_creation()
    player = ''
    mobs = Group()

    pygame.init()
    clock = pygame.time.Clock()
    game_settings = Settings()

    screen = pygame.display.set_mode(
        (game_settings.screen_width, game_settings.screen_height))
    pygame.display.set_caption("Dungeon Capture")

    forrest = Background(
        game_settings, screen, '../resources/backgrounds/forest3.png')

    if char_select == 'wizard':
        player = characters.Wizard(game_settings, screen, weapon)
    elif char_select == 'elf':
        player = characters.Elf(game_settings, screen, weapon)
    else:
        player = characters.Knight(game_settings, screen, weapon)

    while True:

        gf.check_events(player, mobs)

        for mob in mobs.sprites():
            player.check_collision(mob)
        player.update()

        if player.hp <= 0:
            print('Game Over')
            sys.exit()

        gf.update_mobs(game_settings, screen, mobs, player)

        gf.update_screen(game_settings, screen, clock, forrest, player, mobs)


run_game()

