from turtle import Turtle

#-- Main GUI Class --#
class GUI(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.ht()
        self.pu()

class Background(GUI):

    def __init__(self, screenWidth, screenHeight):
        GUI.__init__(self)

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.color("#cc9900")
        self.goto(-screenWidth / 2, screenHeight / 2)

        self.pd()
        self.draw_background()
        self.pu()

    def draw_background(self):
        self.begin_fill()
        for i in range(2):
            self.forward((self.screenWidth + 300))
            self.right(90)
            self.forward(self.screenHeight / 2)
            self.right(90)
        self.end_fill()

