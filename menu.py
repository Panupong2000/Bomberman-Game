import pygame

import game
from button import Button
from algorithm import Algorithm

pygame.display.init()
INFO = pygame.display.Info()
TILE_SIZE = int(INFO.current_h * 0.035)
WINDOW_SIZE = (13 * TILE_SIZE, 13 * TILE_SIZE)

player_alg = Algorithm.PLAYER
en1_alg = Algorithm.DFS
en2_alg = Algorithm.DFS
en3_alg = Algorithm.DFS
show_path = True
surface = pygame.display.set_mode(WINDOW_SIZE)

def run_game():
    game.game_init(show_path, player_alg, en1_alg, en2_alg, en3_alg, TILE_SIZE, button)


clock = pygame.time.Clock()

button = Button(surface.get_width() // 2, surface.get_height() // 2, 200, 50, (200, 200, 200), (150, 150, 150), "Play Game", "Bomberman Game", 30, run_game)
font = pygame.font.SysFont('Bebas', 30)
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = pygame.mouse.get_pos()
                if button.rect.collidepoint(mouse_pos):
                    button.do_action()

    surface.fill((255, 255, 255))
    mouse_pos = pygame.mouse.get_pos()
    button.draw(surface, mouse_pos)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
