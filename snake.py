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
        self.goto(self.startX, self.startY)
        self.pu()

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

        if self.direction == 0:
            self.x += 1
        elif self.direction == 1:
            self.y -= 1
        elif self.direction == 2:
            self.x -= 1
        else:
            self.y += 1

        self.goto(self.get_positionX(), self.get_positionY())

    #-- Main Functions --#
    def die(self):
        self.x, self.y = 0, 0
        self.goto(self.startX, self.startY)

    def check_collision(self, fruit, array, snakeBody):
        if fruit.pos() == self.pos():
            fruit.move()
            array.append(snakeBody)


