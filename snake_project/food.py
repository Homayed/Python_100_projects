from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=.5,stretch_wid=.5)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        rand_x = random.randint(a=-280, b=280)
        rand_y = random.randint(a=-280, b=280)
        self.goto(rand_x, rand_y)




