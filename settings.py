import pygame
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
)
import random

# from pygame.locals import (
#    K_UP,
# )

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
green = pygame.Color('#99ff66')
red = pygame.Color('#ff6644')
background = pygame.Color('#ffffff')


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.RUNNING = True
        self.size = 25
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill((green))
        self.rect = self.surf.get_rect()
        self.rect.move_ip(SCREEN_HEIGHT//2, SCREEN_WIDTH//2)
        self.u = 5
        self.v = 0

    def update_position(self, pressed_keys):
        self.rect.move_ip(self.u, self.v)

    def update_direction(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.v = -5
            self.u = 0
        if pressed_keys[K_DOWN]:
            self.v = 5
            self.u = 0
        if pressed_keys[K_LEFT]:
            self.u = -5
            self.v = 0
        if pressed_keys[K_RIGHT]:
            self.u = 5
            self.v = 0

    def check_boundary(self):
        if self.rect.left < 0:
            self.RUNNING = False
            return self.RUNNING
        if self.rect.right > SCREEN_WIDTH:
            self.RUNNING = False
            return self.RUNNING
        if self.rect.top <= 0:
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
        self.surf = pygame.Surface((self.size, self.size))
        self.surf.fill(background)
        self.rect = self.surf.get_rect()
        self.rect.move_ip(200, 200)
        pygame.draw.circle(self.surf, red, (12.5, 12.5), 12.5)

    def change_location(self):
        self.current_location = self.surf.get_rect()
        self.rect.left = random.randrange(0, 800, 25)
        self.rect.top = random.randrange(0, 600, 25)
