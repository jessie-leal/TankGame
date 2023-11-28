import pygame as pg
from CONSTANTS import *
from global_vars import *
from entities import *
from Map import Map
from event_handler import EventHandler

#shot sounds credit to hosch (https://hosch.itch.io)
#https://opengameart.org/content/8-bit-sound-effects-2

#explosion sound: https://opengameart.org/content/big-explosion

#Background music credit to bart @  http://opengameart.org

if __name__ == "__main__":
    #Initiate pygame
    pg.init()
    pg.font.init()
    pg.mixer.init()
    pg.display.set_caption("Tank Game")
    pg.display.set_icon(pg.image.load("resources/sprites/tank_icon.png"))
    handler = EventHandler()
    map = Map(mainDisplay)

    menu = handler.create_menu(map)

    #Sprites
    SPRITE = {"PLAYER1": Texture("resources/sprites/tankG.png", isAnimated = True, frames = 3, frameTime = 20),
                "PLAYER2": Texture("resources/sprites/tankR.png", isAnimated = True, frames = 3, frameTime = 20)}

    player1 = Player(1, texture = SPRITE["PLAYER1"], coord = (SCREEN_WIDTH/3, SCREEN_HEIGHT/2), controls=CONTROL_PRESET["WASD"])
    player2 = Player(2, texture = SPRITE["PLAYER2"], coord = (SCREEN_WIDTH/3*2, SCREEN_HEIGHT/2), angleDeg=180, controls=CONTROL_PRESET["ARROWS"])
    list_players.append(player1)
    list_players.append(player2)

    handler.control_splash_screen()

    mainDisplay.fill('black')
    menu.draw(mainDisplay)
    menu.mainloop(mainDisplay)
    while handler.programActive:
        # ticks per seconds
        clock.tick(SCREEN_FPS)
        # stuff to update every tick
        handler.keys = pg.key.get_pressed()
        handler.events = pg.event.get()
        handler.listen()

        if handler.gameActive:
            handler.runGame(map)
        elif not menu.is_enabled():
            menu.enable()
            menu.mainloop(mainDisplay)

        pg.display.update()