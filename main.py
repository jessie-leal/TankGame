from pyGameUtils import *
import pygame
import pygame_menu
from Map import Map


#initialize pygame
pygame.init()

#initialize a display
mainDisplay = pygame.display.set_mode((1280, 720))

#set background image
bgImage = pygame.image.load("Resources/fields.png")
bgImage = pygame.transform.scale(bgImage, (1280, 720))
mainDisplay.blit(bgImage, ((0, 0)))

#fill the display background
mainDisplay.fill((200, 0, 100))

#create a map
map = Map(mainDisplay)

#define a function to set the map when selector in menu is used.
#first declare a variable to hold a choice
choice = 0
def set_map(map, value):
    global choice
    if value == 1:
        choice = 1
    elif value == 2:
        choice = 2
    else:
        choice = 3

def start_the_game(choice):

    # draw the map
    map.draw()

    # draw the maze
    map.drawMaze(choice)


#call event handler
handler = EventHandler(mainDisplay, map)

#create a game clock
gameClock = pygame.time.Clock()

menu = pygame_menu.Menu('Welcome', 500, 300, theme=pygame_menu.themes.THEME_BLUE)
    #mapMenu = pygame_menu.Menu('Select a Map', 500, 300, theme=pygame_menu.themes.THEME_BLUE)

menu.add.selector('Choose Your Map :', [('Map 1', 1), ('Map 2', 2), ('Map 3', 3)], onchange=set_map)
menu.add.button('Play', start_the_game(choice))
menu.add.button('Quit', pygame_menu.events.EXIT)


# Write loop that will run forever until we exit
while True:
    menu.draw(mainDisplay)
    menu.mainloop(mainDisplay)

    #Use the handler to listen for events
    handler.listen(pygame.event.get())


    # Do some stuff
    pygame.display.update()

    # Wait for next frame using Clock
    gameClock.tick(5)