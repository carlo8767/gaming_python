import pygame
import random
pygame.init()

screen_width=800
screen_height=600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("my mega game")

x = 0
running = True
mole_image = pygame.image.load('dog.webp')
mole_image = pygame.transform.scale(mole_image, (70, 70))
mole_position = (random.randint(0, screen_width), random.randint(0, screen_height ))
mole_timer = pygame.time.get_ticks()
player_speed=5
# the overall event loop
x_axis = 0
y_axis = 0
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 1
    if x>=255:
        x=0

    length=40
    width=50
    rgb_color=(255,30,40)
    background_color = (255 , 255, 255)  # Ensure x stays within 0-255 range
    if pygame.time.get_ticks() - mole_timer > 2000:
        mole_position = (random.randint(0, screen_width-70), random.randint(0, screen_height-70 ))

        mole_timer = pygame.time.get_ticks()
    screen.fill(background_color)  # update screen with new color
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        x_axis -= 1
    if keys[pygame.K_RIGHT]:
        x_axis += 1
    if keys[pygame.K_UP]:
        y_axis -= 1
    if keys[pygame.K_DOWN]:
        y_axis += 1
    pygame.draw.rect(screen, rgb_color, (x_axis, y_axis, length, width))


    screen.blit(mole_image, mole_position)
    pygame.display.update()

pygame.quit()
