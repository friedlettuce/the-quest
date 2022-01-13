class Settings:

    def __init__(self):

        self.screen_width = 768
        self.screen_height = 448
        self.forestFile = 'resources/backgrounds/forest3.png'

        self.button_width = 200
        self.button_height = 100
        self.button_font = 24
        self.button_color = (255, 255, 255)
        self.btxt_color = (128, 128, 128)

        self.statusBarX = 103
        self.statusBarY = 14
        self.enemyBarX = 35
        self.enemyBarY = 7
        self.empty_bar = 'resources/ui/EmptyBar.png'
        self.health_bar = 'resources/ui/RedBar.png'
        self.mana_bar = 'resources/ui/BlueBar.png'

        self.fps = 18  # 15
        self.anicycle = 4

        self.floor = 32

        self.player_speed = 5
        self.player_startx = -50

        self.mob_speed = 3
        self.mobs_allowed = 2

        self.wizard = {
            'NAME': 'wizard',
            'HP': 10,
            'MANA': 60,
            'MANAREGEN': .125,
            'WEAPONS': ['green_staff', 'red_staff']
        }
        self.knight = {
            'NAME': 'knight',
            'HP': 20,
            'WEAPONS': ['big_sword', 'long_hammer', 'short_sword']
        }
        self.elf = {
            'NAME': 'elf',
            'HP': 15,
            'WEAPONS': ['axe', 'club', 'cleaver', 'rapier']
        }
        self.characters = [self.wizard, self.knight, self.elf]

        self.bigDemonHP = 9
        self.impHP = 3
        self.bigDemonDamage = (self.bigDemonHP / 4) + 1
        self.impDamage = (self.impHP / 4) + 1

        # Animations settings
        self.hit_path = 'resources/animations/attack/hit'
        self.hit_frames = 4
        self.hit_size = 16, 16

        self.ice_spell = {
            'name': 'ice spell',
            'path': 'resources/animations/ice_shard/ice_spell',
            'frames': 11,
            'cost': 5,
            'speed': 30,
            'dmg':  1,
            'sound': 'resources/wizard/ice_sound1.wav'
        }
        self.fire_spell = {
            'name': 'fireball',
            'path': 'resources/animations/fireball/fireball',
            'frames': 8,
            'cost': 10,
            'speed': 20,
            'dmg': 2,
            'sound': 'resources/wizard/fireball_sound1.wav'
        }
        self.p_spell_size = 32, 32

    def setWeaponDamage(self, weapon):
        if weapon == 'axe':
            return 5
        elif weapon == 'club':
            return 3
        elif weapon == 'long_hammer':
            return 7
        elif weapon == 'big_sword':
            return 6
        elif weapon == 'cleaver':
            return 5
        elif weapon == 'rapier':
            return 6
        elif weapon == 'green_staff':
            return 3
        elif weapon == 'short_sword':
            return 8
        elif weapon == 'red_staff':
            return 3
