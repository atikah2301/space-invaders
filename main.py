import pygame

# initialise new pygame
pygame.init()

# create a display window
display_w = 800
display_h = 600
game_display = pygame.display.set_mode((display_w, display_h))

# setting title and icon
pygame.display.set_caption("Space Invaders")
game_icon = pygame.image.load("flower.png")
pygame.display.set_icon(game_icon)

# player
player_img = pygame.image.load("witch_pusheen_transparent.png")
player_x = display_w/2 - 90
player_y = display_h/2

def player():
    game_display.blit(player_img, (player_x, player_y))

# create a game loop for runtime functionality
is_running = True
while is_running:
    # quit game by closing window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

    # create solid background colour using RGB values
    game_display.fill((224, 187, 228))

    player()

    pygame.display.update()