from turtle import Turtle
from random import randint

#-- Fruit Class --#
class Fruit(Turtle):

    #-- Constructor --#
    def __init__(self, snake):
        Turtle.__init__(self)

        self.snake = snake

        self.TILESX = int(1088 / 32)
        self.TILESY = int(736 / 32)

        self.startX = -16 # These are used to orient the fruit.
        self.startY = 0   # These are used in all of the position oriented classes.

        self.x, self.y = self.get_specific_num(32, self.snake)

        self.shape("square")
        self.color("red")
        self.pu()
        self.speed(0)
        self.shapesize(32 / 22)
        self.goto(self.startX + (self.x * 32), self.startY + (self.y * 32))

    def when_hit(self, angle):
        self.setheading(self.heading() + angle)

    #-- Main Functions --#
    def move(self, array):
        for i in array:
            if i.pos() == self.pos():
                self.x, self.y = self.get_specific_num(32, self.snake)
                self.goto(self.startX + (self.x * 32), self.startY + (self.y * 32))

    #-- Helper Functions --#
    def get_specific_num(self, range, snake):                              # Basically gets a random number
        num1 = randint(int(-self.TILESX / 2) + 1, 5)                       # if that number is a multiple of
        num2 = randint(int(-self.TILESY / 2), int(self.TILESY / 2))        # 32

        while (num1 % range != 0 and num2 % range != 0) and self.pos() == snake.pos():
            num1 = randint(int(-self.TILESX / 2) + 1, 5)
            num2 = randint(int(-self.TILESY / 2), int(self.TILESY / 2))

        return num1, num2
