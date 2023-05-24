from turtle import Turtle

DIST = 70


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.goto(x=0, y=-380)

    def move_left(self):
        self.backward(DIST)

    def move_right(self):
        self.forward(DIST)
