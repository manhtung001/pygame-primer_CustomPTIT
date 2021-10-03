import pygame
import random
from pygame.locals import *


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pygame.image.load('assets/img/jet.png').convert()
        self.image.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.image.get_rect(center=(10, 300))
        self.is_bat_tu = False
        self.is_x2 = False

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            self.rect.move_ip(0, -5)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 5)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-5, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

        # Keep player on the screen
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > 800:
            self.rect.right = 800
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= 600:
            self.rect.bottom = 600


class Enemy(pygame.sprite.Sprite):
    def __init__(self, type):
        super(Enemy, self).__init__()
        self.type = type

        if self.type == "bullet":
            self.image = pygame.image.load('assets/img/missile.png').convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
            self.speed = random.randint(5, 10)
            self.rect = self.image.get_rect(
                center=(random.randint(820, 900), random.randint(0, 600)))
            self.weight = 1

        if self.type == "stone":
            self.image = pygame.image.load('assets/img/stone.jpg').convert()
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
            self.speed = random.randint(5, 10)
            self.rect = self.image.get_rect(
                center=(random.randint(820, 900), random.randint(0, 600)))
            self.weight = 3

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


# Coin big
# Gift

class Item(pygame.sprite.Sprite):
    def __init__(self, type):
        super(Item, self).__init__()
        self.time_eat_last = 0
        # 100
        self.time_eat_max = 0;
        if type == "coin":
            self.image = pygame.image.load('assets/img/coin.png').convert()
            self.speed = random.randint(5, 10)
            self.image.set_colorkey((255, 255, 255), RLEACCEL)
            self.rect = self.image.get_rect(
                center=(random.randint(820, 900), random.randint(0, 600))
            )

        # if type == "stone":

    def update(self):
        self.rect.move_ip(-self.speed, 0)
        if self.rect.right < 0:
            self.kill()


class Cloud(pygame.sprite.Sprite):
    def __init__(self):
        super(Cloud, self).__init__()
        self.image = pygame.image.load('assets/img/cloud.png').convert()
        self.image.set_colorkey((0, 0, 0), RLEACCEL)
        self.rect = self.image.get_rect(center=(
            random.randint(820, 900), random.randint(0, 600))
        )

    def update(self):
        self.rect.move_ip(-5, 0)
        if self.rect.right < 0:
            self.kill()
