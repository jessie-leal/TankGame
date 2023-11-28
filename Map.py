import pygame.display
from CONSTANTS import *

from Wall import *

class Map():
    def __init__(self, display):
        self.display = display
        self.screensize = pygame.display.get_window_size()
        self.width = self.screensize[0]
        self.height = self.screensize[1]
        self.maze = 1
        self.map = []
        self.spawnLocs = []

    def spawnLoc(self, mazeNum, playerNum)-> (int, int, int):

        if mazeNum == 1 or mazeNum == 2:
            if playerNum == 1:
                return (70, 70, 45)
            elif playerNum == 2:
                return (1200, 640, 225)
            elif playerNum == 3:
                return (1050, 125, 135)
        else:
            if playerNum == 1:
                return (70, 650, 315)
            elif playerNum == 2:
                return(SCREEN_WIDTH-70, SCREEN_HEIGHT-610, 130)


    #draw the edges of the map
    def createMaze(self, mazeNum):
       

        # variables for the edges of the map
        self.lwall = vWall(self.height, 0, 0)
        self.rwall = vWall(self.height, self.width - 20, 0)
        self.twall = hWall(self.width, 0, 0)
        self.bwall = hWall(self.width, 0, self.height - 20)

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

            # declare inner wall variables
            self.iwall1 = hWall(200, 200, 380)
            self.iwall2 = vWall(75, 960, 330)

            # declare horizontal wall variables
            #self.lcwall1 = lcWall(100, 400)
            #self.lcwall2 = lcWall(200, 200)
            self.rcwall1 = rcWall(300, 400, self.width)
            self.rcwall2 = rcWall(200, 200, self.width)

            #clear self.map (in case the map is not the first used)
            self.map = []

            #create a list of which walls are used so the rectangles and their locations can be passed
            self.map = [self.lwall, self.rwall, self.twall, self.bwall, 
                        self.tcwall1, self.tcwall2, self.tcwall3, self.tcwall4,
                        self.bcwall1, self.bcwall2, self.bcwall3, self.bcwall4,
                        self.iwall1, self.iwall2, self.rcwall1, self.rcwall2]
            
        elif mazeNum == 2:
            # set the maze number
            self.maze = 2

            # declare inner wall variables
            self.iwall1 = hWall(180, 90, 455)
            self.iwall2 = hWall(250, 220, 250)
            self.iwall3 = vWall(250, 470, 250)
            self.iwall4 = hWall(400, 680, 200)
            self.iwall5 = hWall(400, 680, 440)
            self.iwall6 = hWall(180, 680, 330)
            self.iwall7 = vWall(260, 1080, 200)
            self.iwall8 = vWall(90, 680, 350)

            # declare border-connected wall variables
            self.bcwall1 = bcWall(130, 950, self.height)
            self.bcwall2 = bcWall(230, 150, self.height)
            self.tcwall1 = tcWall(250, 200)
            self.tcwall2 = tcWall(100, 740)

            #clear self.map (in case the map is not the first used)
            self.map = []

            self.map = [self.lwall, self.rwall, self.twall, self.bwall, 
                        self.tcwall1, self.tcwall2, self.bcwall1, self.bcwall2,
                        self.iwall1, self.iwall2, self.iwall3, self.iwall4, 
                        self.iwall5, self.iwall6, self.iwall7, self.iwall8]

        else:
            # set the maze number
            self.maze = 3

             # declare border-connected wall variables
            self.tcwall1 = tcWall(130, 120)
            self.tcwall2 = tcWall(130, 1140)
            self.bcwall1 = bcWall(130, 120, self.height)
            self.bcwall2 = bcWall(130, 1140, self.height)

            # declare inner wall variables
            self.iwall1 = hWall(300, 170, 340)
            self.iwall2 = vWall(300, 300, 200)
            self.iwall3 = hWall(300, 750, 160)
            self.iwall4 = vWall(200, 890, 70)
            self.iwall5 = hWall(300, 520, 550)
            self.iwall6 = vWall(220, 660, 450)
            self.iwall7 = vWall(200, 600, 120)

            #clear self.map (in case the map is not the first used)
            self.map = []

            self.map = [self.lwall, self.rwall, self.twall, self.bwall, 
                        self.tcwall1, self.tcwall2, self.bcwall1, self.bcwall2,
                        self.iwall1, self.iwall2, self.iwall3, self.iwall4,
                        self.iwall5, self.iwall6, self.iwall7]
        
        #create a list of safe spawn locations for each player for Map 
        self.spawnLocs = (self.spawnLoc(mazeNum, 1), self.spawnLoc(mazeNum, 2), self.spawnLoc(mazeNum, 3))


    def drawMaze(self, mazeNum):
        bgImage = pygame.image.load("resources/sprites/none.png")
        bgImage = pygame.surface.Surface(SCREEN_RES)
        bgImage.fill((0, 0, 0))
        bgImage = pygame.transform.scale(bgImage, SCREEN_RES)
        self.display.blit(bgImage, ((0, 0)))

        #takes each wall in the list of walls for each map and draws it
        for x in self.map:
            x.draw(self.display)
        
    def redraw(self):
        #gets the window size
        self.screensize = pygame.display.get_window_size()

        #sets the width and height (used for possible resizable display in future versions)
        self.width = self.screensize[0]
        self.height = self.screensize[1]

        #create the maze
        #self.createMaze(self.maze)
        #draw the maze
        self.drawMaze(self.maze)
