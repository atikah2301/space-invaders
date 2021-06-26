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
game_icon = pygame.image.load("spaceship.png")
pygame.display.set_icon(game_icon)

# player
player_img = pygame.image.load("spaceship.png")
player_w = 64
player_h = 64
player_x = display_w / 2 - player_w / 2
player_y = display_h - player_h - 50
playerX_change = 0
playerY_change = 0
player_speed = 0.5

# movement booleans
go_right = False
go_left = False

# enemy
enemy_img = pygame.image.load("ufo.png")
enemy_w = 64
enemy_h = 64
enemy_x = random.randint(0, display_w - enemy_w)
enemy_y = 20
enemy_speed = 0.2
enemyX_change = enemy_speed
enemyY_change = 25

# bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500 #display_h - player_y
bulletX_change = 0
bulletY_change = 2
bullet_fired = False

def player(x, y):
    game_display.blit(player_img, (x, y))

def enemy(x, y):
    game_display.blit(enemy_img, (x, y))

def fire_bullet(x, y):
    global bullet_fired
    bullet_fired = True
    game_display.blit(bullet_img, (x + 16, y))


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

            # bullet
            if event.key == pygame.K_SPACE:
                if bullet_fired is False:
                    bullet_x = player_x
                    fire_bullet(player_x, bullet_y)

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

    # bullet motion
    if bullet_y <= 5:
        bullet_y = 500
        bullet_fired = False

    if bullet_fired:
        fire_bullet(player_x, bullet_y)
        bullet_y -= bulletY_change

    # draw player in new position
    player(player_x, player_y)

    # draw enemy in new position
    enemy(enemy_x, enemy_y)

    pygame.display.update()
