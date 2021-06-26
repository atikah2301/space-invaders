import pygame
import random
import math

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
enemy_img = []
enemy_x = []
enemy_y = []
enemyX_change = []
enemyY_change = []
enemy_w = 64
enemy_h = 64
enemy_speed = 0.2
enemy_count = 6

for i in range(enemy_count):
    enemy_img.append(pygame.image.load("ufo.png"))
    enemy_x.append(random.randint(0, display_w - enemy_w))
    enemy_y.append(20)
    enemyX_change.append(enemy_speed)
    enemyY_change.append(25)

# bullet
bullet_img = pygame.image.load("bullet.png")
bullet_x = 0
bullet_y = 500  # display_h - player_y
bulletX_change = 0
bulletY_change = 1.5
bullet_fired = False

score = 0

def player(x, y):
    game_display.blit(player_img, (x, y))


def enemy(x, y, i):
    game_display.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_fired
    bullet_fired = True
    game_display.blit(bullet_img, (x + 16, y))


def isCollided(enemy_x, enemy_y, bullet_x, bullet_y):
    x_sq = math.pow(enemy_x - bullet_x, 2)
    y_sq = math.pow(enemy_y - bullet_y, 2)
    distance = math.sqrt(x_sq + y_sq)

    if distance < 30:
        return True
    else:
        return False


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
                # checking the bool prevents us from re-setting bullet
                if bullet_fired is False:
                    # bullet_x allows bullet to have its own path
                    # instead of following the player's x value
                    bullet_x = player_x
                    fire_bullet(bullet_x, bullet_y)

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

    # enemy movement
    for i in range(enemy_count):
        # enemy movement - horizontal
        enemy_x[i] += enemyX_change[i]
        # enemy movement - redirection before moving off screen
        if enemy_x[i] <= 0:
            enemyX_change[i] = enemy_speed
            enemy_y[i] += enemyY_change[i]
        elif enemy_x[i] >= display_w - enemy_w:
            enemyX_change[i] = -enemy_speed
            enemy_y[i] += enemyY_change[i]

        # reset bullet and enemy upon collision with enemy
        collision = isCollided(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            bullet_y = 500
            bullet_fired = False
            score += 1
            enemy_x[i] = random.randint(0, display_w - enemy_w)
            enemy_y[i] = 20

        # draw enemy in new position
        enemy(enemy_x[i], enemy_y[i], i)

    # reset bullet upon moving off screen
    if bullet_y <= 5:
        bullet_y = 500
        bullet_fired = False

    # bullet motion
    if bullet_fired:
        fire_bullet(bullet_x, bullet_y)
        bullet_y -= bulletY_change

    # draw player in new position
    player(player_x, player_y)

    pygame.display.update()
