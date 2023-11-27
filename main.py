import pygame as pg
from CONSTANTS import *
from global_vars import *
from entities import *
from mapClass import Map
from event_handler import EventHandler
import pygame_menu

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

# define a function to set the map when selector in menu is used.
# first declare a variable to hold a choice

choice = 1

def set_map(map, value):
    global choice
    if value == 1:
        choice = 1
    elif value == 2:
        choice = 2
    else:
        choice = 3

def start_the_game(choice, handler):
    handler.gameActive = True

def create_menu() -> pygame_menu.Menu:
    menu = pygame_menu.Menu('Welcome', 500, 300, theme=pygame_menu.themes.THEME_BLUE)
    # mapMenu = pygame_menu.Menu('Select a Map', 500, 300, theme=pygame_menu.themes.THEME_BLUE)
    menu.add.selector('Choose Your Map :', [('Map 1', 1), ('Map 2', 2), ('Map 3', 3)], onchange=set_map)
    menu.add.button('Play', start_the_game(choice, handler))
    menu.add.button('Quit', pygame_menu.events.EXIT)

    return menu

# if __name__ == "__main__":
#Initiate pygame
pg.init()
pg.display.set_caption("Tank Game")
pg.display.set_icon(pg.image.load("resources/sprites/tank_icon.png"))
handler = EventHandler()
map = Map(mainDisplay)

menu = create_menu()

#Sprites
SPRITE = {"PLAYER1": Texture("resources/sprites/tankG.png", isAnimated = True, frames = 3, frameTime = 20),
            "PLAYER2": Texture("resources/sprites/tankR.png", isAnimated = True, frames = 3, frameTime = 20)}

player1 = Player(1, texture = SPRITE["PLAYER1"], coord = (SCREEN_WIDTH/3, SCREEN_HEIGHT/2), controls=CONTROL_PRESET["WASD"])
player2 = Player(2, texture = SPRITE["PLAYER2"], coord = (SCREEN_WIDTH/3*2, SCREEN_HEIGHT/2), angleDeg=180, controls=CONTROL_PRESET["ARROWS"])
list_players.append(player1)
list_players.append(player2)

mainDisplay.fill('black')
menu.draw(mainDisplay)
# menu.mainloop(mainDisplay)
while handler.programActive:
    # ticks per seconds
    clock.tick(SCREEN_FPS)
    # stuff to update every tick
    handler.keys = pg.key.get_pressed()
    handler.events = pg.event.get()
    handler.listen()
    if handler.gameActive:
        runGame(handler)
        collision_list.extend([x.rect for x in map.map if x.rect not in collision_list])

    pg.display.update()