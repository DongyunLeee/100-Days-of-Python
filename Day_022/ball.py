# Pong Game Ball Control
from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super(Ball, self).__init__()
        self.color("white")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.goto(0, 0)
        self.x = 10
        self.y = 10

    def reset(self):
        self.goto(0, 0)
        self.touch_user()

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def touch_wall(self):
        self.y = -self.y

    def touch_user(self):
        self.x = -self.x