import pygame
import random

# initialise new pygame
pygame.init()

# create a display window
display_w = 800
display_h = 600
game_display = pygame.display.set_mode((display_w, display_h))

# create background
bg = pygame.image.load("space_bg.png")

# setting title and icon
pygame.display.set_caption("Space Invaders")
game_icon = pygame.image.load("flower.png")
pygame.display.set_icon(game_icon)

# player
player_img = pygame.image.load("witch_pusheen_transparent.png")
player_w = 200
player_h = 200
player_x = display_w / 2 - player_w / 2
player_y = display_h / 2
playerX_change = 0
playerY_change = 0
player_speed = 1


def player(x, y):
    game_display.blit(player_img, (x, y))


# movement booleans
go_right = False
go_left = False

# enemy
enemy_img = pygame.image.load("octopus.png")
enemy_w = 64
enemy_h = 64
enemy_x = random.randint(0, display_w - enemy_w)
enemy_y = 20
enemy_speed = 0.2
enemyX_change = enemy_speed
enemyY_change = 25


def enemy(x, y):
    game_display.blit(enemy_img, (x, y))


# create a game loop for runtime functionality
is_running = True
while is_running:

    # create solid background colour using RGB values
    game_display.fill((224, 187, 228))
    # create background
    game_display.blit(bg, (0, 0))

    for event in pygame.event.get():

        # quit event
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.KEYDOWN:
            # moving along x axis
            if event.key == pygame.K_RIGHT:
                go_right = True
            if event.key == pygame.K_LEFT:
                go_left = True

        if event.type == pygame.KEYUP:
            # stop moving when arrow key is released
            if event.key == pygame.K_RIGHT:
                go_right = False
            if event.key == pygame.K_LEFT:
                go_left = False

        if go_right:
            playerX_change = player_speed
        elif go_left:
            playerX_change = -player_speed
        else:
            playerX_change = 0

    # update player position
    player_x += playerX_change
    player_y += playerY_change

    # prevent player from moving off screen
    if player_x <= 0:
        player_x = 0
    if player_x >= display_w - player_w:
        player_x = display_w - player_w

    if player_y <= 0:
        player_y = 0
    if player_y >= display_h - player_h:
        player_y = display_h - player_h

    # enemy horizontal movement
    enemy_x += enemyX_change

    # prevent enemy from moving off screen by redirecting him
    # enemy moves downwards upon hitting boundary
    if enemy_x <= 0:
        enemyX_change = enemy_speed
        enemy_y += enemyY_change
    if enemy_x >= display_w - enemy_w:
        enemyX_change = -enemy_speed
        enemy_y += enemyY_change

    # draw player in new position
    player(player_x, player_y)

    # draw enemy in new position
    enemy(enemy_x, enemy_y)

    pygame.display.update()
