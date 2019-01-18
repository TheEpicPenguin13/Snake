"""
Snake (clone), by John McAllister

If you've played snake, than you know exactly how to play this, and that's great!
For those who haven't played snake, it is quite simple. You are a snake, (the
green thing moving on your screen). Your goal is to eat the red dot to get longer.
Just don't hit the wall, or yourself and you should do fine!

Now your probably wondering, "How do I move my snake?". The answer to this is
simple. You do this by either using the arrow keys or WASD. Whatever you are used
to using.

W, UpArrow = Up
A, LeftArrow = Left
S, DownArrow = Down
D, RightArrow = Right
Escape, Quit

Check List:
Title: Done
Name: Done
Description: Done
Directions: Done
Question Input: ?
Variables: Doneww
Two Functions: Done
Use Of List: Done
Strings: Done
Console Output: Done
Operators: Done
Conditionals: Done
Loops: Done
Comparative Operators: Done
Score/Custom Message: Done
Commemts: Done
Give Credit: My Own Code So Done
Testing: Working on it
Ask Peers To Test: Working on it
"""

print(
"""
Snake (clone), by John McAllister

If you've played snake, than you know exactly how to play this, and thats great!
For those who haven't played snake, it is quite simple. You are a snake, (the
green thing moving on your screen) Your goal is to eat the red dot to get longer.
Just don't hit the wall, or yourself and you should do fine!

Now your probably wondering, "How do I move my snake?". The answer to this is
simple. You do this by either using the arrow keys or WASD. Whatever you are used
to using.

W, UpArrow = Up
A, LeftArrow = Left
S, DownArrow = Down
D, RightArrow = Right
Escape, Quit
"""
)

from turtle import Screen
from snake import Snake
from fruit import Fruit
from snakebody import SnakeBody
from gui import Background, Text
from time import sleep

#-- Constant Vars --#
WIDTH = 1088 # The Width of the screen.
HEIGHT = 736 # The Height of the screen.

#-- Setup Screen --#
wn = Screen()           # This whole chunk of code basically creates a Screen
wn.title("Snake")       # object and gives it a title ("Snake"), a width and
wn.setup(WIDTH, HEIGHT) # height of WIDTH and HEIGHT, sets the background color
wn.bgcolor("black")     # to black, and sets the update speed to 0 (Becomes
wn.tracer(0)            # useful later)

#-- Vars ==#
snakes = []
score = 0
local_high_score = 0
global_high_score = 0

running = True

#-- Instances --#
snake = Snake()
fruit = Fruit(snake)

#-- Main Functions --#
def check_snake_wall_collision():
    if snake.x >= 6 or snake.xcor() <= -WIDTH / 2: # This checks whether the snake has reached certain points and if so,
        snake.die(snakes)               # kills the snake, it checks the x and y position of the snake, and afterwards
        get_highscore()                 # updates score.
    elif snake.ycor() >= HEIGHT / 2 or snake.ycor() <= -HEIGHT / 2:
        snake.die(snakes)
        get_highscore()

def get_highscore():
    global global_high_score, local_high_score, score
    if local_high_score < score:
        local_high_score = score
    if global_high_score < local_high_score:
        global_high_score = local_high_score
    score = 0

def leave():
    global running
    set_global()
    running = False

def get_global():
    global global_high_score
    f = open("global_score.txt", "r")
    global_high_score = int(f.read())
    f.close()

def set_global():
    global global_high_score
    f = open("global_score.txt", "w")
    f.write(str(global_high_score))
    f.close()

def remove_global():
    global global_high_score
    global_high_score = 0
    f = open("global_score.txt", "w")
    f.write("0")
    f.close()

def snake_move():
    snakes[-1].x, snakes[-1].y = snake.prevX, snake.prevY
    snakes[-1].update(snakes[-1].x, snakes[-1].y)
    temp = []                    # This is the bit of code that moves the snake.
    temp.append(snakes[-1])      # The idea, is that it gets the snakeBody at
    snakes.pop(-1)               # the end of the snake, and puts it at the front.
    snakes.insert(1, temp[0])    # This makes it look like the snake is moving.

def write_score(text, text2, text3):
    s = Text("#1a1a1a")
    s.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 300)
    s.write_text(text)
    s.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 200)
    s.write_text(text2)
    s.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 100)
    s.write_text(text3)
    s.clear()

#-- Load / Update --#
def load():
    get_global()
    Background(WIDTH, HEIGHT)
    snakes.append(snake)

def update():
    global score                                                               # This whole update method is the meat of this program.
    wn.update()                                                                # It updates the window, updates the snake, and then does
    snake.update()                                                             # the collision checking. It writes the score, and runs most
    check_snake_wall_collision()                                               # of the methods from other classes.
    write_score("Score: " + str(score), "High Score: " + str(local_high_score), "Global High Score: " + str(global_high_score))

    if fruit.pos() == snake.pos():
        snakes.append(SnakeBody(snake.prevX, snake.prevY))

    if len(snakes) > 1:
        score = (len(snakes) - 1) * 100
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
wn.onkey(remove_global, "m")

wn.onkey(snake.up, "Up")
wn.onkey(snake.l, "Left")
wn.onkey(snake.down, "Down")
wn.onkey(snake.r, "Right")
wn.onkey(leave, "Escape")

#-- Main Loop  --#
load()
while running:
    update()
