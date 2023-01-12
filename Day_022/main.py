# Pong Game with Python
# Using Turtle Library of Python
# 1P key - Up: "w", Down: "s"
# 2P key - Up: ↑, Down: ↓
# Who's winner? Get 5 points

import time
from turtle import Screen
from scoreboard import Scoreboard
from gamefild import Game_fild
from ball import Ball
from user import User

# Setting Game Screen
screen = Screen()
screen.title("Pong Game -> Made in DY")
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.tracer(0)

score = Scoreboard()
fild = Game_fild()
player_0 = User((350, 0))
player_1 = User((-350, 0))
ball = Ball()

# Setting Keys
screen.listen()
screen.onkey(player_0.user_up, "Up")
screen.onkey(player_0.user_down, "Down")
screen.onkey(player_1.user_up, "w")
screen.onkey(player_1.user_down, "s")

game_is_on = True  #Game Play Status
delay = 0.05  #Game Speed Value
while game_is_on:
    ball.move()
    time.sleep(delay)

    # When ball touch wall
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.touch_wall()

    # When player touch ball
    if (ball.distance(player_0) < 50 and ball.xcor() > 320) or (ball.distance(player_1) < 50 and ball.xcor() < -320):
        ball.touch_user()
        # Game Speed Up!
        if delay > 0.01:
            delay -= 0.005

    # Player_0 Win!
    elif ball.xcor() > 350:
        game_is_on = score.increase_score(0)
        ball.reset()
        player_0.reset()
        player_1.reset()
        delay = 0.05
    # Player_1 Win!
    if ball.xcor() < -350:
        game_is_on = score.increase_score(1)
        ball.reset()
        player_0.reset()
        player_1.reset()
        delay = 0.05

    screen.update()


screen.exitonclick()


