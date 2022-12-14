import numpy as np
import pygame


class View:
    def process_events(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        return False

    def display_frame(self, screen, frame: np.array, fps_text=None, i=0) -> None:
        surfarray = pygame.surfarray.make_surface(frame)
        screen.blit(surfarray, (0, 0))
        if fps_text:
            screen.blit(fps_text, (10, 10))
        pygame.display.update()
        pygame.image.save(surfarray, f"img/image{i}.jpg")
