"""_summary_

    Returns:
        _type_: _description_
"""
import pygame


class Game(object):
    """_summary_

    Args:
        object (_type_): _description_
    """
    def __init__(self, board):
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
