import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
import random

# screen properties
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# declaring colors
green = pygame.Color('#99ff66')
red = pygame.Color('#ff6644')
background = pygame.Color('#ffffff')
blue = pygame.Color('#6666ff')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.RUNNING = True
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.size = 25
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(pygame.Color(self.r, self.g, self.b))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(self.size*5, SCREEN_HEIGHT//2)  # set starting location
        self.u = 5  # initially moving to the right
        self.v = 0

    def update_position(self, pressed_keys):
        self.rect.move_ip(self.u, self.v)  # gives the player movement

    def update_direction(self, pressed_keys):  # logic to control snake
        if pressed_keys[K_UP] and self.v != 5:
            self.v = -5
            self.u = 0
        if pressed_keys[K_DOWN] and self.v != -5:
            self.v = 5
            self.u = 0
        if pressed_keys[K_LEFT] and self.u != 5:
            self.u = -5
            self.v = 0
        if pressed_keys[K_RIGHT] and self.u != -5:
            self.u = 5
            self.v = 0

    def check_boundary(self):  # check if snake has hit boundary
        if self.rect.left < 0:
            self.RUNNING = False
            return self.RUNNING
        if self.rect.right > SCREEN_WIDTH:
            self.RUNNING = False
            return self.RUNNING
        if self.rect.top < 0:
            self.RUNNING = False
            return self.RUNNING
        if self.rect.bottom > SCREEN_HEIGHT:
            self.RUNNING = False
            return self.RUNNING
        self.RUNNING = True
        return self.RUNNING


class Fruit(pygame.sprite.Sprite):
    def __init__(self):
        super(Fruit, self).__init__()
        self.size = 25
        self.surf = pygame.Surface((self.size, self.size))  # make the surface a square
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.surf.fill(background)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(200, 200)
        pygame.draw.circle(self.surf, pygame.Color(self.r, self.g, self.b), (12.5, 12.5), 12.5)  # draw a circle on the square

    def change_location(self):
        self.current_location = self.surf.get_rect()  # move the fruit when eaten
        self.rect.left = random.randrange(0, 800, 25)
        self.rect.top = random.randrange(0, 600, 25)
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        pygame.draw.circle(self.surf, pygame.Color(self.r, self.g, self.b), (12.5, 12.5), 12.5)  # draw a circle on the square


class Body(pygame.sprite.Sprite):
    def __init__(self, starting_left_loc, starting_top_loc):
        super(Body, self).__init__()
        self.size = 25
        self.surf = pygame.Surface((self.size, self.size))
        self.r = random.randint(0, 255)
        self.g = random.randint(0, 255)
        self.b = random.randint(0, 255)
        self.surf.fill(pygame.Color(self.r, self.g, self.b))
        self.rect = self.surf.get_rect()
        self.rect.left = starting_left_loc
        self.rect.top = starting_top_loc
        self.u = 0
        self.v = 0
