import pygame
import random
import math
from pygame import mixer

# initialise new pygame
pygame.init()

# create a display window
display_w = 800
display_h = 600
game_display = pygame.display.set_mode((display_w, display_h))

# create background
bg = pygame.image.load("Assets\Images\space_bg.png")

# background music
mixer.music.load("Assets\Audio\\background.wav")
mixer.music.play(-1)

# setting title and icon
pygame.display.set_caption("Space Invaders")
game_icon = pygame.image.load("Assets\Images\spaceship.png")
pygame.display.set_icon(game_icon)

# player
player_img = pygame.image.load("Assets\Images\spaceship.png")
player_w = 64
player_h = 64
player_x = display_w / 2 - player_w / 2
player_y = display_h - player_h - 50
playerX_change = 0
playerY_change = 0
player_speed = 0.75

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
enemy_xspeed = 0.3
enemy_yspeed = 75
enemy_count = 6

# add enemies to display
for i in range(enemy_count):
    enemy_img.append(pygame.image.load("Assets\Images\\ufo.png"))
    enemy_x.append(random.randint(0, display_w - enemy_w))
    enemy_y.append(70)
    enemyX_change.append(enemy_xspeed)
    enemyY_change.append(enemy_yspeed)

# bullet
bullet_img = pygame.image.load("Assets\Images\\bullet.png")
bullet_x = 0
bullet_y = 500  # display_h - player_y
bullet_speed = 4
bulletX_change = 0
bulletY_change = bullet_speed
bullet_fired = False

# score
score = 0
score_font = pygame.font.Font("Assets\Images\\batman_forever.ttf", 32)
score_x = 10
score_y = 10

# game over
game_over_font = pygame.font.Font("Assets\Images\\batman_forever.ttf", 64)


def game_over(x, y):
    game_over_display = game_over_font.render("GAME OVER", True, (255, 255, 255))
    game_display.blit(game_over_display, (x, y))


def show_score(x, y):
    score_display = score_font.render(f"Points: {score}", True, (255, 255, 255))
    game_display.blit(score_display, (x, y))


def player(x, y):
    game_display.blit(player_img, (x, y))


def enemy(x, y, i):
    game_display.blit(enemy_img[i], (x, y))


def fire_bullet(x, y):
    global bullet_fired
    bullet_fired = True
    game_display.blit(bullet_img, (x + 16, y))


def is_collided(x1, y1, x2, y2):
    x_sq = math.pow(x1 - x2, 2)
    y_sq = math.pow(y1 - y2, 2)
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
                    bullet_sound = mixer.Sound("Assets\Audio\laser.wav")
                    bullet_sound.play()
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

    # enemy activity
    for i in range(enemy_count):

        # game over
        if enemy_y[i] > 400:
            for j in range(enemy_count):
                enemy_y[j] = 1000
            game_over(display_w / 2 - 235, display_h / 2 - 60)
            break

        # enemy movement - horizontal
        enemy_x[i] += enemyX_change[i]

        # enemy movement - redirection before moving off screen
        if enemy_x[i] <= 0:
            enemyX_change[i] = enemy_xspeed
            enemy_y[i] += enemyY_change[i]
        elif enemy_x[i] >= display_w - enemy_w:
            enemyX_change[i] = -enemy_xspeed
            enemy_y[i] += enemyY_change[i]

        # reset bullet and enemy upon collision with enemy
        collision = is_collided(enemy_x[i], enemy_y[i], bullet_x, bullet_y)
        if collision:
            collision_sound = mixer.Sound("Assets\Audio\explosion.wav")
            collision_sound.play()
            bullet_y = 500
            bullet_fired = False
            score += 1
            enemy_x[i] = random.randint(0, display_w - enemy_w)
            enemy_y[i] = 50

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
    show_score(score_x, score_y)

    pygame.display.update()
