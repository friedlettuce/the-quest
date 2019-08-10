import sys, pygame


def check_events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.right()
            elif event.key == pygame.K_LEFT:
                player.left()
            elif event.key == pygame.K_q:
                player.use_weapon()
            elif event.key == pygame.K_v:
                player.weapon.toggled = not player.weapon.toggled

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
            if event.key == pygame.K_LEFT:
                player.moving_left = False


def update_screen(game_settings, screen, clock, forrest, player):

    screen.fill(game_settings.bg_color)

    forrest.blitme()
    player.blitme()

    pygame.display.flip()
    clock.tick(game_settings.fps)