from turtle import Turtle
import random

from player import MOVE_DISTANCE

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = MOVE_DISTANCE
    def create_car(self):
        rand_chance = random.randint(1,6)
        if rand_chance == 1:
            turtle = Turtle()
            turtle.shape("turtle")
            turtle.shapesize(stretch_len=2, stretch_wid=1)
            turtle.color(random.choice(COLORS))
            turtle.penup()
            turtle.goto(280, random.randint(-280, 280))
            self.all_cars.append(turtle)

    def move_car(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT



