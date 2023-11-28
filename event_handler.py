import pygame as pg
from global_vars import *
from CONSTANTS import *

class EventHandler():
    def __init__(self):
        # General variables
        self.display = mainDisplay
        self.events = None
        self.keys = None
        self.programActive = True
        # Game variables
        self.currentMap = None
        self.friendlyFire = True
        self.gameActive = False
        # Win screen variables
        self.winner = None
        self.winScreenActive = False
        self.winColor = (255, 255, 255)
        # Pause screen variables
        self.paused = False
        self.pauseAngle = 0
        # Sound
        self.s = 'sound'
        self.shot = pg.mixer.Sound("Resources/sound/shot.wav")
        self.hit = pg.mixer.Sound("Resources/sound/hit.ogg")
        self.explosion = pg.mixer.Sound("Resources/sound/explosion.ogg")
        
    
    '''
    Listen for events. Primarily for quitting the game and certain key presses.
    '''
    def listen(self):
        for event in self.events:
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE and self.gameActive and not self.winScreenActive:
                    self.paused = not self.paused
                    if self.paused:
                        print("Game paused")
                if event.key == pg.K_m and self.paused:
                    self.reset()

            if event.type == pg.KEYUP:
                if self.winScreenActive:
                    if event.key == pg.K_SPACE:
                        self.gameActive = False
                        self.winScreenActive = False
                        self.resetPlayers()
                        print("Back to main menu")
                    if event.key == pg.K_r:
                        self.gameActive = True
                        self.winScreenActive = False
                        self.currentMap.redraw()
                        self.resetPlayers()
                        print("Game started")

    '''
    Fades in and out the splash screen. Displays the controls for the game.
    '''
    def control_splash_screen(self):
        mainDisplay.fill('black')
        # Fade in for 2 seconds
        ticks = 0
        while ticks <= 60:
            clock.tick(30)
            ticks += 1
            font = pg.font.Font('resources/Crang.ttf', 20)
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50, "Player 1: WASD to move, Q to shoot", font, shadow=True)
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "Player 2: Arrow keys to move, RSHIFT to shoot", font, shadow=True)
            translucent = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            translucent.set_alpha(255*(60-ticks)/20)
            mainDisplay.blit(translucent, (0,0))
            pg.display.update()
        
        # Wait 3 seconds
        ticks = 0
        while ticks <= 3:
            clock.tick(1)
            ticks += 1
        
        # Fade out for 2 seconds
        ticks = 60
        while ticks >= 0:
            clock.tick(30)
            ticks -= 1
            font = pg.font.Font('resources/Crang.ttf', 20)
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2-50, "Player 1: WASD to move, Q to shoot", font, shadow=True)
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2, "Player 2: Arrow keys to move, RSHIFT to shoot", font, shadow=True)
            translucent = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            translucent.set_alpha(255*(60-ticks)/20)
            mainDisplay.blit(translucent, (0,0))
            pg.display.update()

    '''
    Main game loop. Runs the game if gameActive is True.
    '''
    def runGame(self, map):
        if self.gameActive:
            # event handling
            if not self.paused:
                if not self.winScreenActive:
                    self.player_control_process()
                self.update_bullets()
                self.check_hit()
                self.winner = self.check_win()
            
            # Map handling
            map.redraw()

            self.update_game_screen()

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
                            bullet = player.shoot()
                            pg.mixer.Sound.play(self.shot)
                            if bullet != None:
                                list_bullets.append(bullet)
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
    Checks if a bullet has hit a non-owner player. If so, the bullet is deleted and the player takes damage.
    '''
    def check_hit(self):
        for bullet in list_bullets:
            for player in list_players:
                if (bullet.owner != player or self.friendlyFire) and bullet.lifespan < BULLET_LIFESPAN-10:
                    if bullet.rect.colliderect(player.rect):
                        if player.hitPoints == 1:
                            pg.mixer.Sound.play(self.explosion)
                            pg.mixer.music.stop()
                        else:
                            pg.mixer.Sound.play(self.hit)
                        bullet.delete_self()
                        player.getHit()    
                       
                        
    '''
    Blits and draws everything game-related to the screen. 
    Rotates the player image according to the player's angle.
    '''   
    def update_game_screen(self):
        # Blit players
        for player in list_players:
            # Rotate image but not rect
            #Sourced: https://stackoverflow.com/questions/36510795/rotating-a-rectangle-not-image-in-pygame
            current_frame = player.texture.call()
            current_frame = pg.transform.scale(current_frame, (PLAYER_WIDTH*1.5, PLAYER_WIDTH*1.5))
            rotated_texture = pg.transform.rotate(current_frame, -player.angle)
            rotated_rect = rotated_texture.get_rect(center=player.rect.center)
            mainDisplay.blit(rotated_texture, rotated_rect)
            # Blit smoke
            if player.hitPoints < DEFAULT_HEALTH:
                player.smoke.update()
                current_frame = player.smoke.call()
                current_frame = pg.transform.scale(current_frame, (PLAYER_WIDTH*1.5, PLAYER_WIDTH*1.5))
                rotated_texture = pg.transform.rotate(current_frame, -player.angle)
                rotated_rect = rotated_texture.get_rect(center=player.rect.center)
                mainDisplay.blit(rotated_texture, rotated_rect)
            # Draw health bar
            pg.draw.rect(mainDisplay, pg.color.Color('black'), pg.Rect(player.rect.x-1, player.rect.y-11, player.rect.width+2, 7))
            pg.draw.rect(mainDisplay, pg.color.Color('red'), pg.Rect(player.rect.x, player.rect.y - 10, player.rect.width, 5))
            pg.draw.rect(mainDisplay, pg.color.Color('green'), pg.Rect(player.rect.x, player.rect.y - 10, player.rect.width * (player.hitPoints/DEFAULT_HEALTH), 5))
        
        # Blit bullets
        for bullet in list_bullets:
            mainDisplay.blit(bullet.texture, (bullet.rect.center[0] - bullet.texture.get_width()/2, bullet.rect.center[1] - bullet.texture.get_height()/2))
        
        # Win screen
        if self.winner >= 0:
            self.win_screen()

        # Pause screen
        if self.paused:
            self.pause_screen()

        # Debug information. Hitboxes, FPS, number of bullets and players
        if DEBUG:
            self.debug()

    def draw_text(self, x, y, text, font, color='white', shadow=None, shadowColor='black', shadowOffset=2):
        if shadow != None:
            text_surface = font.render(text, True, pg.color.Color(shadowColor))
            text_rect = text_surface.get_rect()
            text_rect.center = (x+shadowOffset, y+shadowOffset)
            self.display.blit(text_surface, text_rect)
        text_surface = font.render(text, True, pg.color.Color(color))
        text_rect = text_surface.get_rect()
        text_rect.center = (x, y)
        self.display.blit(text_surface, text_rect)
        
    '''
    Pause screen. Displays the text "PAUSED" and rotates the player image.
    '''
    def pause_screen(self):
        #Fonts
            translucent = pg.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
            translucent.fill((0,0,0))
            translucent.set_alpha(128)
            mainDisplay.blit(translucent, (0,0))
            font = pg.font.Font('resources/Crang.ttf', 50)
            subfont = pg.font.Font('resources/Crang.ttf', 25)
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/3, "PAUSED", font, 'white', shadow=True, shadowColor='black')
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100, "Press M to return to main menu", subfont, 'white', shadow=True, shadowColor='black')
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+150, "Press ESC to return to game", subfont, 'white', shadow=True, shadowColor='black')
            #Rotating tank
            #Sourced: https://stackoverflow.com/questions/36510795/rotating-a-rectangle-not-image-in-pygame
            current_frame = list_players[0].texture.call()
            current_frame = pg.transform.scale(current_frame, (PLAYER_WIDTH*1.5, PLAYER_WIDTH*1.5))
            rotated_texture = pg.transform.rotate(current_frame, self.pauseAngle)
            self.pauseAngle = (self.pauseAngle + 1) % 360
            rotated_rect = rotated_texture.get_rect(center=(SCREEN_WIDTH/2, SCREEN_HEIGHT/2))
            mainDisplay.blit(rotated_texture, rotated_rect)

    '''
    Checks if there is only one player alive. If so, returns the player number of the winner.
    '''
    def check_win(self):
        alive = [x for x in list_players if x.hitPoints > 0]
        if len(alive) == 1:
            return alive[0].numPlayer
        elif len(alive) == 0:
            return 0
        else:
            return -1
    
    '''
    Checks if the win condition is met. If so, displays the win screen.
    '''
    def win_screen(self):
        font = pg.font.Font('resources/Crang.ttf', int(100))
        subfont = pg.font.Font('resources/Crang.ttf', int(25))
        font.set_bold(False)
        font.set_italic(True)
        #pg.mixer.Sound.play(self.explosion)
                     
        if self.winner == 1:
            self.winColor = (0, (self.winColor[1]+(SCREEN_FPS/60))%256, 0)
        elif self.winner == 2:
            self.winColor = ((self.winColor[0]+(SCREEN_FPS/60))%256, 0, 0)
        elif self.winner == 0:
            self.winColor = ((self.winColor[0]-(SCREEN_FPS/60))%256, (self.winColor[1]+(SCREEN_FPS/60))%256, 0)
            

        if self.winner > 0:
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/3, f"Player {str(self.winner)} wins!", font, pg.color.Color(self.winColor), shadow=True, shadowColor=pg.color.Color('black'), shadowOffset=4)
            self.winScreenActive = True
        if self.winner == 0:
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/3, "It's a draw!", font, pg.color.Color(self.winColor), shadow=True, shadowColor=pg.color.Color('black'), shadowOffset=4)
            self.winScreenActive = True
        if self.winScreenActive:
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+50, "Press SPACE to return to main menu", subfont, pg.color.Color('white'), shadow=True, shadowColor=pg.color.Color('black'))
            self.draw_text(SCREEN_WIDTH/2, SCREEN_HEIGHT/2+100, "Press R to restart", subfont, pg.color.Color('white'), shadow=True, shadowColor=pg.color.Color('black'))

    '''
    Resets the game by resetting all players and bullets.
    '''
    def resetPlayers(self):
        for player in list_players:
            try:
                player.reset(self.currentMap.spawnLocs[player.numPlayer-1])
                print(self.currentMap.spawnLocs[player.numPlayer-1])
            except:
                player.reset()
        list_bullets.clear()
    
    '''
    Resets the game as a whole.
    '''
    def reset(self):
        self.gameActive = False
        self.winScreenActive = False
        self.paused = False
        self.winColor = (255, 255, 255)
        self.pauseAngle = 0
        self.resetPlayers()

    '''
    If DEBUG is True, overlays some debug information on the screen.
    '''
    def debug(self):
        font = pg.font.Font(None, 20)
        mainDisplay.blit(font.render("FPS: " + str(int(clock.get_fps())), False, pg.color.Color('black')), (0,0))
        mainDisplay.blit(font.render("Bullets: " + str(len(list_bullets)), False, pg.color.Color('black')), (0,20))
        mainDisplay.blit(font.render("Players: " + str(len(list_players)), False, pg.color.Color('black')), (0,40))
        for player in list_players:
            mainDisplay.blit(player.image, player.rect)
        for bullet in list_bullets:
            mainDisplay.blit(bullet.image, bullet.rect)
