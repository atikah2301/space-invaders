import pygame


class Character:
    pygame.init()

    def __init__(self, img="",
                 w=0, h=0, x=0, y=0,
                 x_change=0, y_change=0,
                 speed=0):
        self.img = pygame.image.load(img)
        self.w = w
        self.h = h
        self.x = x
        self.y = y
        self.x_change = x_change
        self.y_change = y_change
        self.speed = speed

    def reposition(self, x, y):
        from Game import Game
        Game.display.blit(self.img, (x, y))
