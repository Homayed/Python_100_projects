import random
import turtle
from random import choice
from turtle import Turtle, Screen
turtle.colormode(255)
tim = Turtle()
tim.shape("turtle")
tim.speed("fastest")

def change_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    tim.color(r, g, b)


def set_gap(size_of_gap):
    for i in range(int(360/size_of_gap)):
        change_color()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

set_gap(3)



















screen = Screen()
screen.exitonclick()