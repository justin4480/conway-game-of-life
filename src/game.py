import pygame
from src.config import VideoSettings


class Game(object):
    def __init__(self, board):
        self.board = board
        self.next_frame_array = None
        self.player_sprite = Player()
        self.all_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player_sprite)

    def process_events(self):
        self.next_frame_array = self.board.get_next_frame()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
        if self.check_player_collide():
            return True
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.player_sprite.rect.x -= 2
        if keys[pygame.K_RIGHT]:
            self.player_sprite.rect.x += 2
        if keys[pygame.K_UP]:
            self.player_sprite.rect.y -= 2
        if keys[pygame.K_DOWN]:
            self.player_sprite.rect.y += 2

    def display_frame(self, screen):
        surfarray = pygame.surfarray.make_surface(self.next_frame_array)
        screen.blit(surfarray, (0, 0))
        self.all_sprites_list.draw(screen)
        pygame.display.update()

    def check_player_collide(self):
        return self.next_frame_array[self.player_sprite.rect.x:self.player_sprite.rect.x+5,
                                     self.player_sprite.rect.y:self.player_sprite.rect.y+5].sum() > 0


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([5, 5])
        self.image.fill((0,255,0))
        self.rect = self.image.get_rect()
        self.rect.x = int(VideoSettings.WIDTH / 2)
        self.rect.y = int(VideoSettings.HEIGHT / 2)
