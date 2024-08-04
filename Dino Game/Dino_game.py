import pygame 
import random

pygame.init()

WIDTH, HEIGHT = 800, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("The Dino Game")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

dino_width = 40
dino_height = 60
dino_x = 50
dino_y = HEIGHT - dino_height - 10
dino_vel_y = 0
gravity = 1

obstacle_width = 20
obstacle_height = 40
obstacle_vel_x = -10

score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()

running = True
jumping = False
obstacles = []

while running:
    clock.tick(30)
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not jumping:
                dino_vel_y = -15
                jumping = True
    
    dino_y += dino_vel_y
    dino_vel_y += gravity
    if dino_y >= HEIGHT - dino_height - 10:
        dino_y = HEIGHT - dino_height - 10
        jumping = False
        
    pygame.draw.rect(screen, BLACK, (dino_x, dino_y, dino_width, dino_height))
    
    if len(obstacles) == 0 or obstacles[-1][0] < WIDTH - 200:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - obstacle_height - 10
        obstacles.append([obstacle_x, obstacle_y])

    for obstacle in obstacles:
        obstacle[0] += obstacle_vel_x
        pygame.draw.rect(screen, BLACK, (obstacle[0], obstacle[1], obstacle_width, obstacle_height))
        
    obstacles = [obstacle for obstacle in obstacles if obstacle[0] > -obstacle_width]
    
    for obstacle in obstacles:
        if (dino_x < obstacle[0] + obstacle_width and dino_x + dino_width > obstacle[0] and
            dino_y < obstacle[1] + obstacle_height and dino_y + dino_height > obstacle[1]):
            running = False

    score += 1
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()

pygame.quit()
