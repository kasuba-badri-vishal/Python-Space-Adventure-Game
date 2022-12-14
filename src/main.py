'''
* Adventure PYGAME as part of course project of CS699 Software Lab 
* Has Single player and Multi player components and is basically a space ranger shooting game with multiple levels
*
'''
import os
import pygame
import time
import numpy as np
from pygame.locals import HWSURFACE, DOUBLEBUF, RESIZABLE
from config import *
from player import *
from utils import *



def multi_player_game(CANVAS, game_bg):

    # # BACKGROUND MUSIC
    background_music("multi_player.mp3")

    clock = pygame.time.Clock()

    # INITIALIZE PLAYERS
    multi_player1 = Player(xpos=10, ypos=30, imagepath=os.path.join(PLAYER_IMAGES,'multi_player1.png'), multiplayer=1)
    multi_player2 = Player(xpos=7*WIDTH/8, ypos=HEIGHT/2, imagepath=os.path.join(PLAYER_IMAGES,'multi_player2.png'), multiplayer=2)

    ### Rendering Text on to the screen
    font1 = pygame.font.Font(ALBA_FONT, 40)
    line1 = font1.render("Don't Mess with the Fire", False, (255, 255, 255))
    line2 = font1.render('When Fire fires the fire', False, (255, 255, 255))
    line3 = font1.render('Fire will be fired,', False, (255, 255, 255))
    line4 = font1.render('I AM THE FIRE!!!!!!,', False, (255, 255, 255))
    line5 = font1.render("Nobody is Softer than me!", False, (255, 255, 255))
    line6 = font1.render('Nobody is Fiercer than me!', False, (255, 255, 255))
    line7 = font1.render('Nobody is Flexible than me!,', False, (255, 255, 255))
    line8 = font1.render('And Nobody can win against me!!,', False, (255, 255, 255))
    line9 = font1.render('Game is about to Start!!!!!,', False, (255, 255, 255))
    line10 = font1.render('Get Ready!!!!,', False, (255, 255, 255))

    # INITIALIZE BULLET LIST
    bull_arr_player1 = []
    bull_arr_player2 = []

    # Initializing variables that would be used
    threshold_health = -300

    ### Recurring loop to update the window for each frame interval
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return "end"

            ### Series of events with press of key board keys
            if(event.type == pygame.KEYDOWN):
                if(event.key == pygame.K_ESCAPE):
                    return "end"
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(xpos=multi_player2.xpos - 20, ypos=multi_player2.ypos + 25, imagepath=os.path.join(BULLET_IMAGES,'bullet1.png'))
                    bull_arr_player2.append(bullet)
                if event.key == pygame.K_e:
                    bullet = Bullet(xpos=multi_player1.xpos + 20, ypos=multi_player1.ypos + 25, imagepath=os.path.join(BULLET_IMAGES,'bullet2.png'))
                    bull_arr_player1.append(bullet)
                if event.key == pygame.K_z:
                    multi_player1.got_hurt()
                if event.key == pygame.K_m:
                    multi_player2.got_hurt()
                


        tick = pygame.time.get_ticks()
        

        ### Printing rendered text on to the screen
        CANVAS.blit(game_bg, (0, 0))
        if(tick<4000):
            CANVAS.blit(line9, ((400, HEIGHT / 10)))
            CANVAS.blit(line10, ((400, HEIGHT / 10 + 100)))
        if tick > 4000 and tick < 20000:
            multi_player2.display(screen=CANVAS)
            print_lines([line1, line2, line3, line4], CANVAS, multiplayer=1)
        elif tick > 20000 and tick < 36000:
            multi_player1.display(screen=CANVAS)
            print_lines([line5, line6, line7, line8], CANVAS, multiplayer=1)
        elif tick > 36000:
            multi_player1.display(screen=CANVAS)
            multi_player2.display(screen=CANVAS)

        pygame.draw.rect(CANVAS,(255,0,0),(10,10, 290 + multi_player1.health,25))
        pygame.draw.rect(CANVAS,(255,255,255),(10,10,300,25),4)


        ### Movement of Player 2 based on the Keys Pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            multi_player2.move(direction='l')
        elif keys[pygame.K_RIGHT]:
            multi_player2.move(direction='r')
        elif keys[pygame.K_UP]:
            multi_player2.move(direction='u')
        elif keys[pygame.K_DOWN]:
            multi_player2.move(direction='d')

        
        ### Movement of Player 1 based on the Keys Pressed
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            multi_player1.move(direction='l')
        elif keys[pygame.K_d]:
            multi_player1.move(direction='r')
        elif keys[pygame.K_w]:
            multi_player1.move(direction='u')
        elif keys[pygame.K_s]:
            multi_player1.move(direction='d')


        pygame.draw.rect(CANVAS,(255,0,0),(WIDTH - 310,10, 290 + multi_player2.health,25))
        pygame.draw.rect(CANVAS,(255,255,255),( WIDTH - 310,10, 300,25),4)
        

        ### Ending the Game if either of the Player's health is less than threshold
        if(multi_player1.health < threshold_health):
            return 2
        elif(multi_player2.health < threshold_health):
            return 1


        ### Updating the bullet arrays
        bull_arr_player1 = check_bullet_status(bull_arr_player1, CANVAS, direction="r")
        bull_arr_player2 = check_bullet_status(bull_arr_player2, CANVAS, direction="l")

        
        ### Updating the player's and bullet array information
        multi_player1, bull_arr_player2 = update_player_health(multi_player1, bull_arr_player2)
        multi_player2, bull_arr_player1 = update_player_health(multi_player2, bull_arr_player1)


        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second



