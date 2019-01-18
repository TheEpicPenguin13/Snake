from turtle import Turtle

#-- Snake Class --#
class Snake(Turtle):

    #-- Constructor --#
    def __init__(self):
        Turtle.__init__(self)

        self.startX = -16
        self.startY = 0

        self.width = 1088
        self.height = 736

        self.x = 0
        self.prevX = self.x
        self.y = 0
        self.prevY = self.y
        self.direction = 0

        self.shape("square")
        self.color("green")
        self.shapesize(32 / 22)
        self.pu()
        self.goto(self.startX, self.startY)


    #-- Helper Function --#
    def get_positionX(self): return self.startX + (self.x * 32)
    def get_positionY(self): return self.startY + (self.y * 32)

    #-- Input Functions --#
    def r(self): self.direction = 0
    def down(self): self.direction = 1
    def l(self): self.direction = 2
    def up(self): self.direction = 3

    #-- Update --#
    def update(self):
        self.prevX, self.prevY = self.x, self.y

        if self.direction == 0:   # 0 = Right
            self.x += 1
        elif self.direction == 1: # 1 = Down
            self.y -= 1
        elif self.direction == 2: # 2 = Left
            self.x -= 1
        else:                     # 3 = Up
            self.y += 1

        self.goto(self.get_positionX(), self.get_positionY())

    #-- Main Functions --#
    def die(self, snakes):
        for i in range(len(snakes) - 1):                   # When you die, the
                snakes[1].goto(-100000, -110000)           # SnakeBody parts go into space and
                snakes.pop(1)                              # gets removed from the snake array.
        self.x, self.y = 0, 0
        self.goto(self.get_positionX(), self.startY)
