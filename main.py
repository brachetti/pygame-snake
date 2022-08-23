from mimetypes import init
import sys
import pygame

FRAMERATE = 60
CELL_SIZE = 40
CELL_NUMBER = 20

class Fruit:
    def __init__(self) -> None:
        # create an x and y position
        self.x = 5
        self.y = 4
        # draw a square
        pass

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
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
