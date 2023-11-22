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
    handler.update_bullets()
    handler.check_hit()
    
    # Map handling
    # map.draw()
    # map.drawMaze()
    map.redraw()

    mainDisplay.blit(test_image, test_rect)
    handler.update_screen()
    pg.display.update()