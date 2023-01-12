# Poog Game Scoreboard
from turtle import Turtle

ALIGN = "center"
FONT = ("Arial", 32, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = [0, 0]
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        self.write(f"{self.score[0]} : {self.score[1]}", align=ALIGN, font=FONT)

    def increase_score(self, num):
        self.score[num] += 1
        self.clear()
        self.update_score()
        if self.score[num] == 5:
            self.game_over(num)
            return False
        return True

    def game_over(self, num):
        self.home()
        self.write(f"Player_{num} Win!\n Score : {self.score[0]} : {self.score[1]}", align=ALIGN, font=FONT)


