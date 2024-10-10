import pygame
import time
from .maze import Maze
from .player import Player


CELL_SIZE = 40


class Game:
    def __init__(self, grid_width, grid_height):
        self.screen = pygame.display.set_mode(
            (grid_width * CELL_SIZE, grid_height * CELL_SIZE)
        )
        pygame.display.set_caption("Лабіринт")
        self.maze = Maze(grid_width, grid_height, CELL_SIZE)
        self.player = Player([0, 0])
        self.running = True
        self.game_over = False

    def backtrack(self, x, y):
        if self.maze.is_exit(x, y):
            return True

        self.maze.mark_visited(x, y)

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nx, ny = x + dx, y + dy
            if (
                0 <= nx < self.maze.height
                and 0 <= ny < self.maze.width
                and self.maze.is_open(nx, ny)
            ):
                self.player.move([nx, ny])
                self.render()
                time.sleep(0.2)
                if self.backtrack(nx, ny):
                    return True
        return False

    def render(self):
        self.screen.fill((255, 255, 255))
        self.maze.draw(self.screen)
        self.player.draw(self.screen, CELL_SIZE)
        if self.game_over:
            self.display_retry_message()
        pygame.display.update()

    def display_retry_message(self):
        font = pygame.font.Font(None, 36)
        text = self._render_centered_text(font, "Натисніть R, щоб повторити")
        self.screen.blit(*text)

    def _render_centered_text(self, font, message):
        text = font.render(message, True, (0, 0, 0))
        text_rect = text.get_rect(
            center=(self.maze.width * CELL_SIZE / 2, self.maze.height * CELL_SIZE / 2)
        )
        return text, text_rect

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

            if event.type == pygame.KEYDOWN:
                print(f"Key pressed: {pygame.key.name(event.key)}")
                if event.key == pygame.K_r:
                    self.reset_game()

    def run(self):
        while self.running:
            self.render()
            self.handle_events()

            if not self.game_over:
                self.check_player_progress()

        pygame.quit()

    def check_player_progress(self):
        if self.player.position == [0, 0]:
            if self.backtrack(self.player.position[0], self.player.position[1]):
                print("Вітаємо, комп'ютер знайшов вихід з лабіринту!")
            else:
                print("Комп'ютер не зміг знайти вихід :(")
                self.game_over = True

    def reset_game(self):
        self.maze = Maze(self.maze.width, self.maze.height, CELL_SIZE)
        self.player = Player([0, 0])
        self.game_over = False
