#!/usr/local/bin/python3
'''
Snake game
@author: Scott Gardner
'''

# Import standard modules
import pygame
import numpy as np
from settings import Player, Fruit, Body, SCREEN_WIDTH, SCREEN_HEIGHT, background

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_q,
)


def grab_location():
    i = 0
    for entity in snake_group:
        loc_x[i] = entity.rect.center[0]
        loc_y[i] = entity.rect.center[1]
        i += 1
    return loc_x, loc_y


def grab_diff(loc_x, loc_y):
    for i in range(len(snake_group.sprites())-1):
        diff_x[i] = loc_x[i]-loc_x[i+1]
        diff_y[i] = loc_y[i]-loc_y[i+1]
    return diff_x, diff_y


def update_position(entity):
    entity.rect.move_ip(entity.u, entity.v)  #


def update_direction(entity, x, y, i):  #
    if diff_x[i] > 0 and diff_y[i] == 0:
        entity.v = 0
        entity.u = 5
    elif diff_x[i] < 0 and diff_y[i] == 0:
        entity.v = 0
        entity.u = -5
    elif diff_y[i] > 0 and diff_x[i] == 0:
        entity.u = 0
        entity.v = 5
    elif diff_y[i] < 0 and diff_x[i] == 0:
        entity.u = 0
        entity.v = -5


# Initialize pygame
pygame.init()

# Define constants for the screen width and height
FPS = 60

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
grid_size = 25
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake")

clock = pygame.time.Clock()
RUNNING = True

# Instantiate player
player = Player()
fruit = Fruit()
body = Body(grid_size*4, SCREEN_HEIGHT//2)

# Create groups to hold sprites
fruit_group = pygame.sprite.Group()
snake_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
body_group = pygame.sprite.Group()
snake_butt = pygame.sprite.Group()
added_body = pygame.sprite.Group()

snake_group.add(player)
snake_group.add(body)
body_group.add(body)
body = Body(grid_size*3, SCREEN_HEIGHT//2)

snake_group.add(body)
body_group.add(body)
snake_butt.add(body)
fruit_group.add(fruit)
all_sprites.add(snake_group)
all_sprites.add(fruit_group)

# Main loop
while RUNNING:
    clock.tick(FPS)

    # Look at every event in the queue
    for event in pygame.event.get():
        # Did the user hit a key?
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                RUNNING = False
            if event.key == K_q:
                RUNNING = False
        elif event.type == QUIT:
            RUNNING = False

    loc_x = np.zeros(len(snake_group.sprites()))
    loc_y = np.zeros(len(snake_group.sprites()))
    diff_x = np.zeros(len(snake_group.sprites()) - 1)
    diff_y = np.zeros(len(snake_group.sprites()) - 1)

    screen.fill((background))

    loc_x, loc_y = grab_location()
    diff_x, diff_y = grab_diff(loc_x, loc_y)

    i = 0
    for entity in body_group:
        update_direction(entity, diff_x, diff_y, i)
        update_position(entity)
        i += 1

    pressed_keys = pygame.key.get_pressed()
    OUTSIDE = player.check_boundary()
    player.update_position(pressed_keys)

    if player.rect[0] % 25 == 0 and player.rect[1] % 25 == 0:
        player.update_direction(pressed_keys)

    if not OUTSIDE:
        RUNNING = False

    if pygame.sprite.spritecollideany(player, fruit_group):
        fruit.change_location()
        for entity in snake_butt:
            new_body_left = entity.rect.left
            new_body_top = entity.rect.top
            u_last_body = entity.u
            v_last_body = entity.v
            if entity.u > 0:
                new_body_left -= 25
            elif entity.u < 0:
                new_body_left += 25
            elif entity.v > 0:
                new_body_top -= 25
            elif entity.v < 0:
                new_body_top += 25
        snake_butt.remove(body)
        body = Body(new_body_left, new_body_top)
        body_group.add(body)
        all_sprites.add(body)
        snake_butt.add(body)
        snake_group.add(body)
        added_body.add(body)

    if pygame.sprite.spritecollideany(player, added_body):
        RUNNING = False

# draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
