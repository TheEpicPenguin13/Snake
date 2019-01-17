from turtle import Turtle

#-- Main GUI Class --#
class GUI(Turtle):

    def __init__(self):
        Turtle.__init__(self)
        self.speed(0)
        self.ht()
        self.pu()

#-- Background GUI Subclass --#
class Background(GUI):

    def __init__(self, screenWidth, screenHeight):
        GUI.__init__(self)

        self.screenWidth = screenWidth
        self.screenHeight = screenHeight

        self.extraTiles = 5

        self.color("#997300")
        self.pensize(4)
        self.goto(self.extraTiles * 32, screenHeight / 2)

        self.pd()
        self.draw_background()
        self.pu()

    # Draws a giant rectangle as a background.
    def draw_background(self):
        self.fillcolor("#cc9900")
        self.begin_fill()
        for i in range(2):
            self.forward((self.screenWidth / 2 - self.extraTiles * 32))
            self.right(90)
            self.forward(self.screenHeight)
            self.right(90)
        self.end_fill()

#-- Text GUI Subclass --#
class Text(GUI):

    def __init__(self, color):
        GUI.__init__(self)

        self.color(color)

    def set_pos(self, x, y):
        self.goto(x, y)

    def write_text(self, text):
        self.write(text, font=("Arial", 24, "normal"))
