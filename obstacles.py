import pygame
import random
from utilities.resources import get_resource
from utilities.settings import *

CACTUSES = [
    pygame.image.load(get_resource("cactus_01.png")),
    pygame.image.load(get_resource("cactus_02.png")),
    pygame.image.load(get_resource("cactus_03.png")),
    pygame.image.load(get_resource("cactus_04.png")),
    pygame.image.load(get_resource("cactus_05.png")),
    pygame.image.load(get_resource("cactus_07.png")),
    pygame.image.load(get_resource("cactus_08.png")),
    pygame.image.load(get_resource("cactus_09.png")),
]

GROUND_POS = 390
CACTUS_IMAGE = random.choice(CACTUSES)
CACTUS_RECT = CACTUS_IMAGE.get_rect(bottomleft=(SCREENSIZE[0], GROUND_POS))


def draw_cactus(screen):
    global CACTUS_IMAGE, CACTUS_RECT

    if CACTUS_RECT.right <= 0:
        CACTUS_IMAGE = random.choice(CACTUSES)
        CACTUS_RECT = CACTUS_IMAGE.get_rect(bottomleft=(SCREENSIZE[0], GROUND_POS))

    # pygame.draw.rect(screen, "red", CACTUS_RECT, 3)

    screen.blit(CACTUS_IMAGE, CACTUS_RECT)
    CACTUS_RECT.x -= GROUND_SPEED


def get_cactus_rect():
    return CACTUS_RECT


def reset_cactus():
    global CACTUS_IMAGE, CACTUS_RECT

    CACTUS_IMAGE = random.choice(CACTUSES)
    CACTUS_RECT = CACTUS_IMAGE.get_rect(bottomleft=(SCREENSIZE[0], GROUND_POS))


def bird(screen):
    pass
