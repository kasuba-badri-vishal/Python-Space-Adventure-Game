"""
This Python file contains the Declaration of the objects used in the Pygame
Objects used in the pygame are Player, Bullet, Enemy1 and Enemy2 (Boss)
The Declared class objects would be used in translating the objects from one place to other, update their health information and also delete them

"""
import pygame
from config import *


"""
Same Class Declaration is adopted for both multiplayer and single player games
The Class contains 2 methods
* move()     - To move the player with translational constraints applied
* got_hurt() - To update the health status of the player
* display()  - To Render and display the player and health status on the Screen
"""
class Player:

    ### Class Constructor to initialize the Player class object with the respective player object parameters
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


    ### Method of Player object, to move the player UP, DOWN, LEFT, RIGHT using the keys and the translational constraints
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
    

    ### When Player gets hit by bullet, his health state is updated by this method
    def got_hurt(self):
        self.health -= 20


    ### Displaying the Life of the Player and also rendering him onto the  window screen using blit
    def display(self, screen):
        if(self.multiplayer==0):
            life_val = str(self.life)
            lineinfo = self.font.render(life_val, False, (255, 255, 255))
            screen.blit(lineinfo, (self.xpos + self.surface.get_width() / 2.8, self.ypos + self.surface.get_height() / 1.1))
        screen.blit(self.surface, (self.xpos, self.ypos))




"""
Declaration of Bullet class, which are used by Boss Enemy, Player1 and multi-players to emit bullets and hurt rivals
The Class contains 2 methods
* move()     - To move the bullet with translational constraints applied
* display()  - To Render and display the bullet and the current position of it on the Screen
"""
class Bullet:

    ### Class Constructor to initialize the Bullet class object with the respective bullet object parameters
    def __init__(self, xpos, ypos, imagepath):
        self.xpos = xpos
        self.ypos = ypos
        self.isactive = True
        self.surface = pygame.image.load(imagepath).convert_alpha()
        self.centerx = self.xpos + self.surface.get_width() / 2
        self.centery = self.ypos + self.surface.get_height() / 2


    ### Method of Bullet object, to move the bullet UP, DOWN, LEFT, RIGHT using the keys and the translational constraints
    ### Note that bullets can travel only in one direction and are suitably used
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


    ### Displaying the bullet by rendering it onto the  window screen using blit
    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))




"""
Enemy object declaration which is used in singly player game
The Class contains 2 methods
* move()     - To move the Enemy with translational constraints applied
* display()  - To Render and display the enemy and  also rendering current state of the enemy
"""
class Enemy1:

    ### Class Constructor to initialize the Enemy1 class object with the respective Enemy1 object parameters
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3):
        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.life = 3

        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()

    
    ### Method of Enemy1 object, to move the player UP, DOWN, LEFT, RIGHT using the keys and the translational constraints
    def move(self):
        if self.ypos < HEIGHT - 20:
            self.ypos += .25
        else:
            self.isalive = False


    ### Displaying the Enemy1 by rendering him onto the  window screen using blit
    def display(self, screen):
        if self.life == 3:
            screen.blit(self.surface1, (self.xpos, self.ypos))
        elif self.life == 2:
            screen.blit(self.surface2, (self.xpos, self.ypos))
        elif self.life == 1:
            screen.blit(self.surface3, (self.xpos, self.ypos))




"""
Boss Enemy object declaration which is used in singly player game, where it gets more power abilities with reduced span of life
The Class contains 2 methods
* move()     - To move the Enemy2 with translational constraints applied
* display()  - To Render and display the boss enemy and health status on the Screen
"""
class Enemy2:


    ### Class Constructor to initialize the Enemy2 class object with the respective Enemy2 object parameters
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

        
    ### Method of Enemy2 object, to move the boss enemy UP, DOWN, LEFT, RIGHT using the keys and the translational constraints
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



    ### Displaying the Life of the Boss Enemy and also rendering him onto the window screen using blit
    def display(self, screen):
        life_val = str(self.life)
        lineinfo = self.font.render(life_val, False, (255, 255, 255))


        ### Based on his lifespan, the boss enemy gets some aura of power, strength and glows with reduced life span
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
