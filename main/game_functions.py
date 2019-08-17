import sys, pygame
import characters


def check_events(background, player, mobs):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.right()
                # background.right(player.speed)
            elif event.key == pygame.K_LEFT:
                player.left()
                # background.left(player.speed)
            elif event.key == pygame.K_q:
                player.use_weapon()
            elif event.key == pygame.K_w and player.name == 'wizard':
                if not player.spell.active:
                    player.use_weapon()
                    player.use_spell()
            elif event.key == pygame.K_e and player.name == 'wizard':
                player.switch_spell()
            elif event.key == pygame.K_v:
                player.weapon.toggled = not player.weapon.toggled

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
                # background.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False
                # background.moving_right = False


def check_welc():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


def update_mobs(game_settings, screen, mobs, player):
    # Adding mobs
    if len(mobs) == 0:
        mobs.add(characters.BigDemon(game_settings, screen))

    # Updating mobs
    for mob in mobs.sprites():
        mob.check_collision(player)
        mob.update(player)

        if mob.hp <= 0:
            mobs.remove(mob)

    for mob in mobs.copy():
        if mob.rect.right <= 0:
            mobs.remove(mob)


def update_screen(game_settings, screen, clock, forrest, player, mobs):

    forrest.blitme()

    for mob in mobs.sprites():
        mob.blitme()
    player.blitme()

    pygame.display.flip()
    clock.tick(game_settings.fps)
