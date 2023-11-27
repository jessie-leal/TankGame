import pygame as pg

'''
Constants that are used in multiple files. Edit these at your own risk.
The game was designed in 60FPS, so changing the FPS may cause some unwanted issues.
Items in paranthesis should be left alone.
SPEEDs should be pixel per frame, so changing the FPS should not affect the speed of the game.
'''

#Screen Settings
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
SCREEN_RES = (SCREEN_WIDTH, SCREEN_HEIGHT)
SCREEN_FPS = 120 #Also controls the speed of the game. 60FPS as base

#Player Settings
PLAYER_WIDTH = 40
PLAYER_SIZE = (PLAYER_WIDTH, PLAYER_WIDTH)
PLAYER_SPEED = 2*(60/SCREEN_FPS)
PLAYER_TURNING_SPEED = 360/(120/(60/SCREEN_FPS))
DEFAULT_HEALTH = 3
DEFAULT_MAGAZINE_SIZE = 3

#Control Presets [FORWARD, BACK, LEFT, RIGHT, SHOOT]
CONTROL_PRESET = {"WASD": [pg.K_w, pg.K_s, pg.K_a, pg.K_d, pg.K_q],
                  "ARROWS": [pg.K_UP, pg.K_DOWN, pg.K_LEFT, pg.K_RIGHT, pg.K_RCTRL]}

#Bullet Settings
BULLET_WIDTH = 10
BULLET_SIZE = (BULLET_WIDTH, BULLET_WIDTH)
BULLET_SPEED = 4*(60/SCREEN_FPS)
BULLET_DECELERATION = 0.00
BULLET_LIFESPAN = 200 * (SCREEN_FPS/60)

#Debug
DEBUG = False