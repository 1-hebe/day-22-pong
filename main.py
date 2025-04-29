from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("PONG")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "a")
screen.onkey(l_paddle.go_down, "z")

game_is_on = True

while game_is_on:
    time.sleep(.05)
    screen.update()
    ball.move_ball()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.change_angle()

    # Detect collision with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_off_paddle()

    # Detect when paddle misses the ball
    if ball.distance(r_paddle) >= 50 and ball.xcor() > 320:
        print("right paddle out of bounds")
        ball.ball_reset(side_out="right")
        game_is_on = scoreboard.l_point()
    elif ball.distance(l_paddle) >= 50 and ball.xcor() < -320:
        print("left paddle out of bounds")
        ball.ball_reset(side_out="left")
        game_is_on = scoreboard.r_point()

screen.exitonclick()