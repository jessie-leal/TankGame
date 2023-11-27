import pygame.display

from wallClass import *

class Map():
    def __init__(self, display):
        self.display = display
        self.screensize = pygame.display.get_window_size()
        self.width = self.screensize[0]
        self.height = self.screensize[1]
        self.maze = 1
        self.map = []

    def spawnLoc(self, mazeNum, playerNum)-> (int, int, int):

        if mazeNum == 1:
            if playerNum == 1:
                return (50, 50, 45)
            elif playerNum == 2:
                return (1000, 600, 225)
            elif playerNum == 3:
                return (1050, 125, 135)


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

    def drawMaze(self, mazeNum):
        if mazeNum == 1:

            #set the maze number
            self.maze = 1

            #declare vertical wall variables
            self.tcwall1 = tcWall(100, 400)
            self.tcwall2 = tcWall(200, 200)
            self.tcwall3 = tcWall(250, 600)
            self.tcwall4 = tcWall(150, 950)
            self.bcwall1 = bcWall(300, 200, self.height)
            self.bcwall2 = bcWall(200, 500, self.height)
            self.bcwall3 = bcWall(300, 740, self.height)
            self.bcwall4 = bcWall(150, 1000, self.height)

            #draw vertical wall variables
            self.tcwall1.draw(self.display)
            self.tcwall2.draw(self.display)
            self.tcwall3.draw(self.display)
            self.tcwall4.draw(self.display)
            self.bcwall1.draw(self.display)
            self.bcwall2.draw(self.display)
            self.bcwall3.draw(self.display)
            self.bcwall4.draw(self.display)

            # declare inner wall variables
            self.iwall1 = hWall(200, 200, 380)
            self.iwall2 = vWall(75, 960, 330)

            # draw inner wall variables
            self.iwall1.draw(self.display)
            self.iwall2.draw(self.display)

            # declare horizontal wall variables
            #self.lcwall1 = lcWall(100, 400)
            #self.lcwall2 = lcWall(200, 200)
            self.rcwall1 = rcWall(300, 400, self.width)
            self.rcwall2 = rcWall(200, 200, self.width)

            # draw horizontal wall variables
            #self.lcwall1.draw(self.display)
            #self.lcwall2.draw(self.display)
            self.rcwall1.draw(self.display)
            self.rcwall2.draw(self.display)

            #create a list of which walls are used so the rectangles and their locations can be passed
            self.map = [self.tcwall1, self.tcwall2, self.tcwall3, self.tcwall4,
                        self.bcwall1, self.bcwall2, self.bcwall3, self.bcwall4,
                        self.iwall1, self.iwall2, self.rcwall1, self.rcwall2]

            #create a list of safe spawn locations for each player for Map 1
            self.spawnLocs = (self.spawnLoc(1, 1), self.spawnLoc(1, 2), self.spawnLoc(1, 3))

        elif mazeNum == 2:
            # set the maze number
            self.maze = 2

            # declare vertical wall variables
            self.tcwall1 = tcWall(100, 400)
            self.tcwall2 = tcWall(200, 200)
            self.tcwall3 = tcWall(250, 600)
            self.tcwall4 = tcWall(150, 950)
            self.bcwall1 = bcWall(300, 200, self.height)
            self.bcwall2 = bcWall(200, 500, self.height)
            self.bcwall3 = bcWall(300, 740, self.height)
            self.bcwall4 = bcWall(150, 1000, self.height)

            # draw vertical wall variables
            #self.tcwall1.draw(self.display)
            #self.tcwall2.draw(self.display)
            #self.tcwall3.draw(self.display)
            #self.tcwall4.draw(self.display)
            #self.bcwall1.draw(self.display)
            #self.bcwall2.draw(self.display)
            #self.bcwall3.draw(self.display)
            #self.bcwall4.draw(self.display)

            # declare inner wall variables
            self.iwall1 = hWall(200, 200, 380)
            self.iwall2 = vWall(75, 960, 330)

            # draw inner wall variables
            #self.iwall1.draw(self.display)
            #self.iwall2.draw(self.display)

            # declare horizontal wall variables
            self.lcwall1 = lcWall(100, 400)
            self.lcwall2 = lcWall(200, 200)
            self.rcwall1 = rcWall(300, 400, self.width)
            self.rcwall2 = rcWall(200, 200, self.width)

            # draw horizontal wall variables
            # self.lcwall1.draw(self.display)
            # self.lcwall2.draw(self.display)
            #self.rcwall1.draw(self.display)
            #self.rcwall2.draw(self.display)

            self.map = [self.tcwall1, self.tcwall2, self.tcwall3, self.tcwall4,
                        self.bcwall1, self.bcwall2, self.bcwall3, self.bcwall4,
                        self.iwall1, self.iwall2, self.rcwall1, self.rcwall2]

        else:
            # set the maze number
            self.maze = 3

            # declare vertical wall variables
            self.tcwall1 = tcWall(100, 400)
            self.tcwall2 = tcWall(200, 200)
            self.tcwall3 = tcWall(250, 600)
            self.tcwall4 = tcWall(150, 950)
            self.bcwall1 = bcWall(300, 200, self.height)
            self.bcwall2 = bcWall(200, 500, self.height)
            self.bcwall3 = bcWall(300, 740, self.height)
            self.bcwall4 = bcWall(150, 1000, self.height)

            # draw vertical wall variables
            self.tcwall1.draw(self.display)
            self.tcwall2.draw(self.display)
            self.tcwall3.draw(self.display)
            self.tcwall4.draw(self.display)
            self.bcwall1.draw(self.display)
            self.bcwall2.draw(self.display)
            self.bcwall3.draw(self.display)
            self.bcwall4.draw(self.display)

            # declare inner wall variables
            self.iwall1 = hWall(200, 200, 380)
            self.iwall2 = vWall(75, 960, 330)

            # draw inner wall variables
            self.iwall1.draw(self.display)
            self.iwall2.draw(self.display)

            # declare horizontal wall variables
            # self.lcwall1 = lcWall(100, 400)
            # self.lcwall2 = lcWall(200, 200)
            self.rcwall1 = rcWall(300, 400, self.width)
            self.rcwall2 = rcWall(200, 200, self.width)

            # draw horizontal wall variables
            # self.lcwall1.draw(self.display)
            # self.lcwall2.draw(self.display)
            self.rcwall1.draw(self.display)
            self.rcwall2.draw(self.display)

            self.map = [self.tcwall1, self.tcwall2, self.tcwall3, self.tcwall4,
                        self.bcwall1, self.bcwall2, self.bcwall3, self.bcwall4,
                        self.iwall1, self.iwall2, self.rcwall1, self.rcwall2]

    def redraw(self):
        self.screensize = pygame.display.get_window_size()
        self.width = self.screensize[0]
        self.height = self.screensize[1]
        #self.display.fill((200, 0, 100))


        self.draw()
        self.drawMaze(self.maze)
