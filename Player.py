from Character import Character
import pygame


class Player(Character):
    pygame.init()
    go_right = False
    go_left = False

    def set_dir_bool(self, event):
        if event.key == pygame.K_RIGHT:
            self.go_right = True
        if event.key == pygame.K_LEFT:
            self.go_left = True

    def reset_dir_bool(self, event):
        if event.key == pygame.K_RIGHT:
            self.go_right = False
        if event.key == pygame.K_LEFT:
            self.go_left = False

    def set_dir_value(self):
        if self.go_right:
            self.x_change = self.speed
        elif self.go_left:
            self.x_change = -self.speed
        else:
            self.x_change = 0

    def move(self):
        from Game import Game
        # update player position
        self.x += self.x_change
        self.y += self.y_change

        # prevent player from moving off screen
        if self.x <= 0:
            self.x = 0
        if self.x >= Game.display_w - self.w:
            self.x = Game.display_w - self.w

        if self.y <= 0:
            self.y = 0
        if self.y >= Game.display_h - self.h:
            self.y = Game.display_h - self.h



