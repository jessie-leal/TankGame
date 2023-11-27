import pygame as pg
from CONSTANTS import *
from global_vars import *
from entities import *
from mapClass import Map
from event_handler import EventHandler

def runGame(handler):
    if handler.gameActive:
        # event handling
        handler.player_control_process()
        handler.update_bullets()
        handler.check_hit()
        
        # Map handling
        map.redraw()

        mainDisplay.blit(test_image, test_rect)
        handler.update_game_screen()
        
if __name__ == "__main__":
    #Initiate pygane
    pg.init()
    pg.display.set_caption("Tank Game")
    pg.display.set_icon(pg.image.load("resources/sprites/tank_icon.png"))
    handler = EventHandler()
    map = Map(mainDisplay)

    #Sprites
    SPRITE = {"PLAYER1": Texture("resources/sprites/tankG.png", isAnimated = True, frames = 3, frameTime = 20),
            "PLAYER2": Texture("resources/sprites/tankR.png", isAnimated = True, frames = 3, frameTime = 20)}

    player1 = Player(1, texture = SPRITE["PLAYER1"], coord = (SCREEN_WIDTH/3, SCREEN_HEIGHT/2), controls=CONTROL_PRESET["WASD"])
    player2 = Player(2, texture = SPRITE["PLAYER2"], coord = (SCREEN_WIDTH/3*2, SCREEN_HEIGHT/2), angleDeg=180, controls=CONTROL_PRESET["ARROWS"])
    list_players.append(player1)
    list_players.append(player2)

    print("Press SPACE to start the game")
    while handler.programActive:
        # ticks per seconds
        clock.tick(SCREEN_FPS)
        # stuff to update every tick
        handler.keys = pg.key.get_pressed()
        handler.events = pg.event.get()
        handler.listen()

        if handler.gameActive:
            runGame(handler)
        else:
            mainDisplay.fill('black')

        
        pg.display.update()