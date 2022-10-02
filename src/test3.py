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
        if self.ypos < 950:

            # print("I am toh moving rey baba")
            # print(f"This is self.rect.centery : {self.rect.centery}")
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
        if self.ypos < 950:

            # print("I am toh moving rey baba")
            # print(f"This is self.rect.centery : {self.rect.centery}")
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
        if self.ypos < 950:

            # print("I am toh moving rey baba")
            # print(f"This is self.rect.centery : {self.rect.centery}")
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
            if event.key == pygame.K_q:
                for j in range(10):
                    enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1='images/enemy/alien.png',
                                   imagepath2='images/enemy/alien2.png', imagepath3='images/enemy/alien3.png')
                    enemy_arr.append(enemy)
            if event.key == pygame.K_w:
                x = 130 + ((WIDTH - 180) / 9) * np.arange(9)
                x = list(x)
                for j in range(9):
                    enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1='images/enemy/alien.png',
                                   imagepath2='images/enemy/alien2.png', imagepath3='images/enemy/alien3.png')
                    enemy_arr.append(enemy)
            if event.key == pygame.K_e:
                x = 130 + ((WIDTH - 180) / 4) * np.arange(4)
                x = list(x)
                for j in range(4):
                    enemy = Enemy2(xpos=x[j], ypos=-20, imagepath1='images/enemy/enemy2/sp1.png',
                                   imagepath2='images/enemy/enemy2/sp2.png', imagepath3='images/enemy/enemy2/sp3.png',
                                   imagepath4='images/enemy/enemy2/sp5.png', imagepath5='images/enemy/enemy2/sp4.png')
                    enemy_arr.append(enemy)
            if event.key == pygame.K_t:
                enemy = Enemy3(xpos=((WIDTH-600)/ 2), ypos=-20, imagepath1='images/enemy/enemy3/fb1.png',
                               imagepath2='images/enemy/enemy3/fb2.png',
                               imagepath3='images/enemy/enemy3/fb3.png', imagepath4='images/enemy/enemy3/fb4.png')
                enemy_arr.append(enemy)


    CANVAS.blit(bg, (0, 0))

    click = pygame.mouse.get_pressed()
    if click[0]:
        ticks = pygame.time.get_ticks()
        print(ticks)

    if pygame.time.get_ticks() > 31400:
        if count == 0:
            # print("aaa gaya")
            count = 1
    tick = pygame.time.get_ticks()

    if tick < 11600:
        phase = 'infestedearth'
    elif tick > 11600 and tick < 29000:
        phase = 'instructions'
    elif tick > 29000 and tick < 31400:
        phase = 'threetwoone'
    elif tick > 31400:
        phase = 'enemy1'
    elif tick > 130300:
        phase = 'enemy3'

    if phase == 'infestedearth':
        CANVAS.blit(line1, ((200, HEIGHT / 10)))
        CANVAS.blit(line2, ((200, HEIGHT / 10 + 150)))
        CANVAS.blit(line3, ((200, HEIGHT / 10 + 300)))


    elif phase == 'instructions':
        CANVAS.blit(line4, ((740, HEIGHT / 10)))
        CANVAS.blit(line5, (400, HEIGHT / 10 + 150))
        CANVAS.blit(line6, (600, HEIGHT / 10 + 300))
        CANVAS.blit(line7, (140, HEIGHT / 10 + 450))
    elif phase == 'threetwoone':
        # print("I am inn baby!!!")

        if ctdcount < 50:
            CANVAS.blit(three, (WIDTH / 2 - 50, HEIGHT / 5))
            ctdcount += 1
            # print(ctdcount)
        elif ctdcount < 100:
            CANVAS.blit(two, (WIDTH / 2 - 50, HEIGHT / 5))
            ctdcount += 1
            # print(ctdcount)
        else:
            CANVAS.blit(one, (WIDTH / 2 - 50, HEIGHT / 5))
    elif phase == 'enemy1':

        if (flag == 1) or (timer > 620 and flag == 3):
            x = 40 + (WIDTH / 10) * np.arange(10)
            x = list(x)
            for j in range(10):
                enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1='images/enemy/alien.png',
                               imagepath2='images/enemy/alien2.png', imagepath3='images/enemy/alien3.png')
                enemy_arr.append(enemy)

            if flag == 1:
                flag = 2
            else:
                flag = 4
            # prevtimer=-1

        elif (timer > 310 and flag == 2) or (timer > 920 and flag == 4):

            x = 130 + ((WIDTH - 180) / 9) * np.arange(9)
            x = list(x)
            for j in range(9):
                enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1='images/enemy/alien.png',
                               imagepath2='images/enemy/alien2.png', imagepath3='images/enemy/alien3.png')
                enemy_arr.append(enemy)
            if flag == 2:
                flag = 3
            else:
                flag = 5

        #print(f'This is timer : {timer}')
        timer += 1

    elif phase == 'enemy3':


        enemy = Enemy3(xpos=(WIDTH/2), ypos=-20, imagepath1='images/enemy/enemy3/fb1.png',imagepath2='images/enemy/enemy3/fb2.png',
                       imagepath3='images/enemy/enemy3/fb3.png', imagepath4='images/enemy/enemy3/fb4.png')
        enemy_arr.append(enemy)

        ## Remove all the other enemies





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
        enemy.move()
        enemy.display(screen=CANVAS)

    for b in bull_arr:
        for e in enemy_arr:
            if len(bull_arr) > 0 and len(enemy_arr) > 0:
                if abs(b.xpos - e.xpos) < 60:
                    if b.ypos - 50 < e.ypos:
                        e.life -= 1
                        print(f"This is b.ypos {b.ypos}, e.ypos {e.ypos}")
                        if b in bull_arr:
                            bull_arr.remove(b)
                        if (e.life == 0):
                            enemy_arr.remove(e)

    # print(f"This is length of bull_array : {len(bull_arr)}")

    pygame.display.update()  # To refresh every time while loop runs
    clock.tick(60)  # To run update 60 frames in 1 second
