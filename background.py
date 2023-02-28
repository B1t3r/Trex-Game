import pygame
from utilities.resources import get_resource

MOUNTAINS = pygame.image.load(get_resource("mountains.png"))


def draw_background(screen):
    screen.blit(MOUNTAINS, (-500, -50))
