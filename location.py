from tiles import *
from random import *


class Location:
    pass


class SilverCavern(Location):
    def load(self):
        blocks = []
        y = 0
        x = 0
        tile_height = tile_width = silver_rock.get_height()
        for __ in range(100):
            for ___ in range(randint(3, 8)):
                block = SilverRock(x, y)
                blocks.append(block)
                under_y = y + tile_height
                for i in range(10):
                    block = SilverRock(x, under_y)
                    blocks.append(block)
                    under_y += tile_height
                x += tile_width
            up = choice([True, False])
            if up:
                y -= tile_height
            else:
                y += tile_height
        return blocks












