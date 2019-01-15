from turtle import Turtle

#-- SnakeBody Class --#
class SnakeBody(Turtle):

    #-- Constructor --#
    def __init__(self):
        Turtle.__init__(self)

        self.startX = -16
        self.startY = 0

        self.pu()
        self.shape("square")
        self.speed(0)
        self.shapesize(32 / 22)
        self.color("#33cc33")

    def set_position(snakePrevX, snakePrevY):
        self.goto(self.startX + (snakePrevX * 32), self.startY + (snakePrevY * 32))
