import numpy as np
import pygame
from pygame import mixer


class Player:
    def __init__(self, xpos, ypos, imagepath):
        self.xpos = xpos
        self.ypos = ypos
        self.health = 10
        self.poweredup = False
        self.surface = pygame.image.load(imagepath).convert_alpha()

    def move(self, direction):

        if direction == 'l':
            if self.xpos > 0:
                self.xpos -= 20
        elif direction == 'r':
            if self.xpos < 1780:
                print(self.xpos)
                self.xpos += 20
        elif direction == 'u':
            if self.ypos > 0:
                self.ypos -= 20
        elif direction == 'd':
            if self.ypos < 950:
                self.ypos += 20

    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))


class Bullet:
    def __init__(self, xpos, ypos, imagepath):
        self.xpos = xpos
        self.ypos = ypos
        self.isactive = True
        self.surface = pygame.image.load(imagepath).convert_alpha()
        self.centerx = self.xpos + self.surface.get_width() / 2
        self.centery = self.ypos + self.surface.get_height() / 2
        #print(f"This is topmidx :{self.topmidx}")
        #print(f"This is topmidy :{self.topmidy}")
        #print(f"This is self.xpos :{self.xpos}")
        #print(f"This is self.ypos :{self.ypos}")


    def move(self, direction):
        if direction == 'u':
            if self.ypos > 0:
                self.ypos -= 10
            else:
                self.isactive = False
        elif direction == 'd':
            if self.ypos < 950:
                self.ypos += 10
            else:
                self.isactive = False
        self.centery = self.ypos + self.surface.get_height() / 2

    def display(self, screen):
        screen.blit(self.surface, (self.xpos, self.ypos))


class Enemy3:
    def __init__(self, xpos, ypos, imagepath1, imagepath2, imagepath3, imagepath4):

        self.xpos = xpos
        self.ypos = ypos
        self.isalive = True
        self.life = 320

        self.surface1 = pygame.image.load(imagepath1).convert_alpha()
        self.surface2 = pygame.image.load(imagepath2).convert_alpha()
        self.surface3 = pygame.image.load(imagepath3).convert_alpha()
        self.surface4 = pygame.image.load(imagepath4).convert_alpha()
        self.presentsurface = self.surface1

        self.font = pygame.font.Font('fonts/alba/ALBAS___.TTF', 50)
        print(self.surface1.get_width())
        print(self.surface1.get_height())

        self.centerx = self.xpos + self.presentsurface.get_width() / 2
        self.centery = self.ypos + self.presentsurface.get_height() / 2

    def move(self, direction):

        if direction == 'd':
            if self.ypos < 950:
                self.ypos += .1
                self.centery = self.ypos + self.presentsurface.get_height() / 2
            else:
                self.isalive = False
        elif direction == 'u':

            if self.ypos > 0:
                self.ypos -= .1
                self.centery = self.ypos + self.presentsurface.get_height() / 2

        elif direction == 'r':
            if self.xpos + self.presentsurface.get_width() < 1080:
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
        CANVAS.blit(lineinfo, (self.xpos, self.ypos))



pygame.init()

WIDTH = 1920
HEIGHT = 1080
FPS = 60
CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("ADVENTURE TIME")  # Name of the game
clock = pygame.time.Clock()  # Initialize clock object
count = 0
phase = 'instructions'
ctdcount = 0
phase = 'enemy3'

flip =100
# BACKGROUND IMAGE
bg = pygame.image.load('images/stars.jpg').convert()

# BACKGROUND MUSIC
mixer.music.load("audio/background/single.wav")
mixer.music.play(-1)

# INITIALIZE PLAYER
player1 = Player(xpos=1000, ypos=500, imagepath='images/player/player1.png')

# INITIALIZE BULLET LIST
bull_arr = []
enemy_arr = []

# Infested Earth
font1 = pygame.font.Font('fonts/alba/ALBAS___.TTF', 90)
line1 = font1.render('THE EARTH IS UNDER AN ALIEN ATTACK', False, (255, 255, 255))
line2 = font1.render(' YOU ARE OUR ONLY HOPE MAVERICK', False, (255, 255, 255))
line3 = font1.render('  DONT LET THEM REACH THE WALL', False, (255, 255, 255))

