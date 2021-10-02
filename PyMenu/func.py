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
        


