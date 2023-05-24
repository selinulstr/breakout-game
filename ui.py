import time
from turtle import Turtle
import random

FONT = ("Courier", 52, "normal")
FONT2 = ("Courier", 32, "normal")
ALIGNMENT = "center"
COLOR = "white"
COLOR_LIST = ["firebrick", "lawn green",
              "dark slate blue", "medium blue",
              "turquoise", "deep sky blue",
              "medium violet red", "salmon", "tomato",
              "sandy brown", "purple", "deep pink",
              "medium sea green", "burlywood"]


class UI(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def header(self):
        self.clear()
        self.goto(x=0, y=-150)
        self.write("Breakout", align=ALIGNMENT, font=FONT)

    def change_color(self):
        self.clear()
        self.color(random.choice(COLOR_LIST))
        self.header()

    def paused_status(self):
        self.clear()
        self.change_color()
        time.sleep(0.5)

    def game_over(self, win):
        self.clear()
        if win:
            self.write("You Cleared the Game", align="center", font=FONT)
        else:
            self.write("Game is Over", align="center", font=FONT)