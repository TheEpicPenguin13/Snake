from turtle import Screen, Turtle

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

#-- Helper Functions --#
def initializeGrid():
    for y in range(TILESY):
        grid.append([])
        for x in range(TILESX):
            grid.append(EMPTY)

#-- Load / Update --#
def load():
    initializeGrid()

def update():
    pass

#-- Main Loop  --#
load()
wn.mainloop()