def single_player_game(CANVAS, bg_image):

    # Initialize clock object
    clock = pygame.time.Clock()  

    # In Single player game there is Phase at each passage of time
    phase = 'instructions'
    ctdcount = 0

    # BACKGROUND MUSIC
    background_music("single_player.ogg")

    # INITIALIZE PLAYER
    player1 = Player(xpos=WIDTH / 2, ypos=HEIGHT / 2, imagepath=os.path.join(PLAYER_IMAGES,'player1.png'), multiplayer=0)

    # INITIALIZE BULLET LIST
    bull_arr = []
    bull_arr_enemy = []
    enemy_arr = []
    enemy_arr2 = []

    # GAPS
    vert_gap = HEIGHT / 100  # Vertical Gap
    hor_gap = WIDTH / 100  # Horizontal Gap


    # Greetings
    line1, line1_rect = render_text(int(WIDTH/8.0), 'GREETINGS', (WIDTH / 2), (HEIGHT / 2), (-15 * vert_gap))
    line2, line2_rect = render_text(int(WIDTH/8.0), ' MAVERICK', (WIDTH / 2), (HEIGHT / 2), (+15 * vert_gap))


    # This is your Captain
    line3, line3_rect = render_text(int(WIDTH/14.0), 'This is your Captain',      (WIDTH / 2), (HEIGHT / 2), (-10 * vert_gap))
    line4, line4_rect = render_text(int(WIDTH/14.0), ' The Earth is under attak', (WIDTH / 2), (HEIGHT / 2), (+10 * vert_gap))


    # Arrows
    line5, line5_rect = render_text(int(WIDTH/15.0), 'DEFEND EARTH',           (WIDTH / 2), (HEIGHT / 2), (-10 * vert_gap))
    line6, line6_rect = render_text(int(WIDTH/15.0), 'USE ARROW KEYS TO MOVE', (WIDTH / 2), (HEIGHT / 2), (+10 * vert_gap))


    # FIRE
    line7, line7_rect = render_text(int(WIDTH/15.0), 'USE SPACEBAR TO SHOOT ', (WIDTH / 2), (HEIGHT / 2), 0)


    # HEALTH BAR
    line8, line8_rect   = render_text(int(WIDTH/15.0), 'BE SAFE MAVERICK',             (WIDTH / 2), (HEIGHT / 2), (-20 * vert_gap))
    line9, line9_rect   = render_text(int(WIDTH/15.0), 'Dont Let your ego write ',     (WIDTH / 2), (HEIGHT / 2), 0)
    line10, line10_rect = render_text(int(WIDTH/15.0), 'checks your body can\'t cash', (WIDTH / 2), (HEIGHT / 2), (+20 * vert_gap))


    # tHREE_TWO_ONE
    three, three_rect = render_text(int(WIDTH /2.5), '3', (WIDTH / 2), (HEIGHT / 2), 0)
    two, two_rect     = render_text(int(WIDTH /2.5), '2', (WIDTH / 2), (HEIGHT / 2), 0)
    one, one_rect     = render_text(int(WIDTH /2.5), '1', (WIDTH / 2), (HEIGHT / 2), 0)


    start_time = pygame.time.get_ticks()

    # PHASE : Enemy1 VARIABLES
    x = 40 + (WIDTH / 10) * np.arange(10)
    x = list(x)


    flag = 1
    timer = 0

    # PHASE : Enemy2 VARIABLES
    enemy2flag = 0  
    flip = 100
    enemybulletFlag = 0

    singleRunning = True
    while singleRunning:

        # To Close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                singleRunning = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    bullet = Bullet(xpos=player1.xpos + 50, ypos=player1.ypos, imagepath=os.path.join(BULLET_IMAGES, 'bullet1.png'))
                    bull_arr.append(bullet)


        CANVAS.blit(bg_image, (0, 0))


        tick = pygame.time.get_ticks() -start_time

        ### Instructions phase from 1400 to 29000
        if tick>1400 and tick < 5500:
            print_lines([line1, line1_rect, line2, line2_rect], CANVAS)
        elif tick>6500 and tick <10000:
            print_lines([line3, line3_rect, line4, line4_rect], CANVAS)
        elif tick > 11550 and tick < 16150:
            print_lines([line5, line5_rect, line6, line6_rect], CANVAS)
        elif tick > 16150 and tick < 21300:
            print_lines([line7, line7_rect], CANVAS)
        elif tick > 21300 and tick < 29000:
            print_lines([line8, line8_rect, line9, line9_rect, line10, line10_rect], CANVAS)
        
        ### Count down begins from 29000 onwards
        elif tick > 29000 and tick < 31400:
            if ctdcount < 50:
                CANVAS.blit(three, three_rect)
                ctdcount += 1
            elif ctdcount < 100:
                CANVAS.blit(two, two_rect)
                ctdcount += 1
            else:
                CANVAS.blit(one, one_rect)
        
        ### Enemies start to appear after 31400 and boss enemey appears after 70545 time
        elif tick > 31400 and tick<70545:
            phase = 'enemy1'
        elif tick > 70545:
            phase = 'enemy2'


        ### Logic TO Render and handle Enemy1 objects 
        if phase == 'enemy1':

            if (flag == 1) or (timer > 620 and flag == 3):
                x = list(40 + (WIDTH / 10) * np.arange(10))
                for j in range(10):
                    enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1=os.path.join(ENEMY_IMAGES, 'alien1.png'),
                                   imagepath2=os.path.join(ENEMY_IMAGES, 'alien2.png'), imagepath3=os.path.join(ENEMY_IMAGES, 'alien3.png'))
                    enemy_arr.append(enemy)
                flag = 2 if (flag==1) else 4


            elif (timer > 310 and flag == 2) or (timer > 920 and flag == 4):

                x = list(130 + ((WIDTH - 180) / 9) * np.arange(9))
                for j in range(9):
                    enemy = Enemy1(xpos=x[j], ypos=-20, imagepath1=os.path.join(ENEMY_IMAGES, 'alien1.png'),
                                   imagepath2=os.path.join(ENEMY_IMAGES, 'alien2.png'), imagepath3=os.path.join(ENEMY_IMAGES, 'alien3.png'))
                    enemy_arr.append(enemy)
                flag = 3 if (flag==2) else 5

            timer += 1

        ### TO Render and handle Enemy2 objects 
        elif phase == 'enemy2':

            if enemy2flag == 0:
                enemy = Enemy2(xpos=((WIDTH - 600) / 2), ypos=+100,
                               imagepath1=ENEMY_IMAGES + '/boss1.png', imagepath2=ENEMY_IMAGES + '/boss2.png',
                               imagepath3=ENEMY_IMAGES + '/boss3.png', imagepath4=ENEMY_IMAGES + '/boss4.png')
                enemy_arr2.append(enemy)
                enemy2flag = 1


        player1.display(screen=CANVAS)


        ### Movement of Player 1 on the Screen
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player1.move(direction='l')
        elif keys[pygame.K_RIGHT]:
            player1.move(direction='r')
        elif keys[pygame.K_UP]:
            player1.move(direction='u')
        elif keys[pygame.K_DOWN]:
            player1.move(direction='d')



        bull_arr       = check_bullet_status(bull_arr, CANVAS, direction="u")
        bull_arr_enemy = check_bullet_status(bull_arr_enemy, CANVAS, direction="d")


        for enemy in enemy_arr:
            enemy.move()
            enemy.display(screen=CANVAS)
            if(enemy.isalive == False):
                return "Enemies"


        ### ENemy 2 logic to upgrade the power provess as his health is deteroiting with Player's bullets
        for enemy in enemy_arr2:

            if enemy.life > 300:
                enemy.move(direction='d')

            elif enemy.life > 290:

                if flip < 0:
                    enemy.move(direction='r')
                    flip += 1
                elif flip > 0:
                    enemy.move(direction='l')
                    flip -= 1
                elif flip == 0:
                    if np.random.binomial(1, .5) >= .5:
                        flip = 100
                    else:
                        flip = -100

            elif enemy.life > 100:

                if enemybulletFlag == 0:
                    bullet = Bullet(xpos=enemy.centerx, ypos=enemy.centery, imagepath=os.path.join(BULLET_IMAGES, 'bullet2.png'))
                    bull_arr_enemy.append(bullet)
                    enemybulletFlag = 1
                    old_tick = pygame.time.get_ticks()
                elif pygame.time.get_ticks() - old_tick > 1000:
                    enemybulletFlag = 0

                if flip < 0:
                    enemy.move(direction='r')
                    flip += 1
                elif flip > 0:
                    enemy.move(direction='l')
                    flip -= 1
                elif flip == 0:
                    if np.random.binomial(1, .5) >= .5:
                        flip = 100
                    else:
                        flip = -100

            enemy.display(screen=CANVAS)
            if(enemy.isalive == False):
                return "Boss"


        ### Updating the bullets array list and the enemy's health condition
        for b in bull_arr:
            for e in enemy_arr:
                if len(bull_arr) > 0 and len(enemy_arr) > 0:
                    if abs(b.xpos - e.xpos) < 60:
                        if b.ypos - 50 < e.ypos:
                            e.life -= 1
                            if b in bull_arr:
                                bull_arr.remove(b)
                            if (e.life == 0):
                                enemy_arr.remove(e)
            for e2 in enemy_arr2:
                if len(bull_arr) > 0 and len(enemy_arr2) > 0:

                    hcon1 = b.centerx + b.surface.get_width() / 2 > e2.centerx - e2.presentsurface.get_width() / 2 + 30
                    hcon2 = b.centerx - b.surface.get_width() / 2 < e2.centerx + e2.presentsurface.get_width() / 2 - 30

                    vcon1 = abs(b.centery - b.surface.get_height() / 2 - (e2.centery + e2.presentsurface.get_height() / 2)) < 5

                    if hcon1 and hcon2 and vcon1:
                        e2.life -= 10
                        if b in bull_arr:
                            bull_arr.remove(b)
                        if (e2.life == 0):
                            enemy_arr2.remove(e2)

                        if(len(enemy_arr2)==0):
                            return "player"

            # Collision of Enemy Bullets with Player Bullets
            for enemyBulllet in bull_arr_enemy:

                for playerBullet in bull_arr:
                    r_diff = np.sqrt((enemyBulllet.centerx - playerBullet.centerx)**2 + (enemyBulllet.centery - playerBullet.centery)**2)
                    if r_diff <50:
                        if enemyBulllet in bull_arr_enemy:
                            bull_arr_enemy.remove(enemyBulllet)
                        if playerBullet in bull_arr:
                            bull_arr.remove(playerBullet)


        ### Updating the enemy's bullet array list
        for enemyBulllet in bull_arr_enemy:

            hcon1 = enemyBulllet.centerx + enemyBulllet.surface.get_width() / 2 > player1.centerx - player1.surface.get_width() / 2 + 30
            hcon2 = enemyBulllet.centerx - enemyBulllet.surface.get_width() / 2 < player1.centerx + player1.surface.get_width() / 2 - 30
            vcon1 = abs(enemyBulllet.centery + enemyBulllet.surface.get_height() / 2 - (
                        player1.centery - player1.surface.get_height() / 2)) < 5

            if hcon1 and hcon2 and vcon1:
                player1.life -= 10
                if enemyBulllet in bull_arr_enemy:
                    bull_arr_enemy.remove(enemyBulllet)

        ### Ending the Game if the Player's health is less than threshold
        if(player1.life < 0):
            return "Boss"
        


        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second




