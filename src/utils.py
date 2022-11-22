import os
import pygame
import pandas as pd
import matplotlib.pyplot as plt
from config import STATS, AUDIO
from pygame import mixer

"""
Function to exit the Pygame
"""
def exit_game():
    pygame.quit()
    exit()


### Checking the Window buttons in each iteration to see if the window would be closed or not
def check_window():
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
			exit_game()     
		elif(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_ESCAPE):
				exit_game()



def background_music(audio_file):
	mixer.music.load(os.path.join(AUDIO, audio_file))
	mixer.music.play(-1)

"""
Updating the statistics of the multiplayer game if any player wins
"""
def update_stats(player):
	value = None
	df = pd.read_csv(os.path.join(STATS,'stats.csv'))
	
	if(player == 1):
		value = "Player 1"
	elif(player == 2):
		value = "Player 2"

	if(value !=None):
		df.loc[len(df.index)+1] = [len(df.index), value]
		df.to_csv(os.path.join(STATS,'stats.csv'), index=False)
    

"""
Getting the Statistics of the multiplayer game and saving the image
"""
def get_stats():
	df = pd.read_csv(os.path.join(STATS,'stats.csv'))
	stats = df['Player'].value_counts()
	y = [stats['Player 1'], stats['Player 2']]
	mylabels = ['Player 1', 'Player 2']
	mycolors = ["blue", "red"]
	myexplode = [0.1, 0]

	plt.pie(y, labels = mylabels, explode = myexplode, colors=mycolors, 
			autopct=lambda p: '{:.0f}%'.format(p), shadow = True)
	plt.legend(title = "Game WINS", loc='best')
	plt.savefig(os.path.join('./src/web/static/resources/pie.png'), bbox_inches='tight')
