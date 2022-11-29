import numpy as np
from scipy.ndimage import convolve


def game_of_life(array) -> np.array:
    """
    # Any live cell with fewer than 2 live neighbours dies, as if by underpopulation.
    # Any live cell with 2 or 3 live neighbours lives on to the next generation.
    # Any live cell with more than 3 live neighbours dies, as if by overpopulation.
    live_cells = array * np.isin(neighbours, (2, 3))

    # Any dead cell with exactly 3 live neighbours becomes a live cell, as if by reproduction.
    dead_cells = (array == 0) * (neighbours == 3)
    """
    weights = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    while True:
        neighbours = convolve(
            input=array,
            weights=weights,
            mode="constant",
        )
        live_cells = (array == 1) * np.isin(neighbours, (2, 3))
        dead_cells = (array == 0) * (neighbours == 3)
        array = (live_cells + dead_cells).astype(np.uint8)
        yield array


# Tensorflow implementation works, but have commented out as this is slower than
# the numpy / scipy implementation when ran on a CPU.  Yet to benchmark, but would
# expect tenorflow to outperform when running tensorflow on a GPU.  If enabled
# although not in the requements.txt tensorflow will be needed.

# import tensorflow as tf

# def game_of_life_tensorflow(array: np.array) -> np.array:
#     dtype = tf.int32
#     x_original, y_original = array.shape
#     filters = tf.constant(tf.reshape([[1, 1, 1], [1, 0, 1], [1, 1, 1]], (3, 3, 1, 1)))
#     array = tf.constant(tf.reshape(tf.cast(array, dtype=dtype), (1, x_original, y_original, 1)))

#     while True:
#         neighbours = tf.nn.conv2d(array, filters, strides=[1, 1], padding="SAME")
#         live_cells_2 = tf.math.multiply(
#             tf.cast(array == 1, dtype=dtype), tf.cast(neighbours == 2, dtype=dtype)
#         )
#         live_cells_3 = tf.math.multiply(
#             tf.cast(array == 1, dtype=dtype), tf.cast(neighbours == 3, dtype=dtype)
#         )
#         dead_cells_3 = tf.math.multiply(
#             tf.cast(array == 0, dtype=dtype), tf.cast(neighbours == 3, dtype=dtype)
#         )
#         array = live_cells_2 + live_cells_3 + dead_cells_3
#         yield array.numpy().reshape(x_original, y_original)
