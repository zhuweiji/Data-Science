print("Loading.....")
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
from re import *
import pygame
import pandas as pd
from math import *


DATA_FILE = "NTU map_dataset.csv"
MAP_FILE = "map.png"
FONT = 'freesansbold.ttf'

data_set = pd.read_csv(DATA_FILE)
df = pd.DataFrame(data_set)

white = (255, 255, 255)
green = (0, 128, 0)
blue = (0, 0, 128)
red = (128, 0, 0)
black = (255, 255, 255)
x_size, y_size = (700, 870) #  pygame window size

MAP_SCALE = 225/93 #  map is ~2.4m to one grid square


AUTHORS = 'Alex, Edward, Hui Shan'


# ------------------------------------  FUNCTION DEFINITIONS ---------------------------------------------------------


def find_distance():
    pygame.init()
    display_surface = pygame.display.set_mode((x_size, y_size), 0, 32)
    pygame.display.set_caption("Map of NTU")
    background = pygame.image.load(MAP_FILE).convert()
    display_surface.blit(background, (0, 0))
    pygame.display.update()

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('\n\n')
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                x1, y1 = pygame.mouse.get_pos()
                display_surface.blit(background, (0, 0))
                print(x1,y1)

                pygame.display.update()


                #FIND DISTANCE
                distance_list = []
                for i in range(len(data_set)):
                    distance = int(MAP_SCALE * sqrt(
                        (int(data_set['x'][i]) - x1)**2 + (int(data_set['y'][i]) - y1)**2 ))

                    distance_list.append(distance)
                    print("Distance from {} is {}m".format(df.iloc[i,0],distance))

                df['Distance'] = distance_list
                df.sort_values(by=['Distance'], inplace=True, ascending=True)  # sorting by distances in ascending order

                # select the nearest canteen by position based off 'Distance' value
                closest_canteen = df.iloc[0, 0]
                print("\n--------------------------------------------------------------------------------------")
                print(closest_canteen)
                print("The nearest canteen is", closest_canteen, "which is", min(distance_list), "meters away.")
                print('--------------------------------------------------------------------------------------\n\n')

    pygame.quit()


def price_food():
    """ searches for food within a budget with robust error checking """
    try:
        price = input("What is your budget? Enter a dollar amount(5.50)  >")
        price = price.replace('$', '')
        price = float(price)
        print('\n')
        if price < 6:
            if price >= 5:
                print("Canteen 1 and Quad Cafe have food under 5 dollars\n\n")

            if price >= 4:
                print("Canteen 2, Canteen 11, Canteen 16 and North Spine Food Court have food under 4 dollars\n\n")

            if price >= 3:
                print("Canteen 9, Canteen 13, Canteen 14 and South Spine Food Court have food under 3 dollars\n\n")

            else:
                print("Price is too low, please try another value.\n\n")
                price_food()

        else:
            print("Any canteen's available for you!\n\n")
        print('\n')

    except ValueError:
        print("Please enter a dollar value\n\n")
        price_food()


def check_requirements():
    """ error checking includes regex replacement of all special characters, and case-insensitivity """
    dietreq = input("What dietary requirement do you have? (Halal | Vegetarian | Both):").casefold()
    dietreq = sub('[^A-Za-z0-9]+', '', dietreq)
    if dietreq == "halal":
        print(
            "Canteen 2, Canteen 9, Canteen 11, Canteen 13, Canteen 14, Canteen 16,\n"
            "Quad Cafe, North Spine Food Court and South Spine Food Court have Halal food stalls.\n\n")

    elif dietreq == "vegetarian":
        print("Quad Cafe, North Spine Food Court and South Spine Food Court have Vegetarian food stall.\n\n")

    elif dietreq == "both":
        print("Quad Cafe, North Spine Food Court and South Spine Food Court have Vegetarian and Halal food stalls.\n\n")

    else:
        print("We can only search for canteens with Halal or Vegetarian stalls.\n\n")


def check_hours():
    try:
        search_time = input("Enter the hour you will be visiting (0-23):")

        if search_time.find('pm'.casefold()) != -1:
            if search_time.find(':') != -1:
                search_time = search_time[0:search_time.find(':')]
            if search_time.find('.') != -1:
                search_time = search_time[0:search_time.find('.')]
            search_time = sub(r'[^0-9]+', '', search_time)
            search_time = int(search_time)
            search_time += 12

        else:
            if search_time.find(':') != -1:
                search_time = search_time[0:search_time.find(':')]
            if search_time.find('.') != -1:
                search_time = search_time[0:search_time.find('.')]
            search_time = sub(r'[^0-9]+', '', search_time)
            search_time = int(search_time)


        if search_time < 7:
            print("Timing is too early, no canteens are open yet.\n\n")

        elif search_time > 21:
            print("Timing is too late, no canteens are still open.\n\n")

        elif 7 <= search_time <= 21:
            print("All of the canteens are open.\n\n")

    except ValueError:
        print("Please enter a valid number\n\n")
        check_hours()


def print_capacity():
    for row in range(len(data_set)):
        print("{} has {} seats".format(df.iloc[row, 0], df.iloc[row, 6]))
    print('\n\n')


def menu():
    print("Please select an option:")
    print("1 - Look for the closest canteen from a point")
    print("2 - Look for food cheaper than a set price")
    print("3 - Search for food which meets your dietary requirements")
    print("4 - Check if a store will be open at a certain time")
    print("5 - Print the capacities of the canteens")
    print("0 - Exit")

    _find_distance = 1
    _price_food = 2
    _check_requirements = 3
    _check_hours = 4
    _print_capacity = 5
    _exit = 0
    _WAIT_VALUE = 0.7

    try:
        choice = int(input('\n\n'))

        if choice == _find_distance:
            print('--------------------------------------------------------------\n')
            print("Please close the window to return to the menu")
            find_distance()
            print('--------------------------------------------------------------\n')
            time.sleep(_WAIT_VALUE)

        elif choice == _price_food:
            print('--------------------------------------------------------------\n')
            price_food()
            print('--------------------------------------------------------------\n')
            time.sleep(_WAIT_VALUE)

        elif choice == _check_requirements:
            print('--------------------------------------------------------------\n')
            check_requirements()
            print('--------------------------------------------------------------\n')
            time.sleep(_WAIT_VALUE)

        elif choice == _check_hours:
            print('--------------------------------------------------------------\n')
            check_hours()
            print('--------------------------------------------------------------\n')
            time.sleep(_WAIT_VALUE)

        elif choice == _print_capacity:
            print('--------------------------------------------------------------\n')
            print_capacity()
            print('--------------------------------------------------------------\n')
            time.sleep(_WAIT_VALUE)

        elif choice == _exit:
            print("Thank you for using our program!\n"
                  ,AUTHORS)
            time.sleep(_WAIT_VALUE)
            exit(0)

        else:
            raise ValueError

    except ValueError:
        print("Enter a valid option")
        menu()

# --------------------------------------------------------------------------------------------------------------------

print('Loading complete!')
while True:
    menu()

