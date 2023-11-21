import pygame as pg
from CONSTANTS import *
from global_vars import *

class EventHandler():
    def __init__(self):
        self.display = mainDisplay
        self.events = None
        self.keys = None

    def listen(self):
        for event in self.events:
            if event.type == pg.QUIT or self.keys[pg.K_ESCAPE]:
                pg.quit()
            if event.type == pg.KEYDOWN:
                for player in list_players:
                    if not player.dummy:
                        if event.key == player.controls["SHOOT"] and player.magazine > 0:
                            list_bullets.append(player.shoot())

    def player_control_process(self):
        for player in list_players:
            if not player.dummy:
                player.move(self.keys)
                player.update_location()

    def update_bullets(self, test_rect):
        for bullet in list_bullets:
            bullet.update_location(test_rect)
            #Delete bullet if out of bounds or lifespan is 0
            if bullet.x > SCREEN_WIDTH + 10 or bullet.x < -10 or bullet.y > SCREEN_HEIGHT + 10 or bullet.y < -10 or bullet.lifespan <= 0:
                if bullet in list_bullets:
                    bullet.owner.magazine += 1
                    list_bullets.remove(bullet)

    def check_collisions(self):
        for bullet in list_bullets:
            for player in list_players:
                if bullet.owner != player:
                    if bullet.rect.colliderect(player.rect):
                        if bullet in list_bullets:
                            bullet.lifespan = 0
                            player.getHit()
                        

    def update_screen(self):
        for player in list_players:
            # Rotate image but not rect
            current_frame = player.texture.call()
            current_frame = pg.transform.scale(current_frame, (PLAYER_WIDTH, PLAYER_WIDTH))
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

    def debug(self):
        font = pg.font.SysFont('Arial', 20)
        mainDisplay.blit(font.render("FPS: " + str(int(clock.get_fps())), False, pg.color.Color('black')), (0,0))
        mainDisplay.blit(font.render("Bullets: " + str(len(list_bullets)), False, pg.color.Color('black')), (0,20))
        mainDisplay.blit(font.render("Players: " + str(len(list_players)), False, pg.color.Color('black')), (0,40))
        for player in list_players:
            mainDisplay.blit(player.image, player.rect)
        for bullet in list_bullets:
            mainDisplay.blit(bullet.image, bullet.rect)