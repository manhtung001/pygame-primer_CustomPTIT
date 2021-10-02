import pygame

from char import *
from menu import *
from func import *

class Game(Func):
    def __init__(self):
        Func.__init__(self)
        pygame.init()
        self.running, self.playing = True, False
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 800, 600
        self.display = pygame.Surface((self.DISPLAY_W,self.DISPLAY_H))
        self.window = pygame.display.set_mode(((self.DISPLAY_W,self.DISPLAY_H)))
        pygame.display.set_caption("Team2_Python_PTIT")
        self.font_name = 'assets/font/8-BIT WONDER.TTF'
        self.BLACK, self.WHITE = (0, 0, 0), (255, 255, 255)
        self.main_menu = MainMenu(self)
        self.options = OptionsMenu(self)
        self.ranking = RankingMenu(self)
        self.credits = CreditsMenu(self)
        self.inputplayer = InputPlayer(self)
        self.finishgame = FinishGame(self)
        self.curr_menu = self.main_menu
        self.ini_game()
        
    def ini_screen(self):
        self.display.fill(self.BLACK)
        self.FPS = 120
        self.clock = pygame.time.Clock()

    def ini_game(self):
        self.player_name = ""
        self.player_score = 0
        self.player_level = 1
        self.player_icon = 1 
        self.player_hp = 100
        self.player_hp_max = 100
        self.player_time_max = 90
        self.player_time_start = pygame.time.get_ticks()

    def finish_game(self):
        self.playing = False
        rank.insert_ranking(self.player_name, self.player_score)
        self.curr_menu = self.finishgame


    def game_loop(self):
        self.ini_screen()
        self.ini_char()
        while self.playing:
            self.update_events()
            self.window.blit(self.display, (0,0))
            self.game_update()
            self.game_draw()
            pygame.display.update()
            self.clock.tick(self.FPS)
            self.reset_keys()


    def game_draw(self):
        self.show_score(10, 10)
        if self.player_hp != self.player_hp_last:
            self.player_hp_last = self.player_hp
            pygame.draw.rect(self.display, (0,0,0), pygame.Rect(self.DISPLAY_W - 300 + (self.player_hp * 300 / self.player_hp_max) - 10, 5, (self.player_hp_max - self.player_hp) * 300, 20))


    def show_score(self, x, y):
        font = pygame.font.Font(self.font_name, 15)
        score = font.render("Score " + str(self.player_score), True, (255, 255, 255))
        w, h = score.get_size()
        pygame.draw.rect(self.display, (0,0,0), pygame.Rect(x, y, w + 10, h + 10))
        self.display.blit(score, (x, y))


    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False
                self.curr_menu.run_display = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.START_KEY = True
                if event.key == pygame.K_BACKSPACE:
                    self.BACK_KEY = True
                if event.key == pygame.K_DOWN:
                    self.DOWN_KEY = True
                if event.key == pygame.K_UP:
                    self.UP_KEY = True
                
                if self.curr_menu == self.inputplayer and event.key >= 97 and event.key <= 122 and len(self.player_name) < 10:
                    self.player_name += chr(event.key)

    def reset_keys(self):
        self.UP_KEY, self.DOWN_KEY, self.START_KEY, self.BACK_KEY = False, False, False, False


    def draw_text(self, text, size, x, y ):
        font = pygame.font.Font(self.font_name,size)
        text_surface = font.render(text, True, self.WHITE)
        text_rect = text_surface.get_rect()
        text_rect.center = (x,y)
        self.display.blit(text_surface,text_rect)