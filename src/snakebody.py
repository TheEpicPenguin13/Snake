from turtle import Turtle

#-- SnakeBody Class --#
class SnakeBody(Turtle):

    #-- Constructor --#
    def __init__(self, x, y):
        Turtle.__init__(self)

        self.startX = -16
        self.startY = 0

        self.x = x
        self.y = y

        self.pu()
        self.shape("square")
        self.speed(0)
        self.shapesize(32 / 22)
        self.color("#09c119")

    def update(self, x, y):
        self.goto(self.startX + (x * 32), self.startY + (y * 32))
