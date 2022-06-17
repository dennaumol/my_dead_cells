import pygame

TILE_SCALE = 2.5

from settings import *
image = pygame.image.load('data/images/grayrock/tiles-rock-colour3-alpha_01.png')
silver_rock = pygame.transform.scale(image,
                                     (int(image.get_width() * TILE_SCALE),
                                      int(image.get_height() * TILE_SCALE))).convert_alpha(screen)


class Tile(pygame.sprite.Sprite):
    def __init__(self, x, y, collsion=True):
        super(Tile, self).__init__()
        self.collision = collsion


class SilverRock(Tile):
    def __init__(self, x, y):
        super(SilverRock, self).__init__(x, y)
        self.image = silver_rock
        self.rect = image.get_rect()
        self.rect.center = x, y








