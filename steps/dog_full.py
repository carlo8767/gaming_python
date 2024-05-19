import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
screen_width, screen_height = 800, 600

# Set up the display
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Collision Detection Example')

# Define colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Mole properties
mole_timer = 0
mole_interval = 2000  # 2 seconds

# Load the mole image
mole_image = pygame.image.load('dog.png')
mole_image = pygame.transform.scale(mole_image, (70, 70))
mole_rect = mole_image.get_rect()

# Player properties
player_size = 50
player_x = screen_width // 2 - player_size // 2
player_y = screen_height // 2 - player_size // 2
player_speed = 1

# Set initial mole position
mole_position = (random.randint(0, screen_width - mole_rect.width), random.randint(0, screen_height - mole_rect.height))
mole_rect.topleft = mole_position

whack_sound = pygame.mixer.Sound('ping.mp3')
# Main game loop
running = True
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get keys pressed
    keys = pygame.key.get_pressed()

    # Move the player
    if keys[pygame.K_LEFT]:
        player_x -= player_speed
    if keys[pygame.K_RIGHT]:
        player_x += player_speed
    if keys[pygame.K_UP]:
        player_y -= player_speed
    if keys[pygame.K_DOWN]:
        player_y += player_speed

    # Keep the player within the screen boundaries
    player_x = max(0, min(screen_width - player_size, player_x))
    player_y = max(0, min(screen_height - player_size, player_y))

    # Update player's rectangle
    player_rect = pygame.Rect(player_x, player_y, player_size, player_size)

    # Check for collision between player and mole
    if player_rect.colliderect(mole_rect):
        mole_position = (
        random.randint(0, screen_width - mole_rect.width), random.randint(0, screen_height - mole_rect.height))
        mole_rect.topleft = mole_position
        whack_sound.play()

    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the mole
    screen.blit(mole_image, mole_position)

    # Draw the player (a red square)
    pygame.draw.rect(screen, RED, player_rect)

    # Update the display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
