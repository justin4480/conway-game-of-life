import numpy as np
from scipy.ndimage import convolve
from src.config import VideoSettings


class Board:
    def __init__(self, patterns, player):
        self.zeros = np.zeros(shape=(VideoSettings.HEIGHT, VideoSettings.WIDTH),
                              dtype=np.uint8)
        self.board = Board.downsample(self.zeros)
        self.patterns = patterns
        self.player = player
        self.populate_patterns()
        self.spawn_player()

    @staticmethod
    def upsample(array: np.array):
        return (
            array
            .repeat(VideoSettings.PIXEL_SIZE, axis=0)
            .repeat(VideoSettings.PIXEL_SIZE, axis=1)
        )

    @staticmethod
    def downsample(array: np.array):
        return array[::VideoSettings.PIXEL_SIZE, ::VideoSettings.PIXEL_SIZE]

    def get_random_x_y_board_pos(self, max_buffer_x_y):
        x_lim, y_lim = np.subtract(self.board.shape, max_buffer_x_y)
        return np.random.randint(x_lim), np.random.randint(y_lim)

    def populate_patterns(self):
        for pattern in self.patterns:
            x_pos, y_pos = self.get_random_x_y_board_pos(pattern.array.shape)
            x_size, y_size = pattern.array.shape
            self.board[x_pos:x_pos+x_size, y_pos:y_pos+y_size] = pattern.array

    def spawn_player(self, buffer=15):
        x_board, y_board = self.board.shape
        x_player, y_player = self.player.array.shape

        # create player spawn padding (protection)
        x_buffer_start = (np.round(x_board/2 - x_player/2 - buffer, 0)).astype(int)
        y_buffer_start = (np.round(y_board/2 - y_player/2 - buffer, 0)).astype(int)
        x_buffer_end = (x_buffer_start + x_player + buffer*2).astype(int)
        y_buffer_end = (y_buffer_start + y_player + buffer*2).astype(int)
        self.board[x_buffer_start:x_buffer_end, y_buffer_start:y_buffer_end] =\
            np.zeros(shape=(x_player + buffer*2, y_player + buffer*2))

        # spawn player in center of board
        # x_player_start = (np.round(x_board/2 - x_player/2, 0)).astype(int)
        # y_player_start = (np.round(y_board/2 - y_player/2, 0)).astype(int)
        # x_player_end  = (x_player_start + x_player).astype(int)
        # y_player_end  = (y_player_start + y_player).astype(int)
        # self.board[x_player_start:x_player_end, y_player_start:y_player_end] = self.player.array

    def get_next_frame(self):
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
