import random
from turtle import Turtle

POSITIONS = [(-330, 0), (330,0)]

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("slowest")
        self.color("white")
        self.goto(0,0)
        self.penup()
        self.rand_pos()
        self.move_speed = .05

    def move_ball(self):
        self.setx(self.xcor()+ self.x_move)
        self.sety(self.ycor()+ self.y_move)

    def rand_pos(self):
        self.x_move = 5
        self.y_move = 5

    def wall_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.move_speed *= .9
        self.x_move *= -1
    def reset(self):
        self.goto(0,0)
        self.move_speed = .05


