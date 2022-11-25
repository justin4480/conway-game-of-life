"""_summary_

    Returns:
        _type_: _description_
"""
import numpy as np
from scipy.ndimage import convolve
# from pattern import PatternInventory
from src.config import VideoSettings


class Board:
    """_summary_
    """
    def __init__(self, patterns):
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
