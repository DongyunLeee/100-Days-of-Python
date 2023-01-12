# Pong Game Boundary Line
from turtle import Turtle


class Game_fild(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("red")
        self.pensize(5)
        self.penup()
        self.goto(0, -280)
        self.setheading(90)
        self.drow_fild()

    def drow_fild(self):
        x = -280
        while x < 260:
            x += 20
            self.pendown()
            self.forward(10)
            self.penup()
            self.forward(10)

