from turtle import Screen, Turtle
from snake import Snake
from fruit import Fruit
from snakebody import SnakeBody
from time import sleep

#-- Constant Vars --#
WIDTH = 1088
HEIGHT = 736
TILESX = int(WIDTH / 2)
TILESY = int(HEIGHT / 2)

#-- Setup Screen --#
wn = Screen()
wn.title("Snake")
wn.setup(WIDTH, HEIGHT)
wn.bgcolor("black")
wn.tracer(0)

#-- Vars ==#
snakes = []

#-- Instances --#
snake = Snake()
fruit = Fruit()

#-- Main Functions --#
def check_snake_wall_collision():
    if snake.xcor() >= WIDTH / 2 or snake.xcor() <= -WIDTH / 2:
        snake.die()
    elif snake.ycor() >= HEIGHT / 2 or snake.ycor() <= -HEIGHT / 2:
        snake.die()

#- Debug -#
def drawGrid():
    t = Turtle(); t.ht(); t.speed(0); t.pu()
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
    drawGrid()
    snakes.append(snake)

def update():
    wn.update()
    snake.update()
    check_snake_wall_collision()
    snake.check_collision(fruit, snakes, SnakeBody(snake.prevX, snake.prevY))

    if len(snakes) > 1:
        snakes[-1].update(snake.prevX, snake.prevY)
        print(5)

    sleep(0.2)
    print(snakes)

#-- Key Input --#
wn.listen()
wn.onkey(snake.up, "w")
wn.onkey(snake.l, "a")
wn.onkey(snake.down, "s")
wn.onkey(snake.r, "d")

#-- Main Loop  --#
load()
while True:
    update()

