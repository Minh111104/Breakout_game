import os
from turtle import Turtle

FONT = ("Consolas", 12, "normal")
SCORE_POS = (200, 215)
HEART_POS = (-350, 215)
HIGH_SCORE_FILE = "highscore.txt"

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hearts = 5
        self.high_score = self.load_high_score()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_POS)
        self.update_scoreboard()

    def load_high_score(self):
        if os.path.exists(HIGH_SCORE_FILE):
            with open(HIGH_SCORE_FILE, "r") as f:
                try:
                    return int(f.read())
                except ValueError:
                    return 0
        return 0

    def save_high_score(self):
        with open(HIGH_SCORE_FILE, "w") as f:
            f.write(str(self.high_score))

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POS)
        self.write(f"Score: {self.score}  High: {self.high_score}", align="left", font=FONT)
        self.goto(HEART_POS)
        hearts_display = "❤️" * self.hearts
        self.write(f"Hearts: {hearts_display}", align="left", font=FONT)
        self.goto(0, 215)
        self.write("BREAKOUT", align="center", font=FONT)

    def add_score(self, points):
        self.score += points
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()

    def lose_life(self):
        self.hearts -= 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, -50)
        self.write("GAME OVER", align="center", font=FONT)

    def you_win(self):
        self.goto(0, 0)
        self.write("YOU WIN!", align="center", font=FONT)

    def display_final_score(self):
        self.goto(0, -100)
        self.write(f"You scored: {self.score}", align="center", font=FONT)