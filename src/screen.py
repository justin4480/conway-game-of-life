"""_summary_

    Returns:
        _type_: _description_
"""
import pygame
import numpy as np
from scipy.ndimage import convolve
from src.pattern import PatternInventory


class VideoSettings():
    """_summary_

    Args:
        Enum (_type_): _description_
    """
    WIDTH = 800
    HEIGHT = 800
    PIXEL_SIZE = 2
    FPS = 60


class Board:
    """_summary_
    """
    def __init__(self, patterns: PatternInventory):
        self.zeros = np.zeros(shape=(VideoSettings.HEIGHT, VideoSettings.WIDTH),
                              dtype=np.uint8)
        self.board = Board.downsample(self.zeros)
        self.patterns = patterns
        self.populate()

    @staticmethod
    def upsample(array: np.array):
        """_summary_

        Args:
            array (np.array): _description_

        Returns:
            _type_: _description_
        """
        return (
            array
            .repeat(VideoSettings.PIXEL_SIZE, axis=0)
            .repeat(VideoSettings.PIXEL_SIZE, axis=1)
        )

    @staticmethod
    def downsample(array: np.array):
        """_summary_

        Args:
            array (np.array): _description_

        Returns:
            _type_: _description_
        """
        return array[::VideoSettings.PIXEL_SIZE, ::VideoSettings.PIXEL_SIZE]

    def populate(self):
        """_summary_
        """
        for pattern in self.patterns:
            x, y = np.subtract(self.board.shape, pattern.array.shape)
            x = np.random.randint(x)
            y = np.random.randint(y)
            x_size, y_size = pattern.array.shape
            self.board[x : x + x_size, y : y + y_size] = pattern.array

    def get_next_frame(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        neighbours = convolve(
            input=self.board,
            weights=np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            mode="constant",
        )

        # Any live cell with fewer than 2 live neighbours dies, as if by underpopulation.
        # Any live cell with 2 or 3 live neighbours lives on to the next generation.
        # Any live cell with more than 3 live neighbours dies, as if by overpopulation.
        live_cells = self.board * np.isin(neighbours, (2, 3))

        # Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction.
        dead_cells = (self.board==0) * (neighbours==3)

        self.board = live_cells + dead_cells
        return Board.upsample(self.board).T * 255


class Game(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self, board: Board):
        self.board = board

    def process_events(self):
        """_summary_

        Returns:
            _type_: _description_
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def display_frame(self, screen):
        """_summary_

        Args:
            screen (_type_): _description_
        """
        array = self.board.get_next_frame()
        surfarray = pygame.surfarray.make_surface(array)
        screen.blit(surfarray, (0, 0))
        pygame.display.update()


def main():
    """_summary_
    """
    pygame.init()
    pygame.display.set_caption("Game of life")
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(size=(VideoSettings.WIDTH,
                                           VideoSettings.HEIGHT))
    clock = pygame.time.Clock()

    patterns = PatternInventory().get_patterns(n=200)
    board = Board(patterns)
    game = Game(board)

    end = False

    while not end:
        end = game.process_events()
        game.display_frame(screen)
        clock.tick(VideoSettings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
