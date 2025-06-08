from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("gray")
        self.penup()
        self.speed("fastest")
        self.x_move = random.choice([-6, 6])
        self.y_move = 6

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0, -180)
        self.x_move = 6
        self.y_move = 6

    def set_direction(self, offset):
        self.y_move = abs(self.y_move)
        self.x_move = offset / 10
