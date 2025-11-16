import pygame 
pygame.init()
screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Hollow and Solid Circles Example")
screen.fill((255, 255, 255))
done = False

pygame.draw.circle(screen, (0,255,0), (150, 150), 50)
pygame.draw.circle(screen, (0,255,0), (350, 150), 50, 3)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    pygame.display.flip()