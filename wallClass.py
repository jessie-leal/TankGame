# from pyGameUtils import *
import pygame

#<a href="https://www.vecteezy.com/free-vector/brick-pattern">Brick Pattern Vectors by Vecteezy</a>


#Grass Lawn Field - Free stock photo on Pixabay - Pixabay
#https://pixabay.com/photos/grass-lawn-field-meadow-grassy-84622/
class Wall:
    def __init__(self, width, height, xpos, ypos):
        # self.image = pygame.image.load("resources/wall2.jpg")
        self.image = pygame.surface.Surface((width, height))
        self.image.fill('blue')
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(self.image.get_rect())
        self.x = xpos
        self.y = ypos
        self.rect.topleft = (self.x, self.y)

    '''
    Define a method draw() which will take in a
    display as an input parameter and will draw the
    Wall on the screen at its currently set x and y location
    '''
    def draw(self, display):
        # draw the image to the screen
        display.blit(self.image, (self.x, self.y))


    '''
    Define a method update() which will change the positions of the Berry image
     and the Rect of the berry each time it is called (it will be called once each frame).
      "drop" attribute will define how far the Berry drops down on each frame. 
    '''
    def update(self):
        #The y-coordinate of the berry should drop down by "drop" each time this is called
        self.y += self.drop
        #To move the rect as well, you can access the y attribute of the rect
        self.rect.y = self.y

    '''
    Define a method reload(), which will reload the 
    berry at the top of the screen, with y = 0. 
    This will run later on If the y coordinate of
    the Berry goes below the bottom of your screen.
    '''

    def reload(self):
        WINDOW_WIDTH = 800
        self.y = 0
        #self.x = random.randint(0, WINDOW_WIDTH)
        self.rect = pygame.Rect(self.image.get_rect())


#vertical wall
class vWall(Wall):
    def __init__(self, height, xpos, ypos):
        super().__init__(20, height, xpos, ypos)

#top connected vertical wall (how long and where located)
class tcWall(vWall):
    def __init__(self, length, xpos):
        super().__init__(length, xpos, 20)

#bottom connected vertical wall (how long, where located, and set to start at 20, so no overlap with bottom wall)
class bcWall(vWall):
    def __init__(self, length, xpos, screenHeight):
        super().__init__(length, xpos, screenHeight-length-20)


#Define horizontal walls
class hWall(Wall):
    def __init__(self, width, xpos, ypos):
        super().__init__(width, 20, xpos, ypos)

#left connected vertical wall (how long and where located)
class lcWall(hWall):
    def __init__(self, length, ypos):
        super().__init__(length, 20, ypos)

#right connected horizontal wall (how long, set to start at 20 less than the width, so no overlap with right wall, how high to place it)
class rcWall(hWall):
    def __init__(self, length, ypos, screenWidth):
        super().__init__(length, screenWidth-length-20, ypos)