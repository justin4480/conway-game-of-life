import numpy as np
import pygame


def array_from_text(text: str, height: int, width: int, font: str, font_size=int) -> np.array:
    pygame.init()
    font = pygame.font.SysFont(font, font_size)
    img = font.render(text, True, (255, 255, 255))
    screen = pygame.Surface((width, height))
    screen.blit(img, (20, 20))
    array = np.rot90(np.fliplr(pygame.surfarray.array3d(screen)))[:, :, 0] / 255
    array[::3, :] = 0
    array[:, ::3] = 0
    return array


class World:
    def __init__(self, height: int, width: int) -> None:
        self.height = height
        self.width = width
        self.array = self.generate_world()

    def generate_world(self) -> np.array:
        return np.zeros(shape=(self.height, self.width), dtype=np.uint8)

    def populate_world_from_string(self, string: str) -> None:
        self.array = array_from_text(string, self.height, self.width, "Times New Roman", 100)

    def populate_world(self, sprites: list[np.array]) -> None:
        for sprite in sprites:
            x_pos, y_pos = self.get_random_x_y_world_pos()
            self.add_sprite(sprite, x_pos, y_pos)

    def get_random_x_y_world_pos(self) -> np.array:
        x_lim, y_lim = self.array.shape
        return np.random.randint(x_lim), np.random.randint(y_lim)

    def add_sprite(self, sprite: np.array, x_start: int, y_start: int) -> None:
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

    def depopulate_zone(self, x_start: int, x_end: int, y_start: int, y_end: int):
        self.array[x_start:x_end+1, y_start:y_end+1] = 0


def upsample(array: np.array, factor: int = 1) -> np.array:
    return array.repeat(factor, axis=0).repeat(factor, axis=1)


def downsample(array: np.array, factor: int = 1) -> np.array:
    return array[::factor, ::factor]
