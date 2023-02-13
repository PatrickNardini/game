# Write your code here :-)
from random import randint

potat = Actor("potat")

angotat = Actor("angotat")

def draw():
    screen.clear()
    potat.draw()
    angotat.draw()

def place_potat():
    potat.x = randint(10, 600)
    potat.y = randint(10, 600)

def place_angotat():
    angotat.x = randint(10, 600)
    angotat.y = randint(100, 600)

def on_mouse_down(pos):
    if potat.collidepoint(pos):
        print("Good shot!")
        place_potat()
        place_potat()
        place_angotat()
    else:
        print("You missed!")
        quit()

place_potat()
