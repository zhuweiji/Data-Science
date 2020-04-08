import turtle
import time
import random
from pygame import mixer  # Load the popular external library

screen = turtle.Screen()
screen.screensize(400, 400)
pointer = turtle.Turtle()
pointer.shapesize(10)
pointer.up()
pointer.speed(100)
pointer.setpos(15, 300)
pointer.setheading(270)

wheel_state = 0
wheel_path = "wheels/{}.gif".format(wheel_state)
screen.register_shape(wheel_path)
screen.bgpic(wheel_path)
screen.update()


def show_wheel():
    pass

def choose_letter():
    pass

def spin_wheel():
    """ make sure users cant spin more than once """
    SPIN_SPEED = 0.02
    global wheel_state
    print('spinning wheel')
    spin_strength = random.randint(50, 150)

    while spin_strength:
        wheel_path = "wheels/{}.gif".format(wheel_state)
        print(wheel_path)
        screen.bgpic(wheel_path)

        if spin_strength <4:
            time.sleep(SPIN_SPEED * 8)
            print('3')
        elif spin_strength < 10:
            print('2')
            time.sleep(SPIN_SPEED * 6)
        elif spin_strength < 40:
            time.sleep(SPIN_SPEED * 4)

        else:
            time.sleep(SPIN_SPEED)
        screen.update()

        wheel_state += 1
        spin_strength -= 1
        if wheel_state == 24:
            wheel_state = 0


while True:
    screen.onkeypress(spin_wheel, "Up")
    screen.listen()
    turtle.done()



