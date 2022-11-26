"""_summary_
    """
import pygame
from src.board import Board
from src.game import Game
from src import pattern
from src.config import VideoSettings


def main():
    """_summary_
    """
    pygame.init()
    pygame.display.set_caption("Game of life")
    pygame.mouse.set_visible(False)
    screen = pygame.display.set_mode(size=(VideoSettings.WIDTH,
                                           VideoSettings.HEIGHT))
    clock = pygame.time.Clock()

    patterns = pattern.get_patterns(n_patterns=3000, probabilities=[0.1,0.1,0.8])
    player = pattern.player
    board = Board(patterns, player)
    game = Game(board)

    end = False

    while not end:
        end = game.process_events()
        game.display_frame(screen)
        clock.tick(VideoSettings.FPS)

    pygame.quit()

if __name__ == "__main__":
    main()
