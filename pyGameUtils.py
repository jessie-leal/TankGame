#Event handler

import pygame
from Map import Map

class EventHandler:
    #queueOfEvents starts as empty list
    def __init__(self, display, map):
        self.display = display
        self.queueOfEvents = []
        self.images = []
        self.map = map
        #self.wall = Wall(10,400)

    def loadImage(self, img):
        self.images.append(img)

    def listen(self, events):
        #input parameter should be list of events (comes from pygame.event.get())
        #store out events in queueOfEvents
        self.queueOfEvents = events

        #print the events we hear
        for event in self.queueOfEvents:
            print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            #not needed
            #elif self.menu.is_enabled():
             #   self.menu.update(events)
              #  self.menu.draw(self.display)

            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.display.fill((100, 90, 100))

            elif event.type == pygame.MOUSEBUTTONUP:
                self.display.fill((200, 0, 100))

            elif ( event.type == pygame.VIDEORESIZE ):
            #If the window size changes, redraw the walls
                self.map.redraw()