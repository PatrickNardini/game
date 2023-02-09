import pygame, sys
import os
import random
pygame.mixer.init()
pygame.init()

class Crosshair(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(os.path.join("files", 'crosshair.png'))
        self.rect = self.image.get_rect()
        self.shot_sound = pygame.mixer.Sound(os.path.join('files','shot.wav'))
    def sound(self):
        self.shot_sound.play()
        pygame.sprite.spritecollide(crosshair,target_group, True)

    def update(self):
        self.rect.center = pygame.mouse.get_pos()


class Target(pygame.sprite.Sprite):
    def __init__(self, target ,x,y):
        super().__init__()
        self.image = pygame.image.load(target)
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]



# Screeen
width, height = 1000,700
screen = pygame.display.set_mode((width,height))
clock = pygame.time.Clock()

bg = pygame.transform.scale2x(pygame.transform.scale2x(pygame.image.load(os.path.join('files','bg.png'))))
pygame.display.set_caption("Shotting Game")
pygame.mouse.set_visible(False)


# crosshair
crosshair = Crosshair()
crosshair_group = pygame.sprite.Group()
crosshair_group.add(crosshair)

# Target
target_group = pygame.sprite.Group()
for target in range(20):
    draw_target = Target(os.path.join('files','target.png'),random.randint(0,width), random.randint(0,height))
    target_group.add(draw_target)

# Main loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            crosshair.sound()

    screen.fill((255,255,255))
    screen.blit(bg,(0,0))
    target_group.draw(screen)
    crosshair_group.draw(screen)
    crosshair_group.update()

    pygame.display.update()
    clock.tick(50)
