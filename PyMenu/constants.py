class LevelGame:

    def __init__(self, level=0):
        self.level = level
        if self.level == 0:
            self.time_add_bullet = 2000
            self.time_add_stone = 3000
            self.time_add_alien = 4000
            self.time_add_coin_small = 1000
            self.time_add_coin_big = 2000
            self.time_add_immortal = 15000
            self.time_add_heal_small = 20000
            self.time_add_heal_big = 20000
            self.time_add_x2coin = 15000
            self.time_add_random = 20000
        elif self.level == 1:
            self.time_add_bullet = 700
            self.time_add_stone = 1000
            self.time_add_alien = 1500
            self.time_add_coin_small = 2000
            self.time_add_coin_big = 4000
            self.time_add_immortal = 25000
            self.time_add_heal_small = 25000
            self.time_add_heal_big = 30000
            self.time_add_x2coin = 20000
            self.time_add_random = 25000
        elif self.level == 2:
            self.time_add_bullet = 500
            self.time_add_stone = 700
            self.time_add_alien = 900
            self.time_add_coin_small = 5000
            self.time_add_coin_big = 10000
            self.time_add_immortal = 35000
            self.time_add_heal_small = 35000
            self.time_add_heal_big = 45000
            self.time_add_x2coin = 30000
            self.time_add_random = 30000


def getDisplay():
    DISPLAY_W, DISPLAY_H = 1200, 800
    return DISPLAY_W, DISPLAY_H
