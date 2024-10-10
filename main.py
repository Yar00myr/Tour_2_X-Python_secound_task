import pygame
from maze.game import Game


def draw_button(screen, font, text, center_pos):
    button_text = font.render(text, True, (0, 0, 0))
    button_rect = button_text.get_rect(center=center_pos)
    screen.blit(button_text, button_rect)
    return button_rect


def handle_events(button_6x6_rect, button_10x10_rect):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            return None
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button_6x6_rect.collidepoint(event.pos):
                return 6, 6
            if button_10x10_rect.collidepoint(event.pos):
                return 10, 10
    return None


def main_menu():
    pygame.init()
    screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("Вибір розміру лабіринту")
    font = pygame.font.Font(None, 48)

    while True:
        screen.fill((255, 255, 255))

        title_text = font.render("Виберіть розмір", True, (0, 0, 0))
        title_rect = title_text.get_rect(center=(200, 50))
        screen.blit(title_text, title_rect)

        button_6x6_rect = draw_button(screen, font, "6x6", (200, 120))
        button_10x10_rect = draw_button(screen, font, "10x10", (200, 180))

        pygame.display.flip()

        result = handle_events(button_6x6_rect, button_10x10_rect)
        if result:
            return result


if __name__ == "__main__":
    grid_width, grid_height = main_menu()
    game = Game(grid_width, grid_height)
    game.run()
