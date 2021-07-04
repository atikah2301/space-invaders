import pygame
from pygame import mixer


class Game:
    pygame.init()

    # create a display window
    display_w = 800
    display_h = 600
    display = pygame.display.set_mode((display_w, display_h))

    # create background
    bg = pygame.image.load("Assets\Images\space_bg.png")

    # game over
    game_over_font = pygame.font.Font("Assets\Images\\batman_forever.ttf", 64)

    # score
    score = 0
    score_font = pygame.font.Font("Assets\Images\\batman_forever.ttf", 32)
    score_x = 10
    score_y = 10

    @staticmethod
    def setup():
        # setting title and icon
        pygame.display.set_caption("Space Invaders")
        game_icon = pygame.image.load("Assets\Images\spaceship.png")
        pygame.display.set_icon(game_icon)

        # load background music
        mixer.music.load("Assets\Audio\\background.wav")
        mixer.music.play(-1)