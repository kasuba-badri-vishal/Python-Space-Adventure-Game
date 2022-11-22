import pygame
import pandas as pd
import os
from config import STATS

def exit_game():
    pygame.quit()
    exit()

def update_stats(player):
    df = pd.read_csv(os.path.join(STATS,'stats.csv'))
    df.loc[len(df.index)] = [len(df.index), player]
    df.to_csv(os.path.join(STATS,'stats.csv'), index=False)
    
