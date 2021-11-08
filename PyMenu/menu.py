import pygame
import rank


class Menu():
    def __init__(self, game):
        self.game = game
        self.mid_w, self.mid_h = self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2
        self.run_display = True
        self.cursor_rect = pygame.Rect(0, 0, 20, 25)
        self.offset = - 100

    def draw_cursor(self):
        self.game.draw_text('*', 15, self.cursor_rect.x, self.cursor_rect.y)

    def blit_screen(self):
        self.game.window.blit(self.game.display, (0, 0))
        pygame.display.update()
        self.game.reset_keys()


class MainMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = "Start"
        self.startx, self.starty = self.mid_w, self.mid_h + 30
        self.optionx, self.optiony = self.mid_w, self.mid_h + 55
        self.rankingx, self.rankingy = self.mid_w, self.mid_h + 80
        self.creditsx, self.creditsy = self.mid_w, self.mid_h + 105
        self.cursor_rect.midtop = (self.startx + self.offset, self.starty)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Main Menu', 25, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Start Game", 20, self.startx, self.starty)
            self.game.draw_text("Options", 20, self.optionx, self.optiony)
            self.game.draw_text("Ranking", 20, self.rankingx, self.rankingy)
            self.game.draw_text("Credits", 20, self.creditsx, self.creditsy)
            self.draw_cursor()
            self.blit_screen()

    def move_cursor(self):
        if self.game.DOWN_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.optionx + self.offset, self.optiony)
                self.state = 'Options'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
        elif self.game.UP_KEY:
            if self.state == 'Start':
                self.cursor_rect.midtop = (
                    self.creditsx + self.offset, self.creditsy)
                self.state = 'Credits'
            elif self.state == 'Options':
                self.cursor_rect.midtop = (
                    self.startx + self.offset, self.starty)
                self.state = 'Start'
            elif self.state == 'Ranking':
                self.cursor_rect.midtop = (
                    self.optionx + self.offset, self.optiony)
                self.state = 'Options'
            elif self.state == 'Credits':
                self.cursor_rect.midtop = (
                    self.rankingx + self.offset, self.rankingy)
                self.state = 'Ranking'

    def check_input(self):
        self.move_cursor()
        if self.game.START_KEY:
            if self.state == 'Start':
                self.game.curr_menu = self.game.inputplayer
                self.game.ini_game()
            elif self.state == 'Options':
                self.game.curr_menu = self.game.options
            elif self.state == 'Credits':
                self.game.curr_menu = self.game.credits
            elif self.state == 'Ranking':
                self.game.curr_menu = self.game.ranking
            self.run_display = False


class SelectIcon(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.nameIcons = ["jet.png", "jet2.png", "jet3.png"]
        self.xIcons = [200, 300, 400]
        self.icons = []
        self.imagerects = []
        for index, item in enumerate(self.nameIcons):
            image = pygame.image.load("assets/img/" + item)
            self.icons.append(image)
            self.imagerects.append(image.get_rect(center=(400, self.xIcons[index])))
        self.index = 0

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill(self.game.BLACK)
            for index, item in enumerate(self.imagerects):
                self.game.display.blit(self.icons[index], item)
            self.game.draw_text("~>", 20, 330, self.xIcons[self.index])
            self.game.draw_text(
                'Select Your Plane', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 160)
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        if self.game.DOWN_KEY:
            if self.index < len(self.xIcons) - 1:
                self.index += 1
            else:
                self.index = 0
        if self.game.UP_KEY:
            if self.index >= 0:
                self.index -= 1
            else:
                self.index = len(self.xIcons) - 1
        if self.game.START_KEY:
            self.game.player_icon = self.nameIcons[self.index]
            #self.game.curr_menu = self.game.inputplayer
            #self.game.ini_game()
            #self.run_display = False
            self.game.playing = True
            self.run_display = False

class OptionsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)
        self.state = 'level'
        self.volx, self.voly = self.mid_w, self.mid_h + 30
        self.cursor_rect.midtop = (self.volx + self.offset, self.voly)
        self.titles_level = ["Easy", "Normal", "Hard"]
        self.player_level = 0

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            self.check_input()
            self.game.display.fill((0, 0, 0))
            self.game.draw_text(
                'Options', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 30)
            self.game.draw_text(
                "Level " + self.titles_level[self.player_level], 15, self.volx, self.voly)
            self.game.draw_text("Press Enter to change ", 13,
                                self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 150)
            self.draw_cursor()
            self.blit_screen()

    def check_input(self):
        if self.game.BACK_KEY:
            self.game.curr_menu = self.game.main_menu
            self.run_display = False
        elif self.game.START_KEY:
            if self.state == 'level':
                if self.player_level == 2:
                    self.player_level = 0
                else:
                    self.player_level += 1


class FinishGame(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.BACK_KEY or self.game.START_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text('Your score ' + str(self.game.player_score),
                                20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text("Press Enter to continue...", 13,
                                self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 150)
            self.blit_screen()


class InputPlayer(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            print(self.game.player_level)
            self.game.check_events()
            if self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            if self.game.START_KEY and len(self.game.player_name) >= 3:
                #self.game.playing = True
                #self.run_display = False
                self.game.curr_menu = self.game.selecticon
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Enter Your Name', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text(
                self.game.player_name, 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 25)
            text_screen = 'Your name must be from 3 to 10 character'
            if len(self.game.player_name) >= 3:
                text_screen = 'Press Enter to continue...'
            self.game.draw_text(
                text_screen, 13, self.game.DISPLAY_W / 2, self.game.DISPLAY_H - 150)
            self.blit_screen()


class RankingMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        items = rank.get_ranking()
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Ranking', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text(
                'Player        Score', 15, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20 + 60)
            if type(items) is not int:
                for index, item in enumerate(items):
                    self.game.draw_text(item['name'] + '        ' + item['score'], 15,
                                        self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20 + 100 + index * 25)
            self.blit_screen()


class CreditsMenu(Menu):
    def __init__(self, game):
        Menu.__init__(self, game)

    def display_menu(self):
        self.run_display = True
        while self.run_display:
            self.game.check_events()
            if self.game.START_KEY or self.game.BACK_KEY:
                self.game.curr_menu = self.game.main_menu
                self.run_display = False
            self.game.display.fill(self.game.BLACK)
            self.game.draw_text(
                'Credits', 20, self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 - 20)
            self.game.draw_text('Made by Team 2 Python Ptit', 15,
                                self.game.DISPLAY_W / 2, self.game.DISPLAY_H / 2 + 10)
            self.blit_screen()
