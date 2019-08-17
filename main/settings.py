class Settings:

    def __init__(self):

        self.playing = False
        self.screen_width = 768
        self.screen_height = 448
        self.forestFile = '../resources/backgrounds/forest3.png'

        self.button_width = 200
        self.button_height = 100
        self.button_font = 24
        self.button_color = (255, 255, 255)
        self.btxt_color = (128, 128, 128)

        self.statusBarX = 103
        self.statusBarY = 14
        self.enemyBarX = 35
        self.enemyBarY = 7
        self.empty_bar = '../resources/ui/EmptyBar.png'
        self.health_bar = '../resources/ui/RedBar.png'
        self.mana_bar = '../resources/ui/BlueBar.png'

        self.fps = 15
        self.anicycle = 4

        self.floor = 32

        self.player_speed = 5
        self.player_startx = -50

        self.mob_speed = 3
        self.mobs_allowed = 2

        self.knightHP = 20

        self.wizardHP = 10
        self.wizardMana = 60
        self.wizardManaRegen = .125

        self.elfHP = 15

        self.bigDemonHP = 9
        self.impHP = 3
        self.bigDemonDamage = (self.bigDemonHP / 4) + 1
        self.impDamage = (self.impHP / 4) + 1

        # Animations settings
        self.hit_path = '../resources/animations/attack/hit'
        self.hit_frames = 4
        self.hit_size = 16, 16

        self.ice_spell = {
            'name': 'ice spell',
            'path': '../resources/animations/ice_shard/ice_spell',
            'frames': 11,
            'cost': 5,
            'speed': 30,
            'dmg':  1
        }
        self.fire_spell = {
            'name': 'fireball',
            'path': '../resources/animations/fireball/fireball',
            'frames': 8,
            'cost': 10,
            'speed': 20,
            'dmg': 2
        }
        self.p_spell_size = 32, 32

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
