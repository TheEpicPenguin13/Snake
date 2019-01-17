from turtle import Turtle
from random import randint

#-- Fruit Class --#
class Fruit(Turtle):

    #-- Constructor --#
    def __init__(self):
        Turtle.__init__(self)

        self.TILESX = int(1088 / 32)
        self.TILESY = int(736 / 32)

        self.startX = -16 # These are used to orient the fruit.
        self.startY = 0   # These are used in all of the position oriented classes.

        self.x, self.y = self.get_specific_num(32)

        self.shape("square")
        self.color("red")
        self.pu()
        self.speed(0)
        self.shapesize(32 / 22)
        self.goto(self.startX + (self.x * 32), self.startY + (self.y * 32))

    #-- Main Functions --#
    def move(self, array):
        for i in array:
            if i.pos() == self.pos():
                self.x, self.y = self.get_specific_num(32)
                self.goto(self.startX + (self.x * 32), self.startY + (self.y * 32))

    #-- Helper Functions --#
    def get_specific_num(self, range):                                     # Basically gets a random number
        num1 = randint(int(-self.TILESX / 2), 5)                           # if that number is a multiple of
        num2 = randint(int(-self.TILESY / 2), int(self.TILESY / 2))        # 32

        while num1 % range != 0 and num2 % range != 0:
            num1 = randint(int(-self.TILESX / 2), 5)
            num2 = randint(int(-self.TILESY / 2), int(self.TILESY / 2))

        return num1, num2
