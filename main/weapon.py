import pygame
from pygame.sprite import Sprite
from animations import Animation, Spell


class Weapon(Sprite):

    def __init__(self, screen, game_settings, rect, weapon):
        super().__init__()
        self.screen = screen
        self.game_settings = game_settings
        self.xoffset = 15
        self.rotation = 45

        # Sets up state flags
        self.using = False
        self.hit = False
        self.toggled = False
        self.collision = False

        # Rotation and positioning vars
        self.rotbase = 45
        self.rottarget = 60
        self.rotrate = 5

        # Loads weapon img
        self.image_r = pygame.image.load(
            '../resources/items/weapon/' + weapon + '.png')
        self.image_l = pygame.transform.flip(self.image_r, True, False)
        # Tilts weapon
        self.image_r = pygame.transform.rotate(self.image_r, -self.rotation)
        self.image_l = pygame.transform.rotate(self.image_l, self.rotation)

        # Sets up init position/image
        self.image = self.image_r
        self.rect = self.image.get_rect()
        self.rect.left = rect.right
        self.rect.centery = rect.centery

        self.damage = game_settings.setWeaponDamage(weapon)

        self.animation = Animation(screen, game_settings.hit_path,
                         game_settings.hit_frames, game_settings.hit_size)

    def face_right(self):
        self.image = self.image_r
        self.animation.right()

    def face_left(self):
        self.image = self.image_l
        self.animation.left()

    def rotating(self, facing_right):

        if self.using and self.toggled:
            if self.rotation != self.rottarget and not self.hit:
                self.rotation += self.rotrate

                self.image = pygame.transform.rotate(self.image, -self.rotrate)
            else:
                self.hit = True

                if self.rotation != self.rotbase:
                    self.rotation -= self.rotrate

                    self.image = pygame.transform.rotate(
                        self.image, self.rotrate)
                else:
                    self.using = False
                    self.hit = False

                    if facing_right:
                        self.image = self.image_r
                    else:
                        self.image = self.image_l

    def update(self, rect, centery, facing_right):
        self.rotating(facing_right)
        self.rect.centery = centery

        if facing_right:
            self.rect.centerx = rect.right - ((rect.centerx - rect.right) / 3)
        else:
            self.rect.centerx = rect.left + ((rect.left - rect.centerx) / 3)

        self.animation.update()

    def blitme(self):
        if self.toggled:
            self.screen.blit(self.image, self.rect)

            if self.using:
                rect_anim = self.rect.copy()
                rect_anim.left = rect_anim.right
                self.animation.blitme(rect_anim)


class ProjectileSpell(Sprite):

    def __init__(self, screen, game_settings, rect, spell_path, spell_frames,
                 spell_dmg):
        super().__init__()

        self.spell = Spell(screen, rect, game_settings,
                           spell_path, spell_frames)
        self.p_spell_damage = spell_dmg
        self.active = False
        self.weapon_rect = rect

    def checkCollision(self, sprite):
        if pygame.sprite.collide_mask(self.spell, sprite):
            if not self.spell.collision:
                sprite.hp -= self.p_spell_damage
                print(sprite.name, 'hit. HP: ', sprite.hp)

            self.spell.collision = True
            self.spell.collisionRectSet(sprite.rect)
        else:
            self.spell.collision = False

    def reset(self):
        self.active = False
        self.spell.reset(self.weapon_rect)

    def face_left(self):
        if not self.active:
            self.spell.left()

    def face_right(self):
        if not self.active:
            self.spell.right()

    def update(self):
        self.spell.update()
        if self.spell.finished:
            self.reset()

    def blitme(self):
        self.spell.blitme()
