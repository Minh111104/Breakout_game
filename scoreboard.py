from turtle import Turtle

FONT = ("Consolas", 12, "normal")
SCORE_POS = (200, 215)
HEART_POS = (-350, 215)


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hearts = 5
        self.hideturtle()
        self.penup()
        self.color("white")
        self.goto(SCORE_POS)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(SCORE_POS)
        self.write(f"Score: {self.score}", align="left", font=FONT)
        self.goto(HEART_POS)
        hearts_display = "❤️" * self.hearts
        self.write(f"Hearts: {hearts_display}", align="left", font=FONT)
        self.goto(0, 215)
        self.write("BREAKOUT", align="center", font=FONT)

    def add_score(self, points):
        self.score += points
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
