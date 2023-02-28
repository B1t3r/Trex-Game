import pygame
from utilities.resources import get_resource

TREX_RUN = [
    pygame.image.load(get_resource("trex_run_01.png")),
    pygame.image.load(get_resource("trex_run_02.png"))
]

TREX_JUMP = pygame.image.load(get_resource("trex_jump.png"))
JUMP_SOUND = pygame.mixer.Sound(get_resource("jump.wav"))
pygame.mixer.Sound.set_volume(JUMP_SOUND, 0.2)

GROUND_POS = 260
FRAME = 0
ANIM_SPEED = 0.3
GRAVITY = 0
ON_GROUND = True
TREX_IMAGE = TREX_RUN[FRAME]
TREX_RECT = TREX_IMAGE.get_rect(y=GROUND_POS)


def draw_trex(screen):
    global FRAME, TREX_IMAGE, GRAVITY, ON_GROUND

    FRAME += ANIM_SPEED
    if FRAME >= len(TREX_RUN):
        FRAME = 0

    TREX_IMAGE = TREX_RUN[int(FRAME)]

    # Apply GRAVITY
    GRAVITY += 1
    TREX_RECT.y += GRAVITY
    if TREX_RECT.y >= GROUND_POS:
        GRAVITY = 0
        TREX_RECT.y = GROUND_POS
        ON_GROUND = True

    screen.blit(TREX_IMAGE, TREX_RECT)


def trex_jump():
    global GRAVITY, ON_GROUND

    if not ON_GROUND:
        return

    GRAVITY -= 20
    ON_GROUND = False
    JUMP_SOUND.play()


def get_trex_rect():
    return TREX_RECT.inflate(-100, -50)
