import numpy as np


class World:
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.array = self.generate_world()

    def generate_world(self):
        return np.zeros(shape=(self.height, self.width), dtype=np.uint8)

    def populate_world(self, sprites):
        for sprite in sprites:
            x_pos, y_pos = self.get_random_x_y_world_pos()
            self.add_sprite(sprite, x_pos, y_pos)

    def get_random_x_y_world_pos(self):
        x_lim, y_lim = self.array.shape
        return np.random.randint(x_lim), np.random.randint(y_lim)

    def add_sprite(self, sprite, x_start, y_start):
        x_end, y_end = np.array([x_start, y_start]) + sprite.shape
        x_chop, y_chop = np.maximum(
            np.array([0, 0]),
            np.subtract(
                np.array([x_end, y_end]),
                np.array([self.height, self.width])
            )
        )
        self.array[x_start:x_end-x_chop, y_start:y_end-y_chop] =\
            sprite[:-x_chop or None, :-y_chop or None]

    def depopulate_zone(self, x_start, x_end, y_start, y_end):
        self.array[x_start:x_end+1, y_start:y_end+1] = 0


def upsample(array: np.array, factor):
    return array.repeat(factor, axis=0).repeat(factor, axis=1)


def downsample(array: np.array, factor):
    return array[:: factor, :: factor]
