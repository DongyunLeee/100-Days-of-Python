from turtle import Turtle, Screen

# W = forward
# S = backward
# A = counter-clockwise
# D = clockwise
# C = init

turtle = Turtle()
screen = Screen()

length = 10
angle = 30

def t_forward():
    turtle.forward(length)

def t_backward():
    turtle.back(length)

def t_turn():
    turtle.right(angle)

def t_backturn():
    turtle.left(angle)

def t_clear():
    turtle.reset()

screen.listen()
screen.onkey(key="w", fun=t_forward)
screen.onkey(key="s", fun=t_backward)
screen.onkey(key="a", fun=t_backturn)
screen.onkey(key="d", fun=t_turn)
screen.onkey(key="c", fun=t_clear)
screen.exitonclick()