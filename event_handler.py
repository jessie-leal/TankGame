import pygame as pg
from global_vars import *
from CONSTANTS import *

class EventHandler():
    def __init__(self):
        self.display = mainDisplay
        self.events = None
        self.keys = None
        self.gameActive = False
        self.programActive = True
    
    '''
    Listen for events. Primarily for quitting the game and certain key presses.
    '''
    def listen(self):
        for event in self.events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE and not self.gameActive:
                    self.gameActive = True
                    print("Game started")
                if event.key == pg.K_r and self.gameActive:
                    self.reset()
                    self.gameActive = False
                    print("Game reset")

    '''
    Uses event.type == pg.KEYDOWN to check if a key is pressed so that the player shoots only once per key press.
    Goes through all players, and if alive, moves the player accordingly.
    '''
    def player_control_process(self):
        for event in self.events:
            if event.type == pg.KEYDOWN:
                for player in list_players:
                    if not player.hitPoints <= 0:
                        if event.key == player.controls["SHOOT"] and player.magazine > 0:
                            list_bullets.append(player.shoot())
        for player in list_players:
            if not player.hitPoints <= 0:
                player.move(self.keys)

    '''
    Updates the location of all bullets in the list using their update_location() method.
    '''
    def update_bullets(self):
        for bullet in list_bullets:
            bullet.update_location()

    '''
    Checks if a bullet has hit a player. If so, the bullet is deleted and the player takes damage.
    '''
    def check_hit(self):
        for bullet in list_bullets:
            for player in list_players:
                if bullet.owner != player:
                    if bullet.rect.colliderect(player.rect):
                        bullet.delete_self()
                        player.getHit()
                        
    '''
    Blits and draws everything game-related to the screen.
    '''   
    def update_screen(self):
        for player in list_players:
            # Rotate image but not rect
            current_frame = player.texture.call()
            current_frame = pg.transform.scale(current_frame, (PLAYER_WIDTH*1.5, PLAYER_WIDTH*1.5))
            rotated_texture = pg.transform.rotate(current_frame, -player.angle)
            rotated_rect = rotated_texture.get_rect(center=player.rect.center)
            mainDisplay.blit(rotated_texture, rotated_rect)
            # Blit smoke
            if player.hitPoints < DEFAULT_HEALTH:
                player.smoke.update()
                sized_smoke = pg.transform.scale(player.smoke.call(), (PLAYER_WIDTH*1.5, PLAYER_WIDTH*1.5))
                mainDisplay.blit(sized_smoke, (player.rect.center[0] - sized_smoke.get_width()/2, player.rect.center[1] - sized_smoke.get_height()/2))
            # Draw health bar
            pg.draw.rect(mainDisplay, pg.color.Color('black'), pg.Rect(player.rect.x-1, player.rect.y-11, player.rect.width+2, 7))
            pg.draw.rect(mainDisplay, pg.color.Color('red'), pg.Rect(player.rect.x, player.rect.y - 10, player.rect.width, 5))
            pg.draw.rect(mainDisplay, pg.color.Color('green'), pg.Rect(player.rect.x, player.rect.y - 10, player.rect.width * (player.hitPoints/DEFAULT_HEALTH), 5))
        for bullet in list_bullets:
            mainDisplay.blit(bullet.texture, (bullet.rect.center[0] - bullet.texture.get_width()/2, bullet.rect.center[1] - bullet.texture.get_height()/2))
        # debug
        if DEBUG:
            self.debug()

    '''
    Resets the game by resetting all players and bullets.
    '''
    def reset(self):
        for player in list_players:
            player.reset()
        list_bullets.clear()

    '''
    If DEBUG is True, overlays some debug information on the screen.
    '''
    def debug(self):
        font = pg.font.SysFont('Arial', 20)
        mainDisplay.blit(font.render("FPS: " + str(int(clock.get_fps())), False, pg.color.Color('black')), (0,0))
        mainDisplay.blit(font.render("Bullets: " + str(len(list_bullets)), False, pg.color.Color('black')), (0,20))
        mainDisplay.blit(font.render("Players: " + str(len(list_players)), False, pg.color.Color('black')), (0,40))
        for player in list_players:
            mainDisplay.blit(player.image, player.rect)
        for bullet in list_bullets:
            mainDisplay.blit(bullet.image, bullet.rect)
