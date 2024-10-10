import pygame
import random

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
GREY = (99, 99, 99)


class Maze:
    def __init__(self, width, height, cell_size):
        self.width = width
        self.height = height
        self.cell_size = cell_size
        self.maze = self.generate_maze()
        self.exit_pos = [height - 1, width - 1]

    def generate_maze(self):
        while True:
            # Створення випадкової матриці
            maze = [
                [random.choice([0, 1]) for _ in range(self.width)]
                for _ in range(self.height)
            ]

            maze[0][0] = 0
            maze[self.height - 1][self.width - 1] = 0

            if self.has_exit(maze):
                return maze

    def has_exit(self, maze):

        visited = [[False] * self.width for _ in range(self.height)]
        stack = [(0, 0)]
        visited[0][0] = True

        while stack:
            x, y = stack.pop()
            if (x, y) == (self.height - 1, self.width - 1):
                return True

            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if (
                    0 <= nx < self.height
                    and 0 <= ny < self.width
                    and not visited[nx][ny]
                    and maze[nx][ny] == 0
                ):
                    visited[nx][ny] = True
                    stack.append((nx, ny))

        return False

    def draw(self, screen):
        for row in range(self.height):
            for col in range(self.width):
                color = WHITE if self.maze[row][col] == 0 else BLACK
                if self.maze[row][col] == 2:
                    color = GREY
                pygame.draw.rect(
                    screen,
                    color,
                    pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                )
                pygame.draw.rect(
                    screen,
                    GREY,
                    pygame.Rect(
                        col * self.cell_size,
                        row * self.cell_size,
                        self.cell_size,
                        self.cell_size,
                    ),
                    1,
                )

        pygame.draw.rect(
            screen,
            GREEN,
            pygame.Rect(
                self.exit_pos[1] * self.cell_size,
                self.exit_pos[0] * self.cell_size,
                self.cell_size,
                self.cell_size,
            ),
        )

    def is_exit(self, x, y):
        return [x, y] == self.exit_pos

    def is_open(self, x, y):
        return self.maze[x][y] == 0

    def mark_visited(self, x, y):
        self.maze[x][y] = 2
