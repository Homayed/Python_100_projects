from turtle import Turtle, Screen
import turtle
import random


color_list = [(228, 235, 231), (199, 162, 100), (62, 91, 128), (140, 170, 192), (139, 90, 48), (219, 206, 119), (135, 27, 52), (32, 41, 67), (78, 16, 36), (149, 59, 85), (167, 154, 49), (187, 143, 162), (134, 183, 147), (46, 55, 100), (181, 95, 107), (56, 39, 27), (96, 118, 167), (80, 150, 159), (89, 152, 92), (71, 118, 93), (220, 175, 187), (169, 207, 163), (161, 202, 215), (192, 95, 74), (178, 187, 213), (46, 73, 75), (76, 69, 44), (132, 41, 33), (36, 57, 57), (221, 177, 170), (46, 77, 66)]

dot = Turtle()

turtle.colormode(255)
dot.pensize(20)
dot.shape("circle")
dot.speed("fastest")
dot.penup()
dot.setposition(-270,-270)

for _ in range(1,11):
    for i in range(1,11):
        dot.color(random.choice(color_list))
        dot.pendown()
        dot.forward(1)
        dot.penup()
        dot.forward(50)
    dot.penup()
    # Sets the turtle to starting X coordinate with each iteration
    dot.setx(-270)
    dot.sety(-270+50*_) # moves turtle up one row with each iteration
    dot.pendown()
dot.penup()
dot.hideturtle()
dot.setposition(-270,-270)



screen = Screen()
screen.exitonclick()