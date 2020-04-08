import pygame
import time
from pygame.locals import *



black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)

pygame.init()
""" all display related options here """

# x pos, y pos, width, height
input_box = pygame.Rect(800, 500, 200, 50) # input box for users to enter their choices
outline = pygame.Rect(700, 0, 500, 870) # background for all program functions

display_width = 1200
display_height = 870

screen = pygame.display.set_mode((display_width, display_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Hello world!")
background = pygame.image.load(r"C:\Users\User1\Desktop\alex mini project\map.png").convert()
font = pygame.font.Font('freesansbold.ttf', 32)
font2 = pygame.font.Font('freesansbold.ttf',18)


def menu(option):
    _find_distance = 1
    _closest_canteen = 2
    option = int(option)
    if option == _find_distance:
        print('find distance')
    elif option == _closest_canteen:
        print('closest canteen')




def display_inputbox(state,text):
    """ input box for user to enter their choices """
    inactive_colour = pygame.Color('lightskyblue3')
    active_colour = pygame.Color('dodgerblue2')

    if state == 1:
        color = active_colour
    else:
        color = inactive_colour

    txt_surface = font.render(text, True, color)
    # Resize the box if the text is too long.
    width = max(200, txt_surface.get_width() + 10)
    input_box.w = width
    screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
    pygame.draw.rect(screen, color, input_box, 2)

    pygame.display.flip()
    clock.tick(30)


def display_menu():
    line0 = "Please select an option:"
    line1 = "1 - Find the distance to all canteens"
    line2 = "2 - Find the closest canteen"
    line3 = "3 - Look for food cheaper than a set price"
    line4 = "4 - Search for food which meets your dietary requirements"
    line5 = "5 - More options"
    line6 = "6 -  all the stalls within a canteen"
    line7 = "7 - Check if a store will be open at a certain time"
    line8 = "8 -  the capacities of the canteens"
    line9 = "9 - Less options"
    line10 = "0 - Exit"
    list_lines = [line0,line1,line2,line3,line4,line5,line6,line7,line8,line9,line10]
    for offset, line in enumerate(list_lines):
        program_text_surface = font2.render(line, True, black)
        screen.blit(program_text_surface, (outline.x + 20, 0 + 45*offset))
    pygame.display.update()


def game_loop():
    running = True
    text = ''
    state = 0
    screen.blit(background, (0, 0))
    pygame.draw.rect(screen, pygame.Color('white'), outline, 0)
    display_menu()


    while running:
        display_inputbox(state, text)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    state = 1
                else:
                    state = 0
            if event.type == KEYDOWN:
                if state == 1:
                    if event.key == K_RETURN:
                        menu(text)
                        text = ''
                    elif event.key == K_BACKSPACE:
                        text = text[:-1]
                        print(text)
                    else:
                        text += event.unicode

                display_inputbox(1,text)
                pygame.display.update()






game_loop()
pygame.quit()
exit(0)


