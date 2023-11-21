import pygame.display

from wallClass import *

class Map():
    def __init__(self, display):
        self.display = display
        self.screensize = pygame.display.get_window_size()
        self.width = self.screensize[0]
        self.height = self.screensize[1]



    #draw the edges of the map
    def draw(self):
        # bgImage = pygame.image.load("resources/fields.png")
        bgImage = pygame.image.load("resources/sprites/none.png")
        bgImage = pygame.transform.scale(bgImage, (1280, 720))
        self.display.blit(bgImage, ((0, 0)))

        # variables for the edges of the map
        self.lwall = vWall(self.height, 0, 0)
        self.rwall = vWall(self.height, self.width - 20, 0)
        self.twall = hWall(self.width, 0, 0)
        self.bwall = hWall(self.width, 0, self.height - 20)

        # draw the edges of the map
        self.lwall.draw(self.display)
        self.rwall.draw(self.display)
        self.twall.draw(self.display)
        self.bwall.draw(self.display)

    def drawMaze(self):
        #declare vertical wall variables
        self.tcwall1 = tcWall(100, 400)
        self.tcwall2 = tcWall(200, 200)
        self.bcwall1 = bcWall(300, 200, self.height)
        self.bcwall2 = bcWall(200, 400, self.height)
        self.iwall1 = hWall(200, 200, 380)

        #draw vertical wall variables
        self.tcwall1.draw(self.display)
        self.tcwall2.draw(self.display)
        self.bcwall1.draw(self.display)
        self.bcwall2.draw(self.display)
        self.iwall1.draw(self.display)

        # declare horizontal wall variables
        self.lcwall1 = lcWall(100, 400)
        self.lcwall2 = lcWall(200, 200)
        self.rcwall1 = rcWall(300, 400, self.width)
        self.rcwall2 = rcWall(200, 200, self.width)

        # draw horizontal wall variables
        #self.lcwall1.draw(self.display)
        #self.lcwall2.draw(self.display)
        self.rcwall1.draw(self.display)
        self.rcwall2.draw(self.display)

    def redraw(self):
        self.screensize = pygame.display.get_window_size()
        self.width = self.screensize[0]
        self.height = self.screensize[1]
        #self.display.fill((200, 0, 100))


        self.draw()
        self.drawMaze()
