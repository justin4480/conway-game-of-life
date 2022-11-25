"""_summary_
    """
import pygame
from src.board import Board
from src.game import Game
from src.pattern import PatternInventory
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

    patterns = PatternInventory().get_patterns(n=500)
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
