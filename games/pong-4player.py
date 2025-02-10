import pygame
import random

# Initialize Pygame
pygame.init()

# Game Constants
WIDTH, HEIGHT = 800, 600
BALL_RADIUS = 10
PADDLE_SIZE = 80
PADDLE_THICKNESS = 10
BALL_SPEED = 5
PADDLE_SPEED = 5

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Create Game Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("4-Player Pong")

# Ball Object
ball = {
    "x": WIDTH // 2,
    "y": HEIGHT // 2,
    "dx": BALL_SPEED * random.choice([-1, 1]),
    "dy": BALL_SPEED * random.choice([-1, 1])
}

# Paddle Positions
paddles = {
    "left": {"x": 10, "y": HEIGHT // 2 - PADDLE_SIZE // 2},
    "right": {"x": WIDTH - 20, "y": HEIGHT // 2 - PADDLE_SIZE // 2},
    "top": {"x": WIDTH // 2 - PADDLE_SIZE // 2, "y": 10},
    "bottom": {"x": WIDTH // 2 - PADDLE_SIZE // 2, "y": HEIGHT - 20}
}

clock = pygame.time.Clock()
running = True
while running:
    screen.fill(BLACK)
    
    # Draw Ball
    pygame.draw.circle(screen, RED, (ball["x"], ball["y"]), BALL_RADIUS)
    
    # Draw Paddles
    for key, paddle in paddles.items():
        if key in ["left", "right"]:
            pygame.draw.rect(screen, WHITE, (paddle["x"], paddle["y"], PADDLE_THICKNESS, PADDLE_SIZE))
        else:
            pygame.draw.rect(screen, WHITE, (paddle["x"], paddle["y"], PADDLE_SIZE, PADDLE_THICKNESS))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move Ball
    ball["x"] += ball["dx"]
    ball["y"] += ball["dy"]
    
    # Collision with paddles
    if ball["x"] - BALL_RADIUS <= paddles["left"]["x"] + PADDLE_THICKNESS and paddles["left"]["y"] <= ball["y"] <= paddles["left"]["y"] + PADDLE_SIZE:
        ball["dx"] *= -1
    if ball["x"] + BALL_RADIUS >= paddles["right"]["x"] and paddles["right"]["y"] <= ball["y"] <= paddles["right"]["y"] + PADDLE_SIZE:
        ball["dx"] *= -1
    if ball["y"] - BALL_RADIUS <= paddles["top"]["y"] + PADDLE_THICKNESS and paddles["top"]["x"] <= ball["x"] <= paddles["top"]["x"] + PADDLE_SIZE:
        ball["dy"] *= -1
    if ball["y"] + BALL_RADIUS >= paddles["bottom"]["y"] and paddles["bottom"]["x"] <= ball["x"] <= paddles["bottom"]["x"] + PADDLE_SIZE:
        ball["dy"] *= -1
    
    # AI Movement
    if ball["dx"] < 0 and paddles["left"]["y"] + PADDLE_SIZE / 2 < ball["y"]:
        paddles["left"]["y"] += PADDLE_SPEED
    elif paddles["left"]["y"] + PADDLE_SIZE / 2 > ball["y"]:
        paddles["left"]["y"] -= PADDLE_SPEED
    
    if ball["dx"] > 0 and paddles["right"]["y"] + PADDLE_SIZE / 2 < ball["y"]:
        paddles["right"]["y"] += PADDLE_SPEED
    elif paddles["right"]["y"] + PADDLE_SIZE / 2 > ball["y"]:
        paddles["right"]["y"] -= PADDLE_SPEED
    
    if ball["dy"] < 0 and paddles["top"]["x"] + PADDLE_SIZE / 2 < ball["x"]:
        paddles["top"]["x"] += PADDLE_SPEED
    elif paddles["top"]["x"] + PADDLE_SIZE / 2 > ball["x"]:
        paddles["top"]["x"] -= PADDLE_SPEED
    
    if ball["dy"] > 0 and paddles["bottom"]["x"] + PADDLE_SIZE / 2 < ball["x"]:
        paddles["bottom"]["x"] += PADDLE_SPEED
    elif paddles["bottom"]["x"] + PADDLE_SIZE / 2 > ball["x"]:
        paddles["bottom"]["x"] -= PADDLE_SPEED
    
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
