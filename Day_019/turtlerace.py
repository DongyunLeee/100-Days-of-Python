import random
from turtle import Turtle, Screen


is_race_on = False
turtle_color = ["red", "blue", "purple", "green", "orange", "black"]
turtle_list = list()

screen = Screen()
width, height = 500, 400
max = width/2-20
screen.setup(width=width, height=height)
user_bet = screen.textinput(title="Make your bet", prompt="please select winner color:")
print(f"user_bet: {user_bet}")

for num in range(6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_color[num])
    new_turtle.penup()
    x, y = 20-width/2, 100+(40*num)-(height/2)
    new_turtle.goto(x, y)
    turtle_list.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in turtle_list:
        rand_len = random.randint(0, 10)
        turtle.forward(rand_len)
        if turtle.xcor() > max:
            if user_bet == turtle.fillcolor():
                print(f"you win! {user_bet}")
            else:
                print(f"you lose! {turtle.fillcolor()}")
            is_race_on = False
            break


screen.exitonclick()