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

from turtle import *
from snake import Snake
from fruit import Fruit
from snakebody import SnakeBody
from gui import Background, Text, Button
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
hasStarted = False

#-- Instances --#
snake = Snake()
fruit = Fruit(snakes)

Background(WIDTH, HEIGHT)

s = Text("#1a1a1a")
a = Text("#1a1a1a")
d = Text("#1a1a1a")
text = Text("#1a1a1a")
q = Text("#1a1a1a")

quit_button = Button(270, 80, 150, 75, "#634a25")

#-- Main Functions --#
def check_snake_wall_collision():
    if snake.x >= 11 or snake.xcor() <= -WIDTH / 2: # This checks whether the snake has reached certain points and if so,
        snake.die(snakes)               # kills the snake, it checks the x and y position of the snake, and afterwards
        get_highscore()                 # updates score.
        clear([s, a, d])
        write_score("Score: " + str(score), "High Score: " + str(local_high_score),
                    "Global High Score: " + str(global_high_score))
    elif snake.ycor() >= HEIGHT / 2 or snake.ycor() <= -HEIGHT / 2:
        snake.die(snakes)
        get_highscore()
        clear([s, a, d])
        write_score("Score: " + str(score), "High Score: " + str(local_high_score),
                    "Global High Score: " + str(global_high_score))

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
    f = open("data/global_score.txt", "r")
    global_high_score = int(f.read())
    f.close()

def set_global():
    global global_high_score
    f = open("data/global_score.txt", "w")
    f.write(str(global_high_score))
    f.close()

def remove_global():
    global global_high_score
    global_high_score = 0
    f = open("data/global_score.txt", "w")
    f.write("0")
    clear([s, a, d])
    write_score("Score: " + str(score), "High Score: " + str(local_high_score),
                "Global High Score: " + str(global_high_score))
    f.close()

def snake_move():
    snakes[-1].x, snakes[-1].y = snake.prevX, snake.prevY
    snakes[-1].update(snakes[-1].x, snakes[-1].y)
    temp = []                    # This is the bit of code that moves the snake.
    temp.append(snakes[-1])      # The idea, is that it gets the snakeBody at
    snakes.pop(-1)               # the end of the snake, and puts it at the front.
    snakes.insert(1, temp[0])    # This makes it look like the snake is moving.

def write_score(text1, text2, text3):
    s.clear()
    s.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 300)
    s.write_text(text1)
    a.clear()
    a.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 200)
    a.write_text(text2)
    d.clear()
    d.set_pos((WIDTH / 2 - 5 * 32 - 40) / 2, 100)
    d.write_text(text3)

def write_instructions():
    text.set_pos((WIDTH / 2 - 5 * 32 + 150) / 2, -50)
    text.write_text("- How To Play -")
    text.set_pos((WIDTH / 2 - 5 * 32 + 130) / 2, -120)
    text.write_text("W, UpArrow - Up")
    text.set_pos((WIDTH / 2 - 5 * 32 + 110) / 2, -170)
    text.write_text("A, LeftArrow - Left")
    text.set_pos((WIDTH / 2 - 5 * 32 + 60) / 2, -220)
    text.write_text("S, DownArrow - Down")
    text.set_pos((WIDTH / 2 - 5 * 32 + 65) / 2, -270)
    text.write_text("D, RightArrow - Right")

#-- Load / Update --#
def load():
    global q, quit_button
    get_global()
    snakes.append(snake)
    clear([s, a, d])
    write_score("Score: " + str(score), "High Score: " + str(local_high_score),
                "Global High Score: " + str(global_high_score))
    write_instructions()
    q.set_pos(quit_button.centerX - 50, quit_button.centerY - 24)
    q.write("Quit", font=("Arial", 48, "normal"))

def clear(obj):
    for i in obj:
        i.clear()

def update():
    global score, global_high_score, snakes, start_button
    global s, a, d                                                             # This whole update method is the meat of this program.
    wn.update()                                                                # It updates the window, updates the snake, and then does
    snake.update()                                                             # the collision checking. It writes the score, and runs most
    check_snake_wall_collision()                                               # of the methods from other classes.

    if quit_button.pressed == True:
        leave()

    if fruit.pos() == snake.pos():
        fruit.move(snakes)
        snakes.append(SnakeBody(snake.prevX, snake.prevY))
        clear([s, a, d])
        write_score("Score: " + str((len(snakes) - 1) * 100), "High Score: " + str(local_high_score),
                    "Global High Score: " + str(global_high_score))

    score = (len(snakes) - 1) * 100
    if len(snakes) > 1:
        snake_move()
        for i in snakes:
            if snake.pos() == i.pos():
                if i != snake:
                    snake.die(snakes)
                    get_highscore()
                    clear([s, a, d])
                    write_score("Score: " + str(score), "High Score: " + str(local_high_score),
                                "Global High Score: " + str(global_high_score))
            if fruit.pos() == i.pos():
                fruit.move(snakes)

    sleep(0.125)

wn.listen()

#-- Mouse Input --#
onscreenclick(quit_button.is_pressed)

#-- Key Input --#
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