# Intro
font2 = pygame.font.Font('fonts/alba/ALBAS___.TTF', 90)
line4 = font2.render('GET READY', False, (255, 255, 255))
line5 = font2.render('USE ARROW KEYS TO MOVE', False, (255, 255, 255))
line6 = font2.render('USE SPACE TO FIRE', False, (255, 255, 255))
line7 = font2.render('USE CTRL ONCE YOUR POWER BAR IS FULL', False, (255, 255, 255))

font3 = pygame.font.Font('fonts/alba/ALBAS___.TTF', 500)
three = font3.render('3', False, (255, 255, 255))
two = font3.render('2', False, (255, 255, 255))
one = font3.render('1', False, (255, 255, 255))

# PHASE : Enemy1

x = 40 + (WIDTH / 10) * np.arange(10)

x = list(x)
print(x)
flag = 1
timer = 0
layers = 0

singleRunning = True
while singleRunning:

    # To Close the window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            singleRunning = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(xpos=player1.xpos + 50, ypos=player1.ypos, imagepath='images/bullets/bullet1.png')
                bull_arr.append(bullet)

            if event.key == pygame.K_t:
                enemy = Enemy3(xpos=((WIDTH-600)/ 2), ypos=+100, imagepath1='images/enemy/enemy3/fb1.png',
                               imagepath2='images/enemy/enemy3/fb2.png',
                               imagepath3='images/enemy/enemy3/fb3.png', imagepath4='images/enemy/enemy3/fb4.png')
                enemy_arr.append(enemy)


    CANVAS.blit(bg, (0, 0))

    click = pygame.mouse.get_pressed()
    if click[0]:
        ticks = pygame.time.get_ticks()
        print(f"this is the time {ticks}")
        print(pygame.mouse.get_pos())

    if pygame.time.get_ticks() > 31400:
        if count == 0:
            # print("aaa gaya")
            count = 1
    tick = pygame.time.get_ticks()









    player1.display(screen=CANVAS)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.move(direction='l')
    elif keys[pygame.K_RIGHT]:
        player1.move(direction='r')
    elif keys[pygame.K_UP]:
        player1.move(direction='u')
    elif keys[pygame.K_DOWN]:
        player1.move(direction='d')

    # CANVAS.blit(bull1, (WIDTH / 2 - 50, HEIGHT / 5))

    for bullet in bull_arr:
        bullet.move(direction='u')

        if bullet.isactive == False:
            bull_arr.remove(bullet)
        else:
            bullet.display(screen=CANVAS)

    for enemy in enemy_arr:
        if enemy.life > 300:
            enemy.move(direction='d')
        elif enemy.life > 200:
            #enemy.move(direction='l')

            if flip <0:
                enemy.move(direction='r')
                flip +=1
            elif flip >0:
                enemy.move(direction='l')
                flip -=1
            elif flip==0:
                if np.random.binomial(1,.5) >=.5:
                    flip=100
                else:
                    flip=-100
            print(f'This is flip: {flip}')

        elif enemy.life > 100:




            enemy.move(direction='d')
        enemy.display(screen=CANVAS)

    #print(f"This is enemy array : {enemy_arr}")
    #print(f'This is bullet array : {bull_arr}')
    for b in bull_arr:
        for e in enemy_arr:
            if len(bull_arr) > 0 and len(enemy_arr) > 0:

                hcon1 = b.centerx + b.surface.get_width()/2 > e.centerx - e.presentsurface.get_width()/2 +30
                hcon2 = b.centerx - b.surface.get_width()/2 < e.centerx + e.presentsurface.get_width()/2 -30

                vcon1 = abs(b.centery - b.surface.get_height()/2 - (e.centery + e.presentsurface.get_height()/2)) <5

                if hcon1 and hcon2 and vcon1:
                    e.life -= 1
                    print(f"This is b.ypos {b.ypos}, e.ypos {e.ypos}")
                    if b in bull_arr:
                        bull_arr.remove(b)
                    if (e.life == 0):
                        enemy_arr.remove(e)


    # print(f"This is length of bull_array : {len(bull_arr)}")

    pygame.display.update()  # To refresh every time while loop runs
    clock.tick(60)  # To run update 60 frames in 1 second
