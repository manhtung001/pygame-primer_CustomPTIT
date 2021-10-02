from game import Game
from func import *


g = Game()

while g.running:
    g.curr_menu.display_menu()
    g.game_loop()
