from turtle import Screen
from snake import *
from food import *
from scoreboard import *
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.tracer(0)
screen.title("Snake Game -> Ver. DY")

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()

    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    # 먹이와 충돌감지
    if snake.head.distance(food) < 10:
        snake.increase_snake()
        food.create_food()
        score.increase_score()




screen.exitonclick()