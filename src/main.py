from turtle import Screen, Turtle
from snake import Snake
from fruit import Fruit
from time import sleep

#-- Constant Vars --#
WIDTH = 1088
HEIGHT = 736
TILESX = int(WIDTH / 2)
TILESY = int(HEIGHT / 2)

EMPTY = 0
SNAKE_HEAD = 1

#-- Vars --#
grid = []

#-- Setup Screen --#
wn = Screen()
wn.title("Snake")
wn.setup(WIDTH, HEIGHT)
wn.bgcolor("black")
wn.tracer(0)

#-- Instances --#
snake = Snake()
fruit = Fruit()

#-- Helper Functions --#
def initializeGrid():
    for y in range(TILESY):
        grid.append([])
        for x in range(TILESX):
            grid.append(EMPTY)

#- Debug -#
def drawGrid():
    t = Turtle(); t.ht(); t.speed(0); t.pu();
    t.goto(-WIDTH / 2, -HEIGHT / 2); t.color("cyan"); t.pd()

    for y in range(int(-HEIGHT / 2), int(HEIGHT / 2), 32):
        for x in range(int(-WIDTH / 2), int(WIDTH / 2), 32):
            for i in range(4):
                t.pd()
                drawSquare(t, 32)
                t.pu()
            t.goto(x, y)

def drawSquare(t, width):
    t.fd(width); t.left(90)

#-- Load / Update --#
def load():
    initializeGrid()
    drawGrid()

def update():
    wn.update()
    snake.update(fruit)
    sleep(0.2)

#-- Key Input --#
wn.listen()
wn.onkey(snake.up, "w")
wn.onkey(snake.left, "a")
wn.onkey(snake.down, "s")
wn.onkey(snake.right, "d")

#-- Main Loop  --#
load()
while True:
    update()
