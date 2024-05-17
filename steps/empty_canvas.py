import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("my mega game")

x = 0
running = True

# the overall event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 1
    if x>=255:
        x=0
    background_color = (x , 20, 255)  # Ensure x stays within 0-255 range
    screen.fill(background_color)  # update screen with new color
    pygame.display.update()

pygame.quit()
