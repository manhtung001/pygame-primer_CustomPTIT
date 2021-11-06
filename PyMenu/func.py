import pygame

from char import *


class Func():
    def __init__(self):
        self.player_hp_last = 100
        # nhung cai

    def ini_char(self):
        self.ADD_BULLET = pygame.USEREVENT + 1
        pygame.time.set_timer(self.ADD_BULLET, 1000)
        self.ADD_STONE = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADD_STONE, 2000)
        self.ADD_ALIEN = pygame.USEREVENT + 2
        pygame.time.set_timer(self.ADD_ALIEN, 3000)
        self.ADD_CLOUD = pygame.USEREVENT + 4
        pygame.time.set_timer(self.ADD_CLOUD, 1000)
        self.ADD_COIN_SMALL = pygame.USEREVENT + 5
        pygame.time.set_timer(self.ADD_COIN_SMALL, 1500)
        self.ADD_COIN_BIG = pygame.USEREVENT + 6
        pygame.time.set_timer(self.ADD_COIN_BIG, 3000)
        self.ADD_IMMORTAL = pygame.USEREVENT + 7
        pygame.time.set_timer(self.ADD_IMMORTAL, 10000)
        self.ADD_HEAL_SMALL = pygame.USEREVENT + 8
        pygame.time.set_timer(self.ADD_HEAL_SMALL, 10000)
        self.ADD_HEAL_BIG = pygame.USEREVENT + 9
        pygame.time.set_timer(self.ADD_HEAL_BIG, 15000)
        self.ADD_X2COIN = pygame.USEREVENT + 10
        pygame.time.set_timer(self.ADD_X2COIN, 10000)
        self.ADD_RANDOM = pygame.USEREVENT + 11
        pygame.time.set_timer(self.ADD_RANDOM, 10000)

        self.player = Player()
        self.enemies = pygame.sprite.Group()
        self.clouds = pygame.sprite.Group()
        self.items = pygame.sprite.Group()
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
            if event.type == self.ADD_BULLET:
                new_bullet = Enemy("bullet")
                self.enemies.add(new_bullet)
                self.all_sprites.add(new_bullet)
            if event.type == self.ADD_STONE:
                new_stone = Enemy("stone")
                self.enemies.add(new_stone)
                self.all_sprites.add(new_stone)
            if event.type == self.ADD_ALIEN:
                new_alien = Enemy("alien")
                self.enemies.add(new_alien)
                self.all_sprites.add(new_alien)
            if event.type == self.ADD_CLOUD:
                new_cloud = Cloud()
                self.clouds.add(new_cloud)
                self.all_sprites.add(new_cloud)
            if event.type == self.ADD_COIN_SMALL:
                new_coin_small = Item("coin_small")
                self.items.add(new_coin_small)
                self.all_sprites.add(new_coin_small)
            if event.type == self.ADD_COIN_BIG:
                new_coin_big = Item("coin_big")
                self.items.add(new_coin_big)
                self.all_sprites.add(new_coin_big)
            if event.type == self.ADD_IMMORTAL:
                new_immortal = Item("immortal")
                self.items.add(new_immortal)
                self.all_sprites.add(new_immortal)
            if event.type == self.ADD_HEAL_SMALL:
                new_heal_small = Item("heal_small")
                self.items.add(new_heal_small)
                self.all_sprites.add(new_heal_small)
            if event.type == self.ADD_HEAL_BIG:
                new_heal_big = Item("heal_big")
                self.items.add(new_heal_big)
                self.all_sprites.add(new_heal_big)
            if event.type == self.ADD_X2COIN:
                new_x2coin = Item("x2coin")
                self.items.add(new_x2coin)
                self.all_sprites.add(new_x2coin)
            if event.type == self.ADD_RANDOM:
                new_random = Item("random")
                self.items.add(new_random)
                self.all_sprites.add(new_random)

    def game_update(self):
        self.player.update(pygame.key.get_pressed())
        self.enemies.update()
        self.clouds.update()
        self.items.update()

        # render
        for entity in self.all_sprites:
            self.window.blit(entity.image, entity.rect)



        if pygame.time.get_ticks() - self.player.time_start_x2Coin > self.player.time_x2Coin:
            self.player.is_x2Coin = False

        if pygame.time.get_ticks() - self.player.time_start_immortal > self.player.time_immortal:
            self.player.isImmortal = False
            self.player.image = pygame.image.load('assets/img/' + self.player_icon).convert_alpha()
            self.player.image.set_colorkey((255, 255, 255), RLEACCEL)

        for enemy in self.enemies:
            if pygame.sprite.collide_rect(self.player, enemy):
                if not self.player.isImmortal:
                    self.player_hp -= enemy.weight
                    # enemy.kill()
                enemy.kill()


        for item in self.items:
            if pygame.sprite.collide_rect(self.player, item):
                if item.type == 'random':
                    listsItem = ['immortal', 'heal_small', 'heal_big', 'x2coin']
                    item.type = random.choice(listsItem)

                if self.player.is_x2Coin:
                    self.player_score += item.weight * 2
                else:
                    self.player_score += item.weight

                if item.type == 'immortal':
                    self.player.isImmortal = True
                    self.player.image = pygame.image.load('assets/img/' + self.player_icon.split(".")[0] + 'Shell.png')
                    self.player.image.set_colorkey((0, 0, 0), RLEACCEL)
                    self.player.time_start_immortal = pygame.time.get_ticks()
                if item.type == 'heal_small':
                    if self.player_hp <= 70:
                        self.player_hp += 30
                if item.type == 'heal_big':
                    if self.player_hp <= 50:
                        self.player_hp += 50
                if item.type == 'x2coin':
                    self.player.is_x2Coin = True
                    # self.player.image = pygame.image.load('assets/img/coin.png').convert()
                    self.player.time_start_x2Coin = pygame.time.get_ticks()

                item.kill()

        self.update_check_out_game()

    def update_check_out_game(self):
        # if self.player_hp <= 0 or pyelf.player_time_start > self.player_time_max:
        if self.player_hp <= 0:
            self.player.kill()
            self.finish_game()

            # if pygame.sprite.spritecollideany(self.player, item):
