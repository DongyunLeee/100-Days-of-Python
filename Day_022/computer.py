from turtle import Turtle


class Computer(Turtle):
    def __init__(self):
        super().__init__()
        # self.speed(2)
        self.goto(280, 0)
        self.shape("square")
        self.shapesize(1, 3, 1)
        self.setheading(90)
        self.penup()
        self.color("white")

    def com_play(self):
        self.forward(20)

    def touch_wall(self):
        self.right(180)