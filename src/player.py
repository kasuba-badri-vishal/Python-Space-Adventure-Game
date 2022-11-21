import pygame
from config import *

class Player:
    def __init__(self, xpos, ypos, imagepath, multiplayer):
        self.xpos = xpos
        self.ypos = ypos
        self.health = 10
        self.poweredup = False
        self.surface = pygame.image.load(imagepath).convert_alpha()
        self.multiplayer = multiplayer

    def move(self, direction):
        if direction == 'l':
            if self.xpos > 40:
                self.xpos -= 20
        elif direction == 'r':
            if self.xpos < WIDTH - 40:
                self.xpos += 20
        elif direction == 'u':
            if self.ypos > 40:
                self.ypos -= 20
        elif direction == 'd':
            if self.ypos < HEIGHT - 50:
                self.ypos += 20
    
    def got_hurt(self):
        self.health -= 20

    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))


class Bullet:
    def __init__(self, xpos, ypos, imagepath):
        self.xpos = xpos
        self.ypos = ypos
        self.isactive = True
        self.surface = pygame.image.load(imagepath).convert_alpha()

    def move(self, direction):
        if direction == 'u':
            if self.ypos > 0:
                self.ypos -= 10
            else:
                self.isactive = False
        elif direction == 'd':
            if self.ypos < HEIGHT - 10:
                self.ypos += 10
            else:
                self.isactive = False    
        elif direction == 'r':
            if self.xpos > 0:
                self.xpos += 10
            else:
                self.isactive = False
        elif direction == 'l':
            if self.xpos < WIDTH - 10:
                self.xpos -= 10
            else:
                self.isactive = False

    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))


class Enemy1:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()
        # self.rect = self.surface.get_rect(center=(self.xpos, self.ypos))
        self.life = 3

    def move(self):
        if self.ypos < HEIGHT - 20:
            self.ypos += .25
        else:
            self.isalive = False

    def display(self, screen):
        if self.life == 3:
            screen.blit(self.surface1, (self.xpos, self.ypos))
        elif self.life == 2:
            screen.blit(self.surface2, (self.xpos, self.ypos))
        elif self.life == 1:
            screen.blit(self.surface3, (self.xpos, self.ypos))

    # def explode(self):


class Enemy2:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3, imagepath4, imagepath5):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.surface1 = pygame.image.load(imagepath1).convert_alpha()

        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()

        self.surface4 = pygame.image.load(imagepath4).convert_alpha()

        self.surface5 = pygame.image.load(imagepath5).convert_alpha()
        # self.rect = self.surface.get_rect(center=(self.xpos, self.ypos))
        self.life = 30

    def move(self):
        if self.ypos < HEIGHT - 20:
            self.ypos += .25
        else:
            self.isalive = False

    def display(self, screen):
        if self.life >= 25:
            screen.blit(self.surface1, (self.xpos, self.ypos))
        elif self.life >= 20:
            screen.blit(self.surface2, (self.xpos, self.ypos))
        elif self.life >= 15:
            screen.blit(self.surface3, (self.xpos, self.ypos))
        elif self.life >= 10:
            screen.blit(self.surface4, (self.xpos, self.ypos))
        else:
            screen.blit(self.surface5, (self.xpos, self.ypos))

    # def explode(self):


class Enemy3:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3, imagepath4):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()
        self.surface4 = pygame.image.load(imagepath4).convert_alpha()

        self.life = 100

    def move(self):
        if self.ypos < HEIGHT - 20:
            self.ypos += .01
        else:
            self.isalive = False

    def display(self, screen):
        if self.life >= 75:
            screen.blit(self.surface1, (self.xpos, self.ypos))
        elif self.life >= 50:
            screen.blit(self.surface2, (self.xpos, self.ypos))
        elif self.life >= 25:
            screen.blit(self.surface3, (self.xpos, self.ypos))
        else:
            screen.blit(self.surface4, (self.xpos, self.ypos))

    # def explode(self):