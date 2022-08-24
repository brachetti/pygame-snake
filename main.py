from mimetypes import init
import sys
import pygame
from pygame.math import Vector2
import random

FRAMERATE = 60
CELL_SIZE = 40
CELL_NUMBER = 20

class Fruit:
    def __init__(self) -> None:
        # create an x and y position
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.position = Vector2(self.x, self.y)
        # draw a square
    
    def draw_fruit(self):
        # create a rectangle
        fruit_rect = pygame.Rect(
            self.position.x * CELL_SIZE, 
            self.position.y * CELL_SIZE, 
            CELL_SIZE, 
            CELL_SIZE
        )
        # draw it
        pygame.draw.rect(screen, (126, 166, 114), fruit_rect)

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()
screen.fill((175,215,70))

fruit = Fruit()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw all our elements
    fruit.draw_fruit()
    pygame.display.update()
    clock.tick(FRAMERATE)
