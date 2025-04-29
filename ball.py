import random
from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.setheading(random.randint(0,360))
        self.move_speed = 5

    def move_ball(self):
        self.forward(self.move_speed)

    def increase_speed(self):
        if self.move_speed < 10:
            self.move_speed += .2
            print(self.move_speed)

    def change_angle(self):
        current_heading = self.heading()
        # add jitter to the ball
        jitter = random.randint(-10 , 10)
        new_heading = 360 - current_heading + jitter
        self.setheading(new_heading)

    def bounce_off_paddle(self):
        current_heading = self.heading()
        # add jitter to the ball
        jitter = random.randint(-10, 10)
        new_heading = 180 - current_heading + jitter
        self.setheading(new_heading)
        self.increase_speed()

    def ball_reset(self, side_out):
        self.goto(0,0)
        if side_out == "right":
            self.setheading(random.randint(120, 240))
        else:
            self.setheading(random.randint(-60,30))

