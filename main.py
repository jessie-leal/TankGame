import pygame as pg
from CONSTANTS import *
from global_vars import *
from entities import *
from Map import Map
from event_handler import EventHandler
import pygame_menu

#shot sounds credit to hosch (https://hosch.itch.io)
#https://opengameart.org/content/8-bit-sound-effects-2

#explosion sound: https://opengameart.org/content/big-explosion

#Background music credit to bart @  http://opengameart.org
        
# define a function to set the map when selector in menu is used.
# first declare a variable to hold a choice

choice = 1

def start_the_game(choice, handler):
    # Create the selected map
    currentMap.createMaze(currentMap.maze)
    handler.currentMap = currentMap
    # Add map's rects to collision list
    collision_list.clear()
    collision_list.extend([x.rect for x in currentMap.map if x.rect not in collision_list])
    # Reset players
    handler.resetPlayers()
    # Start the game
    handler.gameActive = True
    # Disable the menu so the mainloop stops
    menu.disable()
    #start background music
    music = pg.mixer.music.load("Resources/sound/bggame.ogg")
    pg.mixer.music.set_volume(.5)
    pg.mixer.music.play(-1)


def create_menu() -> pygame_menu.Menu:
    def set_map(map, value):
        global choice
        if value == 1:
            choice = 1
        elif value == 2:
            choice = 2
        else:
            choice = 3
        currentMap.maze = choice
        
    menu = pygame_menu.Menu('Tank Game', 500, 300, theme=pygame_menu.themes.THEME_BLUE)
    # mapMenu = pygame_menu.Menu('Select a Map', 500, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Choose Your Map :', [('Map 1', 1), ('Map 2', 2), ('Map 3', 3)], onchange=set_map)
    menu.add.button('Play', lambda: start_the_game(choice, handler))
    menu.add.button('Quit', pygame_menu.events.EXIT)
    menu.add.surface

    return menu

if __name__ == "__main__":
    #Initiate pygame
    pg.init()
    pg.font.init()
    pg.mixer.init()
    pg.display.set_caption("Tank Game")
    pg.display.set_icon(pg.image.load("resources/sprites/tank_icon.png"))
    handler = EventHandler()
    currentMap = Map(mainDisplay)
    

    menu = create_menu()

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
            handler.runGame(currentMap)
        elif not menu.is_enabled():
            menu.enable()
            menu.mainloop(mainDisplay)

        pg.display.update()