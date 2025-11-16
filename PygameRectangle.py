import pygame
pygame.init()

screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("Rectangle Example")
done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.draw.rect(screen, (0, 0, 255), (30, 30, 60, 60))

    pygame.display.flip()