import numpy as np
from scipy.ndimage import convolve


def game_of_life(array):
    """
        # Any live cell with fewer than 2 live neighbours dies, as if by underpopulation.
        # Any live cell with 2 or 3 live neighbours lives on to the next generation.
        # Any live cell with more than 3 live neighbours dies, as if by overpopulation.
        live_cells = array * np.isin(neighbours, (2, 3))

        # Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction.
        dead_cells = (array == 0) * (neighbours == 3)
    """
    while True:
        neighbours = convolve(
            input=array,
            weights=np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
            mode="constant",
        )
        live_cells = (array == 1) * np.isin(neighbours, (2, 3))
        dead_cells = (array == 0) * (neighbours == 3)
        array = (live_cells + dead_cells).astype(np.uint8)
        yield array
