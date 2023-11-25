import pygame as pg
from CONSTANTS import *

mainDisplay = pg.display.set_mode(SCREEN_RES)
clock = pg.time.Clock()

#TEMP
test_image = pg.surface.Surface((50, 50))
test_image.fill('green4')
test_rect = test_image.get_rect()
test_rect.center = ((SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50))
# print(test_rect.left, test_rect.right, test_rect.top, test_rect.center)

#Game elemtents
list_players = []
list_bullets = []
collision_list = [test_rect] # List of rects that are collidable