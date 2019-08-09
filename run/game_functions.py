import sys, pygame


def check_events(player):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player.moving_right = True
                player.weapon.face_right()
            elif event.key == pygame.K_LEFT:
                player.moving_left = True
                player.weapon.face_left()

        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                player.moving_right = False
                player.facing_right = True
            if event.key == pygame.K_LEFT:
                player.moving_left = player.facing_right = False


def update_screen(game_settings, screen, clock, forrest, player):

    screen.fill(game_settings.bg_color)

    forrest.blitme()
    player.blitme()

    pygame.display.flip()
    clock.tick(game_settings.fps)