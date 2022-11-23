import os

# Host and Port on which Web Application would be run
HOST = "0.0.0.0"
PORT = 5000


# Declaration of Size of the Window and No. of frames per second
WIDTH = 1920
HEIGHT = 1080
FPS = 60


# Current state of the Game when game is initialized
GAME_STATE = "start"


# Variable that contains the details of who won the Game
WON = None


# Names of the Multi-Players that are being played
PLAYER_NAMES = ['Aditya', 'Badri']


# Path to the data that is used by the game
IMAGES = "./data/images/"
AUDIO  = "./data/audio/"
FONTS  = "./data/fonts/"
STATS  = "./data/stats/"

BACKGROUND_IMAGES = os.path.join(IMAGES,"backgrounds")
ASTRONOMER_IMAGES = os.path.join(IMAGES,"astronomers")
PLAYER_IMAGES = os.path.join(IMAGES,"players")
BULLET_IMAGES = os.path.join(IMAGES,"bullets")
ENEMY_IMAGES = os.path.join(IMAGES,"enemy")


#Font type for the Details that are shown on the Pygame
ALBA_FONT  = os.path.join(FONTS, 'alba/ALBAS___.TTF')
SPACE_FONT = os.path.join(FONTS, 'space-age/space age.ttf')



#Threshold Bullet hit distance for the Players
X_POS = 50
Y_POS = 50


# Threshold of Distance between two lines that are displayed
DISTANCE = 100