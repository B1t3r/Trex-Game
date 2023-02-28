import pygame
import sys

pygame.init()
pygame.mixer.init()

from utilities.settings import *
from game_assets.game_over_screen import draw_game_over
from game_assets.background import draw_background
from game_assets.clouds import draw_clouds
from game_assets.ground import draw_ground
from game_assets.trex import draw_trex, get_trex_rect, trex_jump
from game_assets.obstacles import draw_cactus, get_cactus_rect, reset_cactus

# game window settings
SCREEN = pygame.display.set_mode(SCREENSIZE)
pygame.display.set_caption(GAMETITLE)
CLOCK = pygame.time.Clock()
GAME_OVER = False


def main():
    # game loop
    while True:
        check_events()

        if GAME_OVER:
            draw_game_over(SCREEN)

        else:
            # SCREEN.fill(SKYCOLOR)

            # draw mountains and sky
            draw_background(SCREEN)
            draw_clouds(SCREEN)

            # draw ground and cactuses
            draw_ground(SCREEN)
            draw_cactus(SCREEN)

            # draw trex
            draw_trex(SCREEN)

            check_collisions()

        pygame.display.update()
        CLOCK.tick(FPS)


def check_events():
    global GAME_OVER

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            close_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            close_game()

        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            if GAME_OVER:
                reset_cactus()
                GAME_OVER = False
            else:
                trex_jump()


def check_collisions():
    global GAME_OVER

    trex_rect = get_trex_rect()
    cactus_rect = get_cactus_rect()

    if trex_rect.colliderect(cactus_rect):
        GAME_OVER = True


def close_game():
    pygame.quit()
    sys.exit()


main()
