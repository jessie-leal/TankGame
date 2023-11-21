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

#call event handler
handler = EventHandler(mainDisplay, map)

#create a game clock
gameClock = pygame.time.Clock()

# Write loop that will run forever until we exit
while True:
    #Use the handler to listen for events
    handler.listen(pygame.event.get())
    #mainDisplay.fill((200, 200, 150)) #This just gets rid of the other event for clicking

    # draw the map
    map.draw()
    #draw the maze
    map.drawMaze()


    # Do some stuff
    pygame.display.update()

    # Wait for next frame using Clock
    gameClock.tick(5)