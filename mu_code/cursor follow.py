import pygame
import time
from random import randint

pygame.init()
pygame.mouse.set_visible(False)
display = pygame.display.set_mode((500, 500))
FPS = 60
clock = pygame.time.Clock()

def doit():
    display.fill((255, 0, 0))
    pygame.display.update()
    time.sleep(1.0)

def graphics(x, y):
    display.fill((0, 0, 0))
    pygame.draw.rect(display, (255, 255, 255), [x + 6, y, 5, 2])
    pygame.draw.rect(display, (255, 255, 255), [x - 8, y, 5, 2])
    pygame.draw.rect(display, (255, 255, 255), [x , y + 6, 2, 5])
    pygame.draw.rect(display, (255, 255, 255), [x, y - 8, 2, 5])
    pygame.display.update()
    clock.tick(FPS)


def main():
    x = 0
    y = 0
    while True:
        (x, y) = pygame.mouse.get_pos()
        print(x)
        print(y)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                doit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    print("a")
        graphics(x, y)

main()
