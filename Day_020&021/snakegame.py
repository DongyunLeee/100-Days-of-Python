import time
import turtle
import random

screen = turtle.Screen()
screen.listen()
screen.tracer(0)
turtle.screensize(400, 400, "black")

segment = list()
route = list()
flag = 0


def set_snake():
    new_snake = turtle.Turtle(shape="square")
    # new_snake.shapesize(0.5, 0.5)
    new_snake.penup()
    new_snake.speed(2)
    new_snake.color("white")
    segment.append(new_snake)


def add_snake():
    global flag
    xy = segment[-1].pos()
    # move_snake()
    new_snake = turtle.Turtle(shape="square")
    # new_snake.shapesize(0.5, 0.5)
    new_snake.setpos(xy)
    route.insert(0, xy)
    new_snake.penup()
    new_snake.speed(2)
    new_snake.color("white")
    segment.append(new_snake)


def set_target():
    new_target = turtle.Turtle(shape="circle")
    new_target.shapesize(0.5, 0.5)
    new_target.penup()
    new_target.speed(10)
    x = random.randrange(-180, 180, 20)
    y = random.randrange(-180, 180, 20)
    new_target.setpos(x, y)
    new_target.color("yellow")
    return new_target


def change_target(tg):
    tg.setpos(random.randrange(-180, 180, 20), random.randrange(-180, 180, 20))


def move_snake():
    global flag
    if flag == 0:
        route.append((route[-1][0] + 20, route[-1][1]))
    elif flag == 1:
        route.append((route[-1][0], route[-1][1] + 20))
    elif flag == 2:
        route.append((route[-1][0] - 20, route[-1][1]))
    else:
        route.append((route[-1][0], route[-1][1] - 20))

    for num, snake in enumerate(reversed(segment)):
        snake.setpos(route[num])
        screen.update()
        time.sleep(0.1)

    route.pop(0)
    print(route)


def set_right():
    global flag
    flag = 0


def set_up():
    global flag
    flag = 1


def set_left():
    global flag
    flag = 2


def set_down():
    global flag
    flag = 3


def main():
    global flag
    game_is_on = True
    while game_is_on:
        move_snake()
        if segment[0].pos() == target.pos():
            add_snake()
            change_target(target)

        screen.onkey(set_right, "Right")
        screen.onkey(set_up, "Up")
        screen.onkey(set_left, "Left")
        screen.onkey(set_down, "Down")


set_snake()
route.append(segment[0].pos())
target = set_target()
print(segment[0].pos(), target.pos())
main()
screen.exitonclick()