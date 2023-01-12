from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        # self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("yellow")
        self.speed("fastest")
        self.penup()
        self.create_food()

    def create_food(self):
        new_x = random.randrange(-260, 260, 20)
        new_y = random.randrange(-260, 260, 20)
        self.goto(new_x, new_y)
