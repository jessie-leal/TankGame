import pygame as pg
from CONSTANTS import *

'''
Some global variables that are used in multiple files.
'''

mainDisplay = pg.display.set_mode(SCREEN_RES)
clock = pg.time.Clock()

#Game elemtents
list_players = []
list_bullets = []
collision_list = [] # List of rects that are collidable