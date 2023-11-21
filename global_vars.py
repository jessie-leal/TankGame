import pygame as pg
from CONSTANTS import *

mainDisplay = pg.display.set_mode(SCREEN_RES)
clock = pg.time.Clock()

#Game elemtents
list_players = []
list_bullets = []

gameActive = True