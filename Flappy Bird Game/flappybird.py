import pygame
import random

# Initialize the pygame
pygame.init()

# Screen dimensions
screen_width = 800
screen_height = 600

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)

# Game variables
gravity = 0.5
bird_movement = 0
bird_speed = -10
score = 0

# Load images
bird_img = pygame.image.load('bird.png')
bird_rect = bird_img.get_rect(center=(100, screen_height / 2))

bg_img = pygame.image.load('background.png')
base_img = pygame.image.load('base.png')

pipe_img = pygame.image.load('pipe.png')
pipe_list = []

SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the title and icon
pygame.display.set_caption("Flappy Bird")

# Font
font = pygame.font.Font('freesansbold.ttf', 32)

# Game functions
def draw_pipes(pipes):
    for pipe in pipes:
        screen.blit(pipe_img, pipe)

def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return [pipe for pipe in pipes if pipe.right > 0]

def check_collision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <= -50 or bird_rect.bottom >= 550:
        return False
    return True

def rotate_bird(bird):
    new_bird = pygame.transform.rotozoom(bird, -bird_movement * 3, 1)
    return new_bird

def bird_animation():
    new_bird = bird_frames[bird_index]
    new_bird_rect = new_bird.get_rect(center=(100, bird_rect.centery))
    return new_bird, new_bird_rect

def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_img.get_rect(midtop=(700, random_pipe_pos))
    top_pipe = pipe_img.get_rect(midbottom=(700, random_pipe_pos - 150))
    return bottom_pipe, top_pipe

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement = bird_speed
        if event.type == SPAWNPIPE:
            pipe_list.extend(create_pipe())

    # Background
    screen.blit(bg_img, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(rotate_bird(bird_img), bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Check for collision
    if not check_collision(pipe_list):
        running = False

    # Base
    screen.blit(base_img, (0, 500))

    # Update the display
    pygame.display.update()

    # Frame rate
    pygame.time.Clock().tick(120)

pygame.quit()
