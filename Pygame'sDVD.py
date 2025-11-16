import pygame

def main():
    pygame.init()
    screenwidth, screenheight = 500, 500
    screen = pygame.display.set_mode((screenwidth, screenheight))
    pygame.display.set_caption("Pygame Change Color on Edge Hit")

    colors = {
        "red": pygame.Color(255, 0, 0),
        "green": pygame.Color(0, 255, 0),
        "blue": pygame.Color(0, 0, 255),
        "yellow": pygame.Color(255, 255, 0),
        "white": pygame.Color(255, 255, 255),
    }
    current_color = colors["white"]
    clock = pygame.time.Clock()
    done = False
    x,y = 30,30
    sprite_width, sprite_height = 60,60

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[pygame.K_LEFT]:
            x -= 3
        elif pressed_keys[pygame.K_RIGHT]:
            x += 3
        elif pressed_keys[pygame.K_UP]:
            y -= 3 
        elif pressed_keys[pygame.K_DOWN]:
            y += 3

        x = min(max(0, x), screenwidth - sprite_width)
        y = min(max(0, y), screenheight - sprite_height)

        if x == 0:
            current_color = colors["red"]
        elif x == screenwidth - sprite_width:
            current_color = colors["green"]
        elif y == 0:
            current_color = colors["blue"]
        elif y == screenheight - sprite_height:
            current_color = colors["yellow"]
        else:
            current_color = colors["white"]
        screen.fill((0, 0, 0))
        pygame.draw.rect(screen, current_color, (x, y, sprite_width, sprite_height))
        pygame.display.flip()
        clock.tick(90)

    pygame.quit()

if __name__ == "__main__":
    main()