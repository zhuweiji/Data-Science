import pygame
from pygame.locals import *


def main():
    screen = pygame.display.set_mode((640, 480))
    font = pygame.font.Font(None, 32)
    clock = pygame.time.Clock()
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')

    color = color_inactive
    active = False
    text = ''
    running = False

    while not running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = True
            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                    color = color_active
                else:
                    active = False
                    color = color_inactive

            if event.type == KEYDOWN:
                if active:
                    if event.key == K_RETURN:
                        print(text)
                        text = ''
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill((30, 30, 30))
        # Render the current text.
        txt_surface = font.render(text, True, color)
        # Resize the box if the text is too long.
        width = max(200, txt_surface.get_width() + 10)
        input_box.w = width
        # Blit the text.
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        # Blit the input_box rect.
        pygame.draw.rect(screen, color, input_box, 2)

        pygame.display.flip()
        clock.tick(30)


pygame.init()
main()
pygame.quit()