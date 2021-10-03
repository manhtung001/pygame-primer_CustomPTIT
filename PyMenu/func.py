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
        pygame.time.set_timer(self.ADD_CLOUD, 1000)
        self.ADD_COIN = pygame.USEREVENT + 3
        pygame.time.set_timer(self.ADD_COIN, 1000)

        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.all_sprites = pygame.sprite.Group()
        self.all_sprites.add(self.player)

        pygame.draw.rect(self.display, (255, 0, 0),
                         pygame.Rect(self.DISPLAY_W - 300 - 10, 5, self.player_hp * 300 / self.player_hp_max, 20))
        pygame.draw.rect(self.display, (255, 0, 0),
                         pygame.Rect(self.DISPLAY_W - 300 - 10, 5, self.player_hp * 300 / self.player_hp_max, 20), 2)

    def update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == self.ADD_ENEMY:
                new_enemy = Enemy(1)
                self.enemies.add(new_enemy)
                self.all_sprites.add(new_enemy)
            if event.type == self.ADD_CLOUD:
                new_cloud = Cloud()
                self.clouds.add(new_cloud)
                self.all_sprites.add(new_cloud)
            if event.type == self.ADD_COIN:
                new_coin = Coin()
                self.coins.add(new_coin)
                self.all_sprites.add(new_coin)

    def game_update(self):
        self.player.update(pygame.key.get_pressed())
        self.enemies.update()
        self.clouds.update()
        self.coins.update()
        # render
        for entity in self.all_sprites:
            self.window.blit(entity.image, entity.rect)

        # for enemy in self.enemies:
        #     if pygame.sprite.spritecollide(self.player, self.enemies, True):
        #         self.player_hp -= 1
        #
        #
        # for item in self.coins:
        #     if pygame.sprite.spritecollide(self.player, self.coins, True):
        #         self.player_score += 1


        if pygame.sprite.spritecollide(self.player, self.enemies, True):
            self.player_hp -= 1
        if pygame.sprite.spritecollide(self.player, self.coins, True):
            self.player_score += 1

        # isinstance()

        #
        #
        # if obecjt.type == 1
        #     hp += 100
        # if (object.type == 2)
        #     object.time_last_eat = pygame.time.get_ticks();
        #
        #
        # for item
        #         type = 1;
        #         if (pygame.time.get_ticks() - object.time_eat_last < object.time_eat_max){
        #                 player.is_bat_tu = true
        #         } else {
        #             batut = false
        #         }
        #             player.ise
        #         i

        self.update_check_out_game()

    def update_check_out_game(self):
        # if self.player_hp <= 0 or pygame.time.get_ticks() - self.player_time_start > self.player_time_max:
        if self.player_hp <= 0:
            self.player.kill()
            self.finish_game()


            # if pygame.sprite.spritecollideany(self.player, item):