def start_game(CANVAS, start_bg):

    clock = pygame.time.Clock()

    # TITLE OF THE GAME
    font = pygame.font.Font(SPACE_FONT, 100)
    line1 = font.render('    SPACE  ', True, (255, 232, 31))
    line2 = font.render('ADVENTURE', False, (255, 232, 31))

    # BACKGROUND MUSIC
    background_music("intro.mp3")

    # SINGLE PLAYER BUTTON
    astro1 = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro1.png')).convert_alpha()
    astro1enl = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro1enlarged.png')).convert_alpha()
    astro1_rect = astro1.get_rect(topleft=(WIDTH / 4, HEIGHT / 3.2))

    astro2 = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro2.png')).convert_alpha()
    astro2enl = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro2enlarged.png')).convert_alpha()
    astro2_rect = astro2.get_rect(topleft=((WIDTH / 4) - 40, HEIGHT / 2))

    # MULTIPLAYER BUTTON
    font1 = pygame.font.Font(ALBA_FONT, int(120*HEIGHT/1020))
    line3 = font1.render('  SINGLE PLAYER', False, (255, 255, 255))
    line4 = font1.render('  MULTI PLAYER', False, (255, 255, 255))

    while(True):

        # To Close the window
        check_window()

        CANVAS.blit(start_bg, (0, 0))
        CANVAS.blit(line1, (100, 50))
        CANVAS.blit(line2, (300, 100))

        mouse_coordinates = pygame.mouse.get_pos()
        if astro2_rect.collidepoint(mouse_coordinates):
            CANVAS.blit(astro2enl, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                state = 'multi_player'
                return state

        elif astro1_rect.collidepoint(mouse_coordinates):

            CANVAS.blit(astro1enl, astro1_rect)
            CANVAS.blit(astro2, astro2_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                state = 'single_player'
                return state

        else:
            CANVAS.blit(astro2, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

        CANVAS.blit(line3, (WIDTH / 4 + 100, HEIGHT / 3.2))
        CANVAS.blit(line4, (WIDTH / 4 + 150, HEIGHT / 2))

        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second



def end_game(CANVAS, start_bg, won=None, name=None):

    clock = pygame.time.Clock()

    # # TITLE OF THE PAGE
    font = pygame.font.Font(SPACE_FONT, 100)
    line1 = font.render('    GAME  ', False, (255, 232, 31))
    line2 = font.render('OVER', False, (255, 232, 31))

    ### Won Parameter is used in Single player and multi player game to get message of who won the game
    if(won!=None):
        if(name==None):
            line3 = font.render(won + " Won!!!", False, (255, 232, 31))
        else:
            line3 = font.render(won + ": " + name + " Won!!!", False, (255, 232, 31))

    
    # BACKGROUND MUSIC
    background_music("endgame.mp3")


    # Buttons to use for Replaying the Game
    astro1 = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro1.png')).convert_alpha()
    astro1enl = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro1enlarged.png')).convert_alpha()
    astro1_rect = astro1.get_rect(topleft=(WIDTH / 4, HEIGHT / 3.2))

    # Buttons to use for Exiting the Game
    astro2 = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro2.png')).convert_alpha()
    astro2enl = pygame.image.load(os.path.join(ASTRONOMER_IMAGES,'astro2enlarged.png')).convert_alpha()
    astro2_rect = astro2.get_rect(topleft=((WIDTH / 4) - 40, HEIGHT / 2))

    # Rendering the Font of the text for Play again and Exiting the Game
    font1 = pygame.font.Font(ALBA_FONT, int(120*HEIGHT/1020))
    line4 = font1.render('  Play Again', False, (255, 255, 255))
    line5 = font1.render('  Exit Game', False, (255, 255, 255))


    ### Recurring loop to render text, objects and data into the Display window 
    while True:
        check_window()

        CANVAS.blit(start_bg, (0, 0))
        CANVAS.blit(line1, (WIDTH / 16, HEIGHT / 8))
        CANVAS.blit(line2, (WIDTH * 5 / 8, HEIGHT / 8))
        
        if(won):
            CANVAS.blit(line3, (300, HEIGHT - 200))
        
        mouse_coordinates = pygame.mouse.get_pos()
        if astro2_rect.collidepoint(mouse_coordinates):
            CANVAS.blit(astro2enl, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                return "close"

        elif astro1_rect.collidepoint(mouse_coordinates):

            CANVAS.blit(astro1enl, astro1_rect)
            CANVAS.blit(astro2, astro2_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                time.sleep(3)
                return "start"

        else:
            CANVAS.blit(astro2, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

        CANVAS.blit(line4, (WIDTH / 4 + 100, HEIGHT / 3.4))
        CANVAS.blit(line5, (WIDTH / 4 + 100, HEIGHT / 2))


        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second



"""
* Main Function which initializes the Pygame. 
* Some of the key arguments created here are as follows
* * GAME_STATE := State of the Game at particular instance
* * CANVAS     := Display details of the window that would be created of the pygame
* Different phases of the GAME_STATE are as follows:-
* * start         - Start of the Game
* * end           - Ending the Game
* * single_player - Starting the state of Single Player Game
* * multi_player  - Starting the state of Multi Player Game
"""
def main():

    # Declaring the initial state of the pygame
    GAME_STATE = "start"
    
    # Initializing the Pygame and the Display Window
    pygame.init()
    CANVAS = pygame.display.set_mode((WIDTH, HEIGHT), HWSURFACE | DOUBLEBUF | RESIZABLE)

    # Declaring the Name of the game
    pygame.display.set_caption("ADVENTURE TIME") 

    # Initializing the Background images for different stages of the Pygame
    start_bg = pygame.image.load(os.path.join(BACKGROUND_IMAGES, "start.jpg")).convert()
    game_bg  = pygame.image.load(os.path.join(BACKGROUND_IMAGES, "stars.jpg")).convert()
    end_bg  = pygame.image.load(os.path.join(BACKGROUND_IMAGES, "stars.jpg")).convert()



    # A Continous loop in which game states are altered based on choices and different game modes are displayed and played
    while(True):
        if(GAME_STATE == "start"):
            GAME_STATE = start_game(CANVAS, start_bg)
        elif(GAME_STATE == "end"):
            GAME_STATE = end_game(CANVAS, end_bg)
        elif(GAME_STATE == "single_player"):
            GAME_STATE = single_player_game(CANVAS, game_bg)
            GAME_STATE = end_game(CANVAS, end_bg, won=GAME_STATE)
        elif(GAME_STATE == "multi_player"):
            player = multi_player_game(CANVAS, game_bg)
            update_stats(player)
            GAME_STATE = end_game(CANVAS, end_bg, won=str(player), name=PLAYER_NAMES[player-1])
                        
        else:
            break

    print("Thank you for playing the Game. It is over")



if __name__ == "__main__":
    """
    Main Function is executed here
    The Entire code logic is being run from here.
    We call the Main function which initializes the Pygame
    """
    main()
