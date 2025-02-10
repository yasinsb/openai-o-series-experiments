import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 400
BALL_RADIUS = 10
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 80
PADDLE_SPEED = 8  # Paddle speed
BALL_SPEED_X, BALL_SPEED_Y = 10, 6  # Ball speed
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)  # Ball color changed to red

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("AI Pong Game")

# Ball Object
ball = {
    "x": WIDTH // 2,
    "y": HEIGHT // 2,
    "speed_x": BALL_SPEED_X if random.random() > 0.5 else -BALL_SPEED_X,
    "speed_y": BALL_SPEED_Y if random.random() > 0.5 else -BALL_SPEED_Y
}

# Paddles
left_paddle = {"x": 20, "y": HEIGHT // 2 - PADDLE_HEIGHT // 2}
right_paddle = {"x": WIDTH - 30, "y": HEIGHT // 2 - PADDLE_HEIGHT // 2}

clock = pygame.time.Clock()

running = True
while running:
    screen.fill(BLACK)
    pygame.draw.circle(screen, RED, (ball["x"], ball["y"]), BALL_RADIUS)  # Ball is red
    pygame.draw.rect(screen, WHITE, (left_paddle["x"], left_paddle["y"], PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (right_paddle["x"], right_paddle["y"], PADDLE_WIDTH, PADDLE_HEIGHT))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move Ball
    ball["x"] += ball["speed_x"]
    ball["y"] += ball["speed_y"]

    # Ball Collision with Walls
    if ball["y"] - BALL_RADIUS <= 0 or ball["y"] + BALL_RADIUS >= HEIGHT:
        ball["speed_y"] = -ball["speed_y"]

    # Ball Collision with Paddles
    if (ball["x"] - BALL_RADIUS <= left_paddle["x"] + PADDLE_WIDTH and 
        left_paddle["y"] <= ball["y"] <= left_paddle["y"] + PADDLE_HEIGHT):
        ball["speed_x"] = -ball["speed_x"]

    if (ball["x"] + BALL_RADIUS >= right_paddle["x"] and 
        right_paddle["y"] <= ball["y"] <= right_paddle["y"] + PADDLE_HEIGHT):
        ball["speed_x"] = -ball["speed_x"]

    # Reset Ball if it goes off-screen
    if ball["x"] - BALL_RADIUS <= 0 or ball["x"] + BALL_RADIUS >= WIDTH:
        ball["x"], ball["y"] = WIDTH // 2, HEIGHT // 2
        ball["speed_x"] = BALL_SPEED_X if random.random() > 0.5 else -BALL_SPEED_X
        ball["speed_y"] = BALL_SPEED_Y if random.random() > 0.5 else -BALL_SPEED_Y

    # AI Paddles (Move only when ball is approaching)
    if ball["speed_x"] < 0:  # Ball moving towards left paddle
        if left_paddle["y"] + PADDLE_HEIGHT // 2 < ball["y"]:
            left_paddle["y"] += PADDLE_SPEED
        elif left_paddle["y"] + PADDLE_HEIGHT // 2 > ball["y"]:
            left_paddle["y"] -= PADDLE_SPEED

    if ball["speed_x"] > 0:  # Ball moving towards right paddle
        if right_paddle["y"] + PADDLE_HEIGHT // 2 < ball["y"]:
            right_paddle["y"] += PADDLE_SPEED
        elif right_paddle["y"] + PADDLE_HEIGHT // 2 > ball["y"]:
            right_paddle["y"] -= PADDLE_SPEED

    pygame.display.flip()
    clock.tick(60)

pygame.quit()