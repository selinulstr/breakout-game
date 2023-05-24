from turtle import Turtle

DIST = 10


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.x_dist = DIST
        self.y_dist = DIST
        self.reset()

    def reset(self):
        self.goto(0, -330)
        self.y_dist = DIST

    def move(self):
        new_y = self.ycor() + self.y_dist
        new_x = self.xcor() + self.x_dist
        self.goto(new_x, new_y)

    def bounce(self, x_bounce, y_bounce):
        if x_bounce:
            self.x_dist *= -1
        if y_bounce:
            self.y_dist *= -1