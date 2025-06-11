import turtle
import tkinter
import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from block import Blocks
from scoreboard import Score

def show_message(screen, message):
    msg_turtle = Turtle()
    msg_turtle.hideturtle()
    msg_turtle.color("white")
    msg_turtle.penup()
    msg_turtle.goto(0, 0)
    msg_turtle.write(message, align="center", font=("Arial", 24, "bold"))
    return msg_turtle

def clear_message(msg_turtle):
    msg_turtle.clear()
    msg_turtle.hideturtle()

def play_game(screen, score):
    # Clear everything from previous game
    screen.clearscreen()
    screen.bgcolor("black")
    screen.setup(width=800, height=500)
    screen.title("Breakout")
    screen.tracer(0)

    paddle = Paddle()
    ball = Ball()
    block = Blocks()
    block.create_blocks()
    score.score = 0
    score.hearts = 5
    score.update_scoreboard()

    screen.listen()
    screen.onkey(paddle.go_left, "Left")
    screen.onkey(paddle.go_right, "Right")

    game_is_on = True

    while game_is_on:
        time.sleep(0.03)
        screen.update()
        ball.move()

        if ball.ycor() > 230:
            ball.bounce_y()

        if ball.xcor() > 370 or ball.xcor() < -370:
            ball.bounce_x()

        if ball.y_move < 0 and -210 < ball.ycor() < -190:
            if paddle.xcor() - 100 < ball.xcor() < paddle.xcor() + 100:
                offset = ball.xcor() - paddle.xcor()
                ball.set_direction(offset)

        if ball.ycor() < -230:
            ball.reset_position()
            score.hearts -= 1
            paddle.goto(0, -200)
            score.update_scoreboard()
            if score.hearts <= 0:
                game_is_on = False
                break

        for b in block.blocks[:]:
            if b.distance(ball) < 30:
                ball.bounce_y()
                b.hideturtle()
                block.blocks.remove(b)
                score.add_score(10)
            if len(block.blocks) == 0:
                score.you_win()
                score.display_final_score()
                game_is_on = False
                break

    score.game_over()
    score.display_final_score()

    # Show restart message
    restart_msg = show_message(screen, "Press 'SPACE' to Restart or 'ESC' to Quit")
    waiting = True

    def restart():
        nonlocal waiting
        waiting = False
        clear_message(restart_msg)
        screen.onkey(None, "space")  # Remove handler to avoid stacking
        screen.onkey(None, "Escape")

    def quit_game():
        screen.bye()
    screen.onkey(restart, "space")
    screen.onkey(quit_game, "Escape")

    while waiting:
        screen.update()
        time.sleep(0.05)

def main():
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=500)
    screen.title("Breakout")
    screen.tracer(0)
    score = Score()  # Create Score ONCE

    try:
        # Show start screen
        start_msg = show_message(screen, "Press 'SPACE' to Start Breakout!")
        waiting = True
        
        def start():
            nonlocal waiting
            waiting = False
            clear_message(start_msg)
            screen.onkey(None, "space")
        
        screen.listen()
        screen.onkey(start, "space")
        
        while waiting:
            screen.update()
            time.sleep(0.05)

        while True:
            play_game(screen, score)  # Pass score object

    except (turtle.Terminator, tkinter.TclError):
        print("Turtle graphics window closed.")

if __name__ == "__main__":
    main()