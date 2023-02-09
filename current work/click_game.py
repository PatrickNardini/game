import pygame
import time
from random import randint

pygame.init()
pygame.mouse.set_visible(False)
display = pygame.display.set_mode((500, 500))
FPS = 60
clock = pygame.time.Clock()

def graphics():
    display.fill((0,0,0))

def main():
    x = 0
    y = 0
    while True:
        (x,y) = pygame.mouse.get_pos()
        print(x)
        print(y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pass
            if event.type ==pygame.KEYDOWN:
                if event.key == pygame.K_a
                    print("a")
        graphics()

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
