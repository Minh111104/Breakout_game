from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.goto(0, -200)

    def go_left(self):
        if self.xcor() > -340:
            new_x = self.xcor() - 60
            self.goto(new_x, self.ycor())

    def go_right(self):
        if self.xcor() < 340:
            new_x = self.xcor() + 60
            self.goto(new_x, self.ycor())
