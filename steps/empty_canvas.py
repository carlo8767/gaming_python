import pygame

pygame.init()

screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("my mega game")

x = 0
running = True
mole_image = pygame.image.load('dog.webp')
mole_image = pygame.transform.scale(mole_image, (70, 70))


# the overall event loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    x += 1
    if x>=255:
        x=0
    x_axis=0
    y_axis=40
    length=40
    width=50
    rgb_color=(255,30,40)
    background_color = (255 , 255, 255)  # Ensure x stays within 0-255 range
    screen.fill(background_color)  # update screen with new color
    pygame.draw.rect(screen, rgb_color, (x_axis, y_axis, length, width))

    screen.blit(mole_image, (150,150))
    pygame.display.update()

pygame.quit()
