from ast import main
from cgi import print_form
from curses import KEY_DOWN, echo
from mimetypes import init
import sys
import pygame
from pygame.math import Vector2
import random

FRAMERATE = 60
CELL_SIZE = 40
CELL_NUMBER = 20

surface_bg = (175,215,70)

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
    color = (183, 111, 122)
    
    def __init__(self) -> None:
        self.body = [
            Vector2(5, 10),
            Vector2(6, 10),
            Vector2(7, 10),
        ]
        self.direction = "up"
    
    def blocks(self):
        return [
            Block(position, Snake.color)
            for position in self.body
        ]

    def draw(self):
        for block in self.blocks():
            block.draw_block()

    def move_snake(self):
        direction = Vector2(0,0)
        if self.direction == "up":
            direction = Vector2(0, -1)
        if self.direction == "down":
            direction = Vector2(0, 1)
        if self.direction == "left":
            direction = Vector2(-1, 0)
        if self.direction == "right":
            direction = Vector2(1, 0)
        
        body = self.body[:-1]
        body.insert(0, body[0] + direction)
        self.body = body[:]

    def change_direction(self, event):
        if event.key == pygame.K_UP and self.direction != "down":
            self.direction = "up"
        if event.key == pygame.K_DOWN and self.direction != "up":
            self.direction = "down"
        if event.key == pygame.K_LEFT and self.direction != "right":
            self.direction = "left"
        if event.key == pygame.K_RIGHT and self.direction != "left":
            self.direction = "right"

    def fruit_collission(self, fruit):
        if self.body[0] == fruit.position:
            print("worlds collide!")

class Fruit:
    color = (126, 166, 114)

    def __init__(self) -> None:
        self.position = Vector2(
            random.randint(0, CELL_NUMBER - 1), 
            random.randint(0, CELL_NUMBER - 1)
        )
        self.block = Block(self.position, Fruit.color)
    
    def draw(self):
        self.block.draw_block()

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()

    def update(self):
        self.snake.move_snake()
        self.check_collision()

    def draw(self):
        self.fruit.draw()
        self.snake.draw()

    def move_snake(self, event):
        self.snake.change_direction(event)

    def check_collision(self):
        self.snake.fruit_collission(self.fruit)

pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()      

        if event.type == SCREEN_UPDATE:
            main_game.update()

        if event.type == pygame.KEYDOWN:
            main_game.move_snake(event)

    # draw all our elements
    screen.fill(surface_bg)
    main_game.draw()
    
    pygame.display.update()
    clock.tick(FRAMERATE)
