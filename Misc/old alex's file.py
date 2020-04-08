"""TO DO LIST: fill in functions
                create pygame interface
                create main program
                """
""" Potentially: create display on pygame interface to display messages"""


import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import time
from re import *
import pygame
import numpy as np
import pandas as pd

data_file = r"NTU map_dataset"
map_file = r"NTU MAP.png"
FONT = 'freesansbold.ttf'

white = (255, 255, 255)
green = (0, 128, 0)
blue = (0, 0, 128)
red = (128, 0, 0)
black = (255, 255, 255)
x_size, y_size = (700, 870)
#data = pd.read_csv(data_file) # encoding = cp1252??
#dataset.head(10) ??


"""     functions in program:
distance: Find distance from all canteens | find closest canteen
foodprice: Shld change to option to choose all under price (maybe under pygame)? or display all prices in that canteen
operatinghours: Displays all operating hours, and check if canteen is open
numstalls: Provide number of stalls in a canteen
seatingcapacity: Seating capacity of each canteen
dietaryrequirement: Check against dietary requirements
showmsg: check options

"""
# ------------------------------------  FUNCTION DEFINITIONS ---------------------------------------------------------


def find_distance():
    pass


def closest_canteen():
    pass


def price_food():
    """ searches for food within a budget with robust error checking """
    try:
        price = input("What is your budget? Enter a dollar amount(5.50)  >")
        price = price.replace('$', '')
        price = float(price)
        print('\n')
        if price < 6:
            if price >= 5:
                print("Canteen 1 and Quad Cafe have food under 5 dollars")

            if price >= 4:
                print("Canteen 2, Canteen 11, Canteen 16 and North Spine Food Court have food under 4 dollars")

            if price >= 3:
                print("Canteen 9, Canteen 13, Canteen 14 and South Spine Food Court have food under 3 dollars")

            else:
                print("Price is too low, please try another value.")

        else:
            print("Any canteen's available for you!")
        print('\n')

    except ValueError:
        print("Please enter a dollar value")
        price_food()


def check_requirements():
    """ error checking includes regex replacement of all special characters, and case-insensitivity """
    dietreq = input("What dietary requirement do you have? (Halal | Vegetarian | Both):").casefold()
    dietreq = sub('[^A-Za-z0-9]+', '', dietreq)
    if dietreq == "halal":
        print(
            "Canteen 2, Canteen 9, Canteen 11, Canteen 13, Canteen 14, Canteen 16,\n"
            "Quad Cafe, North Spine Food Court and South Spine Food Court have Halal food stalls.")

    elif dietreq == "vegetarian":
        print("Quad Cafe, North Spine Food Court and South Spine Food Court have Vegetarian food stall.")

    elif dietreq == "both":
        print("Quad Cafe, North Spine Food Court and South Spine Food Court have Vegetarian and Halal food stalls.")

    else:
        print("We can only search for canteens with Halal or Vegetarian stalls.")




def print_stalls():
    try:
        canteen = input("Enter the canteen you would like to search within").casefold()


    except ValueError:
        print("Canteen not found")
    pass


def check_hours():
    try:
        search_time = input("Enter the hour you will be visiting (0-23):")
        if search_time.find('pm'.casefold()):
            search_time = float(sub('[^0-9]+', '', search_time))
            search_time += 12
        else:
            search_time = float(sub('[^0-9]+', '', search_time))

        if search_time < 7:
            print("Timing is too early, no canteens are open yet.")

        elif search_time > 21:
            print("Timing is too late, no canteens are still open.")

        elif 7 <= search_time <= 21:
            print("All of the canteens are open.")

    except ValueError:
        print("Please enter a valid number")
        check_hours()


def print_capacity():
    # get values from csv file
    pass


def menu():
    print("Please select an option:")
    print("Click on the map to find the closest canteen to a location, or")
    print("1 - Look for food cheaper than a set price")
    print("2 - Search for food which meets your dietary requirements")
    print("3 - More options")
    print("4 - Print all the stalls within a canteen")
    print("0 - Exit")

    _price_food = 1
    _check_requirements = 2
    _more_options = 3
    _print_stalls = 4
    _check_hours = 5
    _print_capacity = 6
    _less_options = 7
    _exit = 0
    _WAIT_VALUE = 1.2

    try:
        choice = int(input())

        if choice == _price_food:
            price_food()
            time.sleep(_WAIT_VALUE)

        elif choice == _check_requirements:
            check_requirements()
            time.sleep(_WAIT_VALUE)

        elif choice == _exit:
            print("Thank you for using our program!\n"
                  "-Alex,name1,name2,name3")
            exit(0)

        elif choice == _more_options:
            print('\n\n\n\n\n\n\n\n------------------------------------------------------------------\n')
            print("5 - Check if a store will be open at a certain time")
            print("6 - Print the capacities of the canteens")
            print("7 - Less options")
            print("0 - Exit")

            choice = int(input())

            if choice == _print_stalls:
                print_stalls()
                time.sleep(_WAIT_VALUE)

            elif choice == _check_hours:
                check_hours()
                time.sleep(_WAIT_VALUE)

            elif choice == _print_capacity:
                print_capacity()
                time.sleep(_WAIT_VALUE)

            elif choice == _less_options:
                menu()
            elif choice == _exit:
                print("Thank you for using our program!\n"
                      "-Alex,name1,name2,name3")
                exit(0)
            else:
                raise ValueError

        else:
            raise ValueError

    except ValueError:
        print("Enter a valid option")
        menu()

# ------------------------------------  FUNCTION DEFINITIONS ---------------------------------------------------------


data_set = pd.read_csv(r'C:\Users\User1\Desktop\alex mini project\NTU map_dataset.csv')


# initialising display
pygame.init()
display_surface = pygame.display.set_mode((x_size, y_size), 0, 32)
pygame.display.set_caption("Map of NTU")
background = pygame.image.load(r"C:\Users\User1\Desktop\alex mini project\map.png").convert()
running = True

while running:
    menu()
    display_surface.blit(background, (0, 0))
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            x1, y1 = pygame.mouse.get_pos()
            display_surface.blit(background, (0, 0))
            x,y = pygame.mouse.get_pos()
            pygame.display.update()

            #FIND DISTANCE
            distance_list = []
            for i in range(len(data_set)):
                distance_list.append(np.abs(int(data_set['x'][i]) - x1) + np.abs(int(data_set['y'][i] - y1)))

            # data in database is aligned in a table format with rows and columns
            df = pd.DataFrame(data_set)
            df['Distance'] = distance_list
            # sorting by distances in ascending order
            df.sort_values(by=['Distance'], inplace=True, ascending=True)

            # select the nearest canteen by position based off 'Distance' value
            closest_canteen = df.iloc[0, 0]
            print(closest_canteen)
            print(sorted(distance_list))
            print("The nearest canteen is", (closest_canteen), "which is", min(distance_list), "units away.")


pygame.quit()
exit()
