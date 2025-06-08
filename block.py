from turtle import Turtle
import random

COLORS = ["red", "yellow", "blue", "green", "orange", "purple", "pink", "brown"]


class Blocks():
    def __init__(self):
        self.blocks = []

    def create_blocks(self):
        for x in range(-350, 351, 70):
            for y in range(30, 150, 30):
                new_block = Turtle("square")
                new_block.penup()
                new_block.shapesize(stretch_wid=1, stretch_len=3)
                new_block.color(random.choice(COLORS))
                new_block.goto(x, y)
                self.blocks.append(new_block)
                