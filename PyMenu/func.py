import pygame

from char import *

class Func():
    def __init__(self):
        self.player_hp_last = 100

        # nhung cai 
        
    def ini_char(self):
        self.ADD_ENEMY = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADD_ENEMY, 250)
        self.ADD_CLOUD = pygame.USEREVENT + 2

        self.player = Player()
        pygame.time.set_timer(self.ADD_CLOUD, 1000)
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.DISPLAY_W - 300 - 10, 5, self.player_hp * 300 / self.player_hp_max, 20))
        pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.DISPLAY_W - 300 - 10, 5, self.player_hp * 300 / self.player_hp_max, 20), 2)

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == self.ADD_ENEMY:
                new_enemy = Enemy()
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)
            if event.type == self.ADD_CLOUD:
                new_cloud = Cloud()
                self.all_sprites.add(new_cloud)
                self.clouds.add(new_cloud) 


    def game_update(self):
        self.game_draw()
        self.player.update(pygame.key.get_pressed())
        self.enemies.update()
        self.clouds.update()
        for entity in self.all_sprites:
            self.window.blit(entity.image, entity.rect)
        if pygame.sprite.spritecollideany(self.player, self.enemies):
            self.player_hp -= 1
            self.player_score += 1
            if self.player_hp <= 0:
                self.player.kill()
                self.finish_game()
        


    def game_draw(self):
        self.draw_text_screen('Score: ' + str(self.player_score), 25, 70, 10)
        #self.draw_text_screen('Time: ' + str(int((pygame.time.get_ticks() - self.player_time_start) / 1000)), 25, self.DISPLAY_W - 150, self.DISPLAY_H - 20)
        if self.player_hp != self.player_hp_last:
            self.player_hp_last = self.player_hp
            pygame.draw.rect(self.display, (0,0,0), pygame.Rect(self.DISPLAY_W - 300 + (self.player_hp * 300 / self.player_hp_max) - 10, 5, (self.player_hp_max - self.player_hp) * 300, 20))



        #pygame.draw.rect(self.display, (255,0,0), pygame.Rect(self.DISPLAY_W - 300 - 10, 5, 300, 20), 2)
    
    def draw_text_screen(self, text, size, x, y ):
        font = pygame.font.Font(pygame.font.get_default_font(),size)
        text_surface = font.render(text, True, (255, 255, 255))
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface, text_rect)
