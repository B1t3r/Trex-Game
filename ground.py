import pygame
from utilities.resources import get_resource
from utilities.settings import *

GROUND_1 = pygame.image.load(get_resource("ground.png"))
GROUND_1_RECT = GROUND_1.get_rect()

GROUND_2 = pygame.image.load(get_resource("ground.png"))
GROUND_2_RECT = GROUND_2.get_rect(midleft=GROUND_1_RECT.midright)


def draw_ground(screen):
    if GROUND_1_RECT.right <= 0:
        GROUND_1_RECT.left = GROUND_2_RECT.right

    if GROUND_2_RECT.right <= 0:
        GROUND_2_RECT.left = GROUND_1_RECT.right

    screen.blit(GROUND_1, GROUND_1_RECT)
    GROUND_1_RECT.x -= GROUND_SPEED

    # pygame.draw.rect(screen, "red", GROUND_1_RECT, 3)

    screen.blit(GROUND_2, GROUND_2_RECT)
    GROUND_2_RECT.x -= GROUND_SPEED

    # pygame.draw.rect(screen, "blue", GROUND_2_RECT, 3)
