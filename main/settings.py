class Settings:

    def __init__(self):

        self.screen_width = 768
        self.screen_height = 448
        self.bg_color = (230, 230, 230)

        self.fps = 15
        self.anicycle = 4

        self.floor = 32

        self.player_speed = 5
        self.player_startx = -50

        self.mob_speed = 3
        self.mobs_allowed = 2

        self.knightHP = 20
        self.wizardHP = 10
        self.elfHP = 15

        self.bigDemonHP = 8
        self.impHP = 3
        self.bigDemonDamage = (self.bigDemonHP / 4) + 1
        self.impDamage = (self.impHP / 4) + 1

    def setWeaponDamage(self, weapon):
        if weapon == 'a':
            return 5
        elif weapon == 'b':
            return 3
        elif weapon == 'bh':
            return 7
        elif weapon == 'bs':
            return 6
        elif weapon == 'c':
            return 5
        elif weapon == 'd':
            return 6
        elif weapon == 'g':
            return 3
        elif weapon == 'ks':
            return 8
        elif weapon == 'r':
            return 3
