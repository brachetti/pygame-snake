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
        self.ate_fruit = False
    
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
        
        if self.ate_fruit:
            body = self.body[:]
            self.ate_fruit = False
        else:
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
            fruit.reposition()
            self.ate_fruit = True

    def is_outside(self):
        head = self.body[0]
        return head.x <= 0 or head.x == CELL_NUMBER or head.y <= 0 or head.y == CELL_NUMBER

    def hits_itself(self):
        head = self.body[0]
        body = self.body[1:]
        return head in body

class Fruit:
    color = (126, 166, 114)

    def __init__(self) -> None:
        self.reposition()
    
    def draw(self):
        block = Block(self.position, Fruit.color)
        block.draw_block()

    def reposition(self):
        self.position = Vector2(
            random.randint(0, CELL_NUMBER - 1), 
            random.randint(0, CELL_NUMBER - 1)
        )

class Main:
    def __init__(self) -> None:
        self.snake = Snake()
        self.fruit = Fruit()
        self.game_over = False

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
        
        if self.snake.is_outside():
            self.game_over = True

        if self.snake.hits_itself():
            self.game_over = True


pygame.init()
screen = pygame.display.set_mode((CELL_SIZE*CELL_NUMBER, CELL_SIZE*CELL_NUMBER))
clock = pygame.time.Clock()
SCREEN_UPDATE = pygame.USEREVENT
pygame.time.set_timer(SCREEN_UPDATE, 150)

main_game = Main()

while True:
    if main_game.game_over:
        pygame.quit()
        sys.exit()

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
