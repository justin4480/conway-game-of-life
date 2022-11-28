import pygame


class View(object):
    def __init__(self, frame_generator):
        self.frame_generator = frame_generator

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True

    def display_frame(self, screen, fps, func):
        frame = func(next(self.frame_generator))
        surfarray = pygame.surfarray.make_surface(frame)
        screen.blit(surfarray, (0, 0))
        screen.blit(fps, (10, 10))
        pygame.display.update()
