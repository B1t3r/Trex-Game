import pygame
from utilities.resources import get_resource
from utilities.settings import *

GAME_OVER_FONT = pygame.font.Font(get_resource("dogicabold.ttf"), 40)
GAME_OVER_TEXT = GAME_OVER_FONT.render("Game Over", False, "white")
GAME_OVER_TEXT_RECT = GAME_OVER_TEXT.get_rect(center=(SCREENSIZE[0] / 2, 180))

PRESS_SPACE_FONT = pygame.font.Font(get_resource("dogica.ttf"), 20)
PRESS_SPACE_TEXT = PRESS_SPACE_FONT.render("Press SPACE to Restart", False, "white")
PRESS_SPACE_TEXT_RECT = PRESS_SPACE_TEXT.get_rect(midtop=GAME_OVER_TEXT_RECT.midbottom)


def draw_game_over(screen):
    screen.fill(SKYCOLOR)
    screen.blit(GAME_OVER_TEXT, GAME_OVER_TEXT_RECT)
    screen.blit(PRESS_SPACE_TEXT, PRESS_SPACE_TEXT_RECT)
