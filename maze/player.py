import pygame


RED = (255, 0, 0)


class Player:
    def __init__(self, start_pos):
        self.position = start_pos

    def draw(self, screen, cell_size):
        pygame.draw.rect(
            screen,
            RED,
            pygame.Rect(
                self.position[1] * cell_size,
                self.position[0] * cell_size,
                cell_size,
                cell_size,
            ),
        )

    def move(self, new_position):
        self.position = new_position
