import pygame
from pygame import mixer

#pygame.init()

#WIDTH = 1920
#HEIGHT = 1080
#FPS = 60
#CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
#pygame.display.set_caption("ADVENTURE TIME")  # Name of the game
#clock = pygame.time.Clock()  # Initialize clock object







def startgame():
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    FPS = 60
    CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ADVENTURE TIME")  # Name of the game
    clock = pygame.time.Clock()  # Initialize clock object

    # BACKGROUND IMAGE
    bg = pygame.image.load('images/backgrounds/start.jpg').convert()

    # TITLE OF THE GAME
    font = pygame.font.Font('fonts/space-age/space age.ttf', 150)
    line1 = font.render('    SPACE  ', False, (255, 232, 31))
    line2 = font.render('ADVENTURE', False, (255, 232, 31))

    # BACKGROUND MUSIC
    mixer.music.load("audio/background/rain.mp3")
    mixer.music.play(-1)

    # SINGLE PLAYER BUTTON
    astro1 = pygame.image.load('images/astro1.png').convert_alpha()
    astro1enl = pygame.image.load('images/astro1enlarged.png').convert_alpha()
    astro1_rect = astro1.get_rect(topleft=(WIDTH / 4, HEIGHT / 3.2))

    astro2 = pygame.image.load('images/astro2.png').convert_alpha()
    astro2enl = pygame.image.load('images/astro2enlarged.png').convert_alpha()
    astro2_rect = astro2.get_rect(topleft=(WIDTH / 4 - 40, HEIGHT / 2))

    # MULTIPLAYER BUTTON
    font2 = pygame.font.Font('fonts/alba/ALBAS___.TTF', 120)
    line3 = font2.render('  SINGLE PLAYER', False, (255, 255, 255))
    line4 = font2.render('  MULTI PLAYER', False, (255, 255, 255))

    startRunning = True
    while startRunning:

        # To Close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                startRunning = False

        CANVAS.blit(bg, (0, 0))
        CANVAS.blit(line1, (400, 50))
        CANVAS.blit(line2, (400, 150))

        mouse_coordinates = pygame.mouse.get_pos()
        if astro2_rect.collidepoint(mouse_coordinates):
            #print("collison ho gaya")
            CANVAS.blit(astro2enl, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                #startRunning = False
                state = 'multi'
                return state



        elif astro1_rect.collidepoint(mouse_coordinates):

            CANVAS.blit(astro1enl, astro1_rect)
            CANVAS.blit(astro2, astro2_rect)

            click = pygame.mouse.get_pressed()
            if click[0]:
                #startRunning = False
                state = 'single'
                return state

        else:
            CANVAS.blit(astro2, astro2_rect)
            CANVAS.blit(astro1, astro1_rect)

        CANVAS.blit(line3, (WIDTH / 4 + 100, HEIGHT / 3.2))
        CANVAS.blit(line4, (WIDTH / 4 + 150, HEIGHT / 2))

        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second


def gameover():
    pygame.init()

    WIDTH = 1920
    HEIGHT = 1080
    FPS = 60
    CANVAS = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("ADVENTURE TIME")  # Name of the game
    clock = pygame.time.Clock()  # Initialize clock object


    # BACKGROUND IMAGE
    bg = pygame.image.load('images/backgrounds/start.jpg').convert()

    # TITLE OF THE GAME
    font = pygame.font.Font('fonts/space-age/space age.ttf', 150)
    line1 = font.render('    GAME  ', False, (255, 232, 31))
    line2 = font.render('OVER', False, (255, 232, 31))

    # BACKGROUND MUSIC
    mixer.music.load("audio/background/rain.mp3")
    mixer.music.play(-1)

    # SINGLE PLAYER BUTTON
    astro1 = pygame.image.load('images/astro1.png').convert_alpha()
    astro1enl = pygame.image.load('images/astro1enlarged.png').convert_alpha()
    astro1_rect = astro1.get_rect(topleft=(WIDTH / 4, HEIGHT / 3.2))

    astro2 = pygame.image.load('images/astro2.png').convert_alpha()
    astro2enl = pygame.image.load('images/astro2enlarged.png').convert_alpha()
    astro2_rect = astro2.get_rect(topleft=(WIDTH / 4 - 40, HEIGHT / 2))

    # MULTIPLAYER BUTTON
    font2 = pygame.font.Font('fonts/alba/ALBAS___.TTF', 120)
    line3 = font2.render('  SINGLE PLAYER', False, (255, 255, 255))
    line4 = font2.render('  MULTI PLAYER', False, (255, 255, 255))

    gameoverRunning = True
    while gameoverRunning:

        # To Close the window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameoverRunning = False

        CANVAS.blit(bg, (0, 0))
        CANVAS.blit(line1, (400, 50))
        CANVAS.blit(line2, (400, 150))






        pygame.display.update()  # To refresh every time while loop runs
        clock.tick(60)  # To run update 60 frames in 1 second





#state = 'start'

state = 'start'
while True:

    if state=='start':
        state = startgame()
    if state == 'single':
        state = gameover()
    if state == 'multi':
        break

print(state)


#if state == 'single':
    #state = gameover()
    #print("hello there")
