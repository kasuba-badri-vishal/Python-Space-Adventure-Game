import os
import pygame
import pandas as pd
import matplotlib.pyplot as plt
from config import *
from pygame import mixer


"""
Function to exit the Pygame
"""
def exit_game():
    pygame.quit()
    exit()


"""
Checking the Window buttons in each iteration to see if the window would be closed or not
"""
def check_window():
	for event in pygame.event.get():
		if event.type == pygame.QUIT or event.type == pygame.K_ESCAPE:
			exit_game()     
		elif(event.type == pygame.KEYDOWN):
			if(event.key == pygame.K_ESCAPE):
				exit_game()


"""
Running the Background music given the file name of the audio file
The Music is different for different stages of Game
"""
def background_music(audio_file):
	mixer.music.load(os.path.join(AUDIO, audio_file))
	mixer.music.play(-1)


"""
If a bullet reaches near to a player upto some threshold X_POS and Y_POS value, the player gets hit by bullet
The player's health information is updated accordingly and the objects is returned back
"""
def update_player_health(player, bull_arr):
	if(len(bull_arr)):
		for b in bull_arr:
			if(abs(b.xpos - player.xpos) < X_POS) and (abs(b.ypos - player.ypos) < Y_POS):
				player.got_hurt()
				bull_arr.remove(b)
	return player, bull_arr

"""

"""
def check_bullet_status(bull_arr, CANVAS, direction=None):
	for bullet in bull_arr:
		bullet.move(direction=direction)

		if bullet.isactive == False:
			bull_arr.remove(bullet)
		else:
			bullet.display(screen=CANVAS)

	return bull_arr

"""

"""
def print_lines(lines_list, CANVAS, multiplayer=0):
	if(multiplayer):
		value = 0
		for line in lines_list:
			CANVAS.blit(line, ((WIDTH/4, (HEIGHT / 10) + value)))
			value += DISTANCE
	else:
		value = 0
		while(value<len(lines_list)):
			CANVAS.blit(lines_list[value], lines_list[value+1])
			value += 2


def render_text(font_size, message, width, height, gap):
	font = pygame.font.Font(ALBA_FONT, font_size)
	line = font.render(message, False, (255, 255, 255))
	line_rect = line.get_rect(center=(width, height + gap))
	return line, line_rect


"""
Updating the statistics of the multiplayer game if any of the player wins
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
Getting the Statistics of the multiplayer game and saving the images of Bar Plot and Pie Plot
"""
def get_stats():

	### Reading the data and loading the stats into variables for analysis
	df = pd.read_csv(os.path.join(STATS,'stats.csv'))
	stats = df['Player'].value_counts()
	values = [stats['Player 1'], stats['Player 2']]
	labels = ['Player 1', 'Player 2']
	colors = ["blue", "red"]
	explode = [0.1, 0]
	total = values[0] + values[1]


	### Making a Pie plot with the available Stats
	plt.pie(values, labels = labels, explode = explode, colors=colors, 
			autopct=lambda p: '{:.0f}%'.format(p), shadow = True)
	plt.legend(title = "Game WINS", loc='best')
	plt.savefig(os.path.join('./src/web/static/resources/pie.png'), bbox_inches='tight')


	### Making a Bar plot with the available Stats
	fig = plt.figure(figsize = (6, 4))
	plt.bar(labels[0], values[0], label='Player 1', color='blue', edgecolor='black')
	plt.bar(labels[1], values[1], label='Player 2', color='red', edgecolor='black', hatch='//')
	plt.xlabel("Player Details")	
	plt.ylabel("No. of Matches")
	plt.title("Bar Graph of Game Wins (" + str(total) + " Games)")
	plt.legend(loc='best')
	plt.savefig(os.path.join('./src/web/static/resources/bar.png'))