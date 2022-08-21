import sys
import pygame

FRAMERATE = 60

pygame.init()
screen = pygame.display.set_mode((400, 500))
clock = pygame.time.Clock()
screen.fill((175,215,70))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw all our elements
    pygame.display.update()
    clock.tick(FRAMERATE)
