from mimetypes import init
import sys
import pygame
from pygame.math import Vector2
import random

FRAMERATE = 60
CELL_SIZE = 40
CELL_NUMBER = 20

class Block:
    def __init__(self, position, color) -> None:
        self.position = position
        self.color = color

    def __rect(self):
        return pygame.Rect(
            self.position.x * CELL_SIZE, 
            self.position.y * CELL_SIZE, 
            CELL_SIZE, 
            CELL_SIZE
        )

    def draw_block(self):
        pygame.draw.rect(screen, self.color, self.__rect())

class Snake:
    def __init__(self) -> None:
        self.body = [
            Vector2(5, 10),
            Vector2(6, 10),
            Vector2(7, 10),
        ]
        self.blocks = [
            Block(position, (255, 0, 0))
            for position in self.body
        ]
    
    def draw(self):
        for block in self.blocks:
            block.draw_block()

class Fruit:
    def __init__(self) -> None:
        position = Vector2(
            random.randint(0, CELL_NUMBER - 1), 
            random.randint(0, CELL_NUMBER - 1)
        )
        self.block = Block(position, (126, 166, 114))
    
    def draw(self):
        self.block.draw_block()

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()
screen.fill((175,215,70))

fruit = Fruit()
snake = Snake()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw all our elements
    fruit.draw()
    snake.draw()
    
    pygame.display.update()
    clock.tick(FRAMERATE)
