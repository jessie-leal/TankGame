import pygame as pg
from CONSTANTS import *
from global_vars import *
from entities import *
from mapClass import Map
from event_handler import EventHandler

#Pygame initialization
pg.init()
handler = EventHandler()
map = Map(mainDisplay)

#Sprites
SPRITE = {"PLAYER1": Texture("resources/sprites/tankG.png", isAnimated = True, frames = 3, frameTime = 20),
          "PLAYER2": Texture("resources/sprites/tankR.png", isAnimated = True, frames = 3, frameTime = 20)}

test_image = pg.surface.Surface((50, 50))
test_image.fill('green4')
test_rect = test_image.get_rect()
test_rect.center = ((SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
print(test_rect.left, test_rect.right, test_rect.top, test_rect.center)

list_players.append(Player(1, texture = SPRITE["PLAYER1"], coord = (SCREEN_WIDTH/3, SCREEN_HEIGHT/2), controls=CONTROL_PRESET["WASD"]))
list_players.append(Player(2, texture = SPRITE["PLAYER2"], coord = (SCREEN_WIDTH/3*2, SCREEN_HEIGHT/2), angleDeg=180, controls=CONTROL_PRESET["ARROWS"]))

while gameActive:
    # ticks per seconds
    clock.tick(SCREEN_FPS)
    # stuff to update every tick
    # mainDisplay.fill(pg.color.Color('white'))
    handler.keys = pg.key.get_pressed()
    handler.events = pg.event.get()

    # event handling
    handler.listen()
    handler.player_control_process()
    handler.update_bullets(test_rect)
    handler.check_collisions()
    
    # Map handling
    # map.draw()
    # map.drawMaze()
    map.redraw()

    handler.update_screen()
    mainDisplay.blit(test_image, test_rect)
    pg.display.update()