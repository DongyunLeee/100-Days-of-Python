# Pong Game Player Paddle Control
from turtle import Turtle


class User(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)
        self.position = position
        self.move_y = 50

    def reset(self):
        self.goto(self.position)

    def user_up(self):
        new_y = self.ycor() + self.move_y
        self.goto(self.xcor(), new_y)

    def user_down(self):
        new_y = self.ycor() - self.move_y
        self.goto(self.xcor(), new_y)

