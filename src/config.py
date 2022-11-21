import os

HOST = "0.0.0.0"
PORT = 5000


# Declaration of Size of the Window and No. of frames per second
WIDTH = 1200 #1920
HEIGHT = 600 #1080
FPS = 60


IMAGES = "./../data/images/"
AUDIO  = "./../data/audio/"
FONTS  = "./../data/fonts/"

BACKGROUND_IMAGES = os.path.join(IMAGES,"backgrounds")
ASTRONOMER_IMAGES = os.path.join(IMAGES,"astronomers")
PLAYER_IMAGES = os.path.join(IMAGES,"players")
BULLET_IMAGES = os.path.join(IMAGES,"bullets")
ENEMY_IMAGES = os.path.join(IMAGES,"enemy")