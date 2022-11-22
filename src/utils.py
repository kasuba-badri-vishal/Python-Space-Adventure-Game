import pygame
import pandas as pd
import os
from config import STATS
import matplotlib.pyplot as plt

def exit_game():
    pygame.quit()
    exit()

def update_stats(player):
    value = "Player 2"
    df = pd.read_csv(os.path.join(STATS,'stats.csv'))
    if(player == 1):
        value = "Player 1"
    df.loc[len(df.index)+1] = [len(df.index), value]
    df.to_csv(os.path.join(STATS,'stats.csv'), index=False)
    

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
	plt.savefig(os.path.join(STATS+'pie.png'), bbox_inches='tight')
