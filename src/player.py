import pygame
from config import *

class Player:
    def __init__(self, xpos, ypos, imagepath, multiplayer):
        self.xpos = xpos
        self.ypos = ypos
        self.health = 10
        self.life = 100
        self.font = pygame.font.Font(ALBA_FONT, 30)
        self.surface = pygame.image.load(imagepath).convert_alpha()
        self.multiplayer = multiplayer

        self.centerx = self.xpos + self.surface.get_width() / 2
        self.centery = self.ypos + self.surface.get_height() / 2

    def move(self, direction):
        if direction == 'l':
            if self.xpos > 40 or (self.multiplayer==1 and self.xpos < WIDTH):
                self.xpos -= 20
        elif direction == 'r' or (self.multiplayer==2 and self.xpos > WIDTH):
            if self.xpos < WIDTH - 40:
                self.xpos += 20
        elif direction == 'u':
            if self.ypos > 40:
                self.ypos -= 20
        elif direction == 'd':
            if self.ypos < HEIGHT - 50:
                self.ypos += 20

        self.centerx = self.xpos + self.surface.get_width() / 2
        self.centery = self.ypos + self.surface.get_height() / 2
    
    def got_hurt(self):
        self.health -= 20

    def display(self, screen):
        if(self.multiplayer==0):
            life_val = str(self.life)
            lineinfo = self.font.render(life_val, False, (255, 255, 255))
            screen.blit(lineinfo, (self.xpos + self.surface.get_width() / 2.8, self.ypos + self.surface.get_height() / 1.1))
        screen.blit(self.surface, (self.xpos, self.ypos))


class Bullet:
    def __init__(self, xpos, ypos, imagepath):
        self.xpos = xpos
        self.ypos = ypos
        self.isactive = True
        self.surface = pygame.image.load(imagepath).convert_alpha()
        self.centerx = self.xpos + self.surface.get_width() / 2
        self.centery = self.ypos + self.surface.get_height() / 2

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
        self.centery = self.ypos + self.surface.get_height() / 2

    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))


class Enemy1:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.life = 3

        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()


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



class Enemy2:

    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3, imagepath4):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.life = 320

        self.font = pygame.font.Font(ALBA_FONT, 50)

        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()
        self.surface4 = pygame.image.load(imagepath4).convert_alpha()
        self.presentsurface = self.surface1

        self.centerx = self.xpos + self.presentsurface.get_width() / 2
        self.centery = self.ypos + self.presentsurface.get_height() / 2

        

    def move(self, direction):

        if direction == 'd':
            if self.ypos < HEIGHT:
                self.ypos += .1
                self.centery = self.ypos + self.presentsurface.get_height() / 2
            else:
                self.isalive = False
        elif direction == 'u':

            if self.ypos > 20:
                self.ypos -= .1
                self.centery = self.ypos + self.presentsurface.get_height() / 2

        elif direction == 'r':
            if self.xpos + self.presentsurface.get_width() < WIDTH:
                self.xpos += 10
                self.centerx = self.xpos + self.presentsurface.get_width() / 2

        elif direction == 'l':
            if self.xpos - self.presentsurface.get_width() > 0:
                self.xpos -= 10
                self.centerx = self.xpos + self.presentsurface.get_width() / 2

    def display(self, screen):
        life_val = str(self.life)
        lineinfo = self.font.render(life_val, False, (255, 255, 255))

        if self.life >= 300:
            self.presentsurface = self.surface1
        elif self.life >= 200:
            self.presentsurface = self.surface2
        elif self.life >= 100:
            self.presentsurface = self.surface3
        else:
            self.presentsurface = self.surface4

        screen.blit(self.presentsurface, (self.xpos, self.ypos))
        screen.blit(lineinfo, (self.xpos + self.presentsurface.get_width() / 2.8, self.ypos))
