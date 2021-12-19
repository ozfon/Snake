#!/usr/local/bin/python3
'''
Snake game
@author: Scott Gardner
'''

# Import standard modules
import pygame
from settings import Player, Fruit, SCREEN_WIDTH, SCREEN_HEIGHT, background

# Import pygame.locals for easier access to key coordinates
# Updated to conform to flake8 and black standards
from pygame.locals import (
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_q,
)

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

# Create groups to hold sprites
fruit_group = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
fruit_group.add(fruit)
all_sprites.add(fruit_group)
all_sprites.add(player)

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

    screen.fill((background))

    pressed_keys = pygame.key.get_pressed()
    OUTSIDE = player.check_boundary()
    player.update_position(pressed_keys)

    if player.rect[0] % 25 == 0 and player.rect[1] % 25 == 0:
        player.update_direction(pressed_keys)

    if not OUTSIDE:
        RUNNING = False

    if pygame.sprite.spritecollideany(player, fruit_group):
        fruit.change_location()

    # draw all sprites
    for entity in all_sprites:
        screen.blit(entity.surf, entity.rect)
    pygame.display.flip()
