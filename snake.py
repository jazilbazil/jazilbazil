import pygame
import random

# Define constants
WIDTH = 400
HEIGHT = 400
CELL_SIZE = 10
FPS = 10

# Initialize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define game variables
snake = [(WIDTH/2, HEIGHT/2)]
direction = random.choice(["up", "down", "left", "right"])
food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
score = 0

# Define functions
def draw_cell(color, row, col):
    x = col * CELL_SIZE
    y = row * CELL_SIZE
    pygame.draw.rect(screen, color, (x, y, CELL_SIZE, CELL_SIZE))

def draw_snake():
    for cell in snake:
        draw_cell(GREEN, cell[1], cell[0])

def move_snake():
    global direction, food, score
    head = snake[0]
    if direction == "up":
        new_head = (head[0], head[1]-CELL_SIZE)
    elif direction == "down":
        new_head = (head[0], head[1]+CELL_SIZE)
    elif direction == "left":
        new_head = (head[0]-CELL_SIZE, head[1])
    elif direction == "right":
        new_head = (head[0]+CELL_SIZE, head[1])
    if new_head == food:
        snake.insert(0, new_head)
        food = (random.randrange(0, WIDTH, CELL_SIZE), random.randrange(0, HEIGHT, CELL_SIZE))
        score += 1
    elif new_head[0] < 0 or new_head[0] >= WIDTH or new_head[1] < 0 or new_head[1] >= HEIGHT or new_head in snake:
        pygame.quit()
        quit()
    else:
        snake.pop()
        snake.insert(0, new_head)

def draw_food():
    draw_cell(RED, food[1]//CELL_SIZE, food[0]//CELL_SIZE)

def draw_score():
    font = pygame.font.SysFont(None, 25)
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))

# Game loop
clock = pygame.time.Clock()
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "down":
                direction = "up"
            elif event.key == pygame.K_DOWN and direction != "up":
                direction = "down"
            elif event.key == pygame.K_LEFT and direction != "right":
                direction = "left"
            elif event.key == pygame.K_RIGHT and direction != "left":
                direction = "right"

    # Update game state
    move_snake()

    # Draw graphics
    screen.fill(BLACK)
    draw_snake()
    draw_food()
    draw_score()
    pygame.display.update()

    # Delay to control FPS
    clock.tick(FPS)

# Quit Pygame
pygame.quit()
