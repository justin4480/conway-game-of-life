import pygame


class View():

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def display_frame(self, screen, frame, fps):
        if fps:
            surfarray = pygame.surfarray.make_surface(frame)
            screen.blit(fps, (10, 10))
        screen.blit(surfarray, (0, 0))
        pygame.display.update()
