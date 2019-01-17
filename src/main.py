from turtle import Screen, Turtle
from snake import Snake
from fruit import Fruit
from snakebody import SnakeBody
from gui import Background, Text
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
score = 0
high_score = 0

#-- Instances --#
snake = Snake()
fruit = Fruit()

#-- Main Functions --#
def check_snake_wall_collision():
    if snake.x >= 6 or snake.xcor() <= -WIDTH / 2:
        snake.die(snakes)
        get_highscore()
    elif snake.ycor() >= HEIGHT / 2 or snake.ycor() <= -HEIGHT / 2:
        snake.die(snakes)
        get_highscore()

def get_highscore():
    global high_score, score
    if high_score < score:
        high_score = score
    score = 0

def snake_move():
    snakes[-1].x, snakes[-1].y = snake.prevX, snake.prevY
    snakes[-1].update(snakes[-1].x, snakes[-1].y)
    temp = []
    temp.append(snakes[-1])
    snakes.pop(-1)
    snakes.insert(1, temp[0])

def write_score(text, text2):
    s = Text("#1a1a1a")
    s.set_pos((WIDTH / 2 - 5 * 32) / 2, 300)
    s.write_text(text)
    s.set_pos((WIDTH / 2 - 5 * 32) / 2, 200)
    s.write_text(text2)
    s.clear()

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
    #drawGrid()
    Background(WIDTH, HEIGHT)
    snakes.append(snake)

def update():
    global score
    wn.update()
    snake.update()
    check_snake_wall_collision()
    write_score("Score: " + str(score), "High Score: " + str(high_score))

    if fruit.pos() == snake.pos():
        fruit.move(snakes)
        snakes.append(SnakeBody(snake.prevX, snake.prevY))

    if len(snakes) > 1:
        score = len(snakes) - 1
        snake_move()
        for i in snakes:
            if snake.pos() == i.pos():
                if i != snake:
                    snake.die(snakes)
                    get_highscore()
    sleep(0.2)

#-- Key Input --#
wn.listen()
wn.onkey(snake.up, "w")
wn.onkey(snake.l, "a")
wn.onkey(snake.down, "s")
wn.onkey(snake.r, "d")

wn.onkey(snake.up, "Up")
wn.onkey(snake.l, "Left")
wn.onkey(snake.down, "Down")
wn.onkey(snake.r, "Right")

#-- Main Loop  --#
load()
while True:
    update()
