import pygame
import random
import math

pygame.init()

GAME_WIDTH = 10
GAME_HEIGHT = 10
TILE_SIZE = 40
WINDOW_WIDTH = GAME_WIDTH * TILE_SIZE
WINDOW_HEIGHT = GAME_HEIGHT * TILE_SIZE
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

player_x = 0
player_y = 0
player_found_key = False
key_x = random.randint(0, GAME_WIDTH - 1)
key_y = random.randint(0, GAME_HEIGHT - 1)
steps = 0
distance_before_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
message = ""

screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Find the Key")

font = pygame.font.SysFont(None, 24)

def display_message(message, color, x, y):
    text = font.render(message, True, color)
    screen.blit(text, (x, y))

def move_player(direction):
    global player_x, player_y, steps, player_found_key, distance_before_move, message

    previous_x, previous_y = player_x, player_y

    if direction == 'w':
        player_y = min(GAME_HEIGHT - 1, player_y + 1)
        if player_y == GAME_HEIGHT - 1:
            message = "You are at the top"
    elif direction == 'a':
        player_x = max(0, player_x - 1)
        if player_x == 0:
            message = "You are on the left side"
    elif direction == 's':
        player_y = max(0, player_y - 1)
        if player_y == 0:
            message = "You are at the bottom"
    elif direction == 'd':
        player_x = min(GAME_WIDTH - 1, player_x + 1)
        if player_x == GAME_WIDTH - 1:
            message = "You are on the right side"

    if (previous_x, previous_y) != (player_x, player_y):
        steps += 1

        if player_x == key_x and player_y == key_y:
            player_found_key = True
            return "Congratulations, you won"

        distance_after_move = math.sqrt((key_x - player_x) ** 2 + (key_y - player_y) ** 2)
        if distance_before_move > distance_after_move:
            message = "Closer"
        else:
            message = "Farther"
        distance_before_move = distance_after_move

    return None

running = True
result = None
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                result = move_player('w')
            elif event.key == pygame.K_a:
                result = move_player('a')
            elif event.key == pygame.K_s:
                result = move_player('s')
            elif event.key == pygame.K_d:
                result = move_player('d')

            if result:
                screen.fill(WHITE)
                display_message(result, BLACK, 10, 10)
                display_message(f"You needed {steps} moves", BLACK, 10, 30)
                pygame.display.flip()
                pygame.time.wait(2000)
                running = False

    screen.fill(WHITE)

    for x in range(0, WINDOW_WIDTH, TILE_SIZE):
        for y in range(0, WINDOW_HEIGHT, TILE_SIZE):
            rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

    pygame.draw.rect(screen, GREEN, (player_x * TILE_SIZE, (GAME_HEIGHT - player_y - 1) * TILE_SIZE, TILE_SIZE, TILE_SIZE))

    display_message(f"Steps: {steps}", BLACK, 10, 10)
    if not player_found_key:
        display_message(message, BLACK, 10, 30)

    pygame.display.flip()

pygame.quit()
