import numpy as np
from scipy.ndimage import convolve
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

verbose = True

board_size = 75
max_frames = 10000

# 0 fast - 500 slow
speed = 0

# set pattern seeds
pattern_weights = [0.5, 0.3, 0.2]
k_pattern_seeds = 50
show_patterns = False

patterns = {
    "still lifes": {
        "block": np.array([
            [1, 1],
            [1, 1]]),
        "bee-hive": np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]),
        "loaf": np.array([
            [0, 1, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 0, 1],
            [0, 0, 1, 0]]),
        "boat": np.array([
            [1, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]),
        "tub": np.array([
            [0, 1, 0],
            [1, 0, 1],
            [0, 1, 0]]),
    },
    "oscillators": {
        "blinker": np.array([
            [1],
            [1],
            [1]]),
        "toad": np.array([
            [0,0,1,0],
            [1,0,0,1],
            [1,0,0,1],
            [0,1,0,0]]),
        "beacon": np.array([
            [1, 1, 0, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1],
            [0, 0, 1, 1]]),
        "pulsar": np.array([
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [1,0,0,0,0,1,0,1,0,0,0,0,1],
            [0,0,0,0,0,0,0,0,0,0,0,0,0],
            [0,0,1,1,1,0,0,0,1,1,1,0,0]]),
        "penta-decathlon": np.array([
            [0,0,0,1,0,0,0],
            [0,0,1,1,1,0,0],
            [0,1,1,0,1,1,0],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [1,1,1,0,1,1,1],
            [0,1,1,0,1,1,0],
            [0,0,1,1,1,0,0],
            [0,0,0,1,0,0,0]]),
    },
    "spaceships": {
        "glider": np.array([
            [1, 0, 0],
            [0, 1, 1],
            [1, 1, 0]]),
        "lwss": np.array([
            [0, 1, 1, 0, 0],
            [1, 1, 1, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 1, 1, 0]]),
        "mwss": np.array([
            [0, 0, 0, 1, 1, 0],
            [1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 0, 0]]),
        "hwss": np.array([
            [0, 0, 0, 0, 1, 1, 0],
            [1, 1, 1, 1, 0, 1, 1],
            [1, 1, 1, 1, 1, 1, 0],
            [0, 1, 1, 1, 1, 0, 0]]),
    },
}

if show_patterns:
    fig, ax = plt.subplots(nrows=5, ncols=3, sharex=False, sharey=False)
    plt.tight_layout()
    for col, (pattern_type, pattern) in enumerate(patterns.items()):
        for row, (pattern_name, array) in enumerate(pattern.items()):
            ylim, xlim = array.shape
            print(pattern_name, array)
            ax[row, col].imshow(array, cmap="gray_r", vmin=0, vmax=1)
            ax[row, col].set(xlim=(-1, xlim), ylim=(ylim, -1),
                             xticks=[], yticks=[], title=pattern_name)
    ax[4, 2].axis('off')
    plt.show()

# randomly select k pattern types, then randomly select patterns themselve
pattern_type = random.choices(
    population=list(patterns.keys()),
    weights=pattern_weights,
    k=k_pattern_seeds,
)
seed_patterns = [random.choice(list(patterns[p].values())) for p in pattern_type]

# randomly select position on the board to place pattern
board = np.zeros((board_size, board_size))
for pattern in seed_patterns:
    x, y = np.subtract(board.shape, pattern.shape)
    x = np.random.randint(x)
    y = np.random.randint(y)
    x_size, y_size = pattern.shape
    board[x : x + x_size, y : y + y_size] = pattern

fig, ax = plt.subplots()
frames = []
memory = {0: np.array([]), 1: np.array([])}

for frame in range(max_frames):
    if verbose and frame % 100 == 0:
        print(f"frame {frame} of {max_frames}")
    frames.append([plt.imshow(X=board, animated=True, cmap="gray")])
    neighbours = convolve(
        input=board,
        weights=np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]]),
        mode="constant",
    )
    board = board * np.isin(neighbours, [2, 3]) + (board == 0) * (neighbours == 3)    
    if np.array_equal(memory[frame % 2], board):
        print(f'breaking early on frame {frame}')
        a = memory[frame % 2]
        b = board
        break
    memory[frame % 2] = board

ani = animation.ArtistAnimation(fig, frames, interval=speed, blit=True, repeat=False)
plt.show()
