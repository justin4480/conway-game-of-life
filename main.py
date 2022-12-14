from itertools import count

import pygame

from src.pattern import get_patterns
from src.simulator import game_of_life
from src.view import View
from src.world import World, upsample

# Screen config
WIDTH = 600
HEIGHT = 200
PIXEL_SIZE = 1  # increase to 2 or 3 if performance is an issue
FPS = 120       # set to -1 to run at maximum FPS

# Pattern config
N_PATTERNS = 500                   # number of patterns
P_PATTERNS = [0.1, 0.1, 0.1, 0.7]  # proportion of patterns (by type)


def main():
    pygame.init()
    pygame.display.set_caption("Game of life")
    pygame.mouse.set_visible(False)
    clock = pygame.time.Clock()
    font = pygame.font.SysFont("Arial", 12)
    screen = pygame.display.set_mode(size=(WIDTH, HEIGHT))

    patterns = get_patterns(n_patterns=N_PATTERNS, p_patterns=P_PATTERNS)
    world = World(int(HEIGHT / PIXEL_SIZE), int(WIDTH / PIXEL_SIZE))
    world.populate_world(patterns)
    simulator = game_of_life(world.array)
    view = View()

    terminate = False
    i = count(1)

    while not terminate:
        terminate = view.process_events()
        frame = upsample(next(simulator), PIXEL_SIZE).T * 255
        fps_text = font.render(
            f"frame {next(i)} | fps: {str(int(clock.get_fps()))}", 1, pygame.Color("coral")
        )
        view.display_frame(screen, frame, fps_text)
        clock.tick(FPS)

    pygame.quit()


if __name__ == "__main__":
    main()
