from global_vars import *
import pygame as pg
from CONSTANTS import *
import math

class Texture():
    def __init__(self, image, isAnimated = False, frames = 1, frameTime = 1):
        self.image = pg.image.load(image)
        self.subImages = []
        self.isAnimated = isAnimated
        self.reverse = False
        self.frames = frames
        self.frameTime = frameTime

        self.currentFrame = 0
        self.currentFrameTime = 0

    def update(self):
        if self.isAnimated:
            if self.reverse:
                if self.currentFrameTime >= self.frameTime:
                    self.currentFrameTime = 0
                    self.currentFrame -= 1
                    if self.currentFrame < 0:
                        self.currentFrame = self.frames - 1
                self.currentFrameTime += 1
            else:
                if self.currentFrameTime >= self.frameTime:
                    self.currentFrameTime = 0
                    self.currentFrame += 1
                    if self.currentFrame >= self.frames:
                        self.currentFrame = 0
                self.currentFrameTime += 1

    def call(self):
        if self.isAnimated:
            if self.isAnimated:
                cropped_region = pg.Rect(0, self.currentFrame*self.image.get_height()//self.frames, self.image.get_width(), self.image.get_height()//self.frames)
                return pg.surface.Surface.subsurface(self.image, cropped_region)
        else:
            return self.image

class Player():
    def __init__(self, numPlayer, texture: Texture = None, coord: tuple = (0,0), angleDeg: int = 0, controls: list = "Dummy"):
        """
        image: Pick color according to pygame's list of colors pg.color.THECOLORS
        coord: (x, y) tuple
        controls: [up, left, down, right] default is dummy
        """
        
        self.numPlayer = numPlayer
        self.hitPoints = DEFAULT_HEALTH
        self.magazine = DEFAULT_MAGAZINE_SIZE
        self.currentPowerup = None
        self.dummy = False

        self.texture = texture if texture != None else pg.image.load("assets/none.png")
        self.smoke = Texture("resources/sprites/smoke.png", isAnimated = True, frames = 6, frameTime = 10)
        # self.smoke.image = pg.transform.scale(self.smoke.image, PLAYER_SIZE)
        self.smoke.image.set_alpha(0)
        self.image = pg.surface.Surface(PLAYER_SIZE)
        self.image.fill(pg.color.Color('purple'))
        self.image.set_alpha(125)
        self.rect = self.image.get_rect()
        self.x = coord[0]
        self.y = coord[1]
        self.rect.center = (self.x, self.y)
        self.angle = angleDeg
        
        #Controls
        if len(controls) != 5 or controls == "Dummy":
            self.dummy = True
            self.controls = None
        else:
            self.controls = {"FORWARD": controls[0],
                             "BACK": controls[1], 
                             "LEFT": controls[2], 
                             "RIGHT": controls[3],
                             "SHOOT": controls[4]
                             }
    
    def move(self, keys):
        current_coords = (self.x, self.y)
        if keys[self.controls["BACK"]]:
            self.x -= math.cos(math.radians(self.angle))
            self.y -= math.sin(math.radians(self.angle))
            self.texture.reverse = True
            self.texture.update()
        if keys[self.controls["FORWARD"]]:
            self.x += math.cos(math.radians(self.angle)) * PLAYER_SPEED
            self.y += math.sin(math.radians(self.angle)) * PLAYER_SPEED
            self.texture.reverse = False
            self.texture.update()
        if keys[self.controls["LEFT"]]:
            self.angle -= PLAYER_TURNING_SPEED
            self.texture.update()
        if keys[self.controls["RIGHT"]]:
            self.angle += PLAYER_TURNING_SPEED
            self.texture.update()
        
        if self.validate_movement():
            self.update_location()
        else:
            self.x = current_coords[0]
            self.y = current_coords[1]

    def validate_movement(self):
        collidedObject = self.rect.collideobjects(collision_list)
        temp_rect = self.rect.copy()
        temp_rect.center = (self.x, self.y)
        if collidedObject != None:
            if collidedObject.colliderect(temp_rect):
                return False
        if self.x < 0 or self.x > SCREEN_WIDTH or self.y < 0 or self.y > SCREEN_HEIGHT:
            return False
        return True
    
    def update_location(self):
        self.rect.center = (self.x, self.y)
        self.angle %= 360

    def shoot(self):
        angle_rad = math.radians(self.angle)

        if self.currentPowerup == None:
            self.magazine -= 1
            return Bullet((self.rect.centerx + math.sqrt(0.5)*self.rect.width*math.cos(angle_rad), #Edge of player in circle
                               self.rect.centery + math.sqrt(0.5)*self.rect.height*math.sin(angle_rad)), #Edge of player
                               angle_rad, self)
        
    def getHit(self):
        if self.hitPoints > 0:
            self.hitPoints -= 1
            self.smoke.image.set_alpha(255//DEFAULT_HEALTH * (DEFAULT_HEALTH-self.hitPoints))
        if self.hitPoints <= 0:
            self.dummy = True
        
class Bullet():
    def __init__(self, coord, angleRad, owner = None):
        self.texture = pg.image.load("resources/sprites/bullet.png")
        self.texture = pg.transform.scale(self.texture, (BULLET_WIDTH*1.4, BULLET_WIDTH*1.4))
        self.image = pg.Surface(BULLET_SIZE)
        self.image.fill(pg.color.Color('red'))
        self.rect = self.image.get_rect()
        self.x = coord[0]
        self.y = coord[1]
        self.rect.center = (self.x, self.y)
        self.angle = angleRad
        self.lifespan = BULLET_LIFESPAN
        self.speed = BULLET_SPEED
        self.owner = owner

    def update_location(self):
        self.x += math.cos(self.angle) * self.speed
        self.y += math.sin(self.angle) * self.speed
        self.rect.center = (self.x, self.y)
        self.lifespan -= 1
        self.speed *= 1 - BULLET_DECELERATION
        #Fade out
        if self.lifespan < 20:
            self.texture.set_alpha(self.lifespan * 10)
        #Bounce
        collidedObject = self.rect.collideobjects(collision_list)
        if(collidedObject != None):
            side = self.determine_side(collidedObject)
            if side == "TOP" or side == "BOTTOM":
                self.angle = -self.angle
            elif side == "LEFT" or side == "RIGHT":
                self.angle = math.pi - self.angle

        #Delete bullet if out of bounds or lifespan is 0
        if self.x > SCREEN_WIDTH + 10 or self.x < -10 or self.y > SCREEN_HEIGHT + 10 or self.y < -10 or self.lifespan <= 0:
            if self in list_bullets:
                self.owner.magazine += 1
                list_bullets.remove(self)


    def determine_side(self, collidedObject):
        # Slopes of collidedObject (top left to bottom right) and (top right to bottom left)
        slope1 = (collidedObject.topleft[1] - collidedObject.bottomright[1]) / (collidedObject.topleft[0] - collidedObject.bottomright[0])
        slope2 = (collidedObject.topright[1] - collidedObject.bottomleft[1]) / (collidedObject.topright[0] - collidedObject.bottomleft[0])

        # Check if bullet is between the two slopes
        isAbove1 = self.rect.center[1] < slope1 * self.rect.center[0] + (collidedObject.topleft[1] - slope1 * collidedObject.topleft[0])
        isAbove2 = self.rect.center[1] < slope2 * self.rect.center[0] + (collidedObject.topright[1] - slope2 * collidedObject.topright[0])
        
        if isAbove1 and isAbove2:
            return "TOP"
        elif not isAbove1 and not isAbove2:
            return "BOTTOM"
        elif isAbove1 and not isAbove2:
            return "RIGHT"
        elif not isAbove1 and isAbove2:
            return "LEFT"
        else:
            return "ERROR"
        
class Laser():
    def __init__(self, coord, angleRad, owner = None):
        self.x = coord[0]
        self.y = coord[1]
        self.angle = angleRad
        self.owner = owner