import random
import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard,FONT,LEVEL

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()




scoreboard = Scoreboard()
player = Player()
car = CarManager()

screen.onkey(fun = player.move_up, key= "Up")



game_is_on = True
while game_is_on:
    time.sleep(.1)
    car.create_car()
    car.move_car()
    for c in car.all_cars:
        if player.distance(c) < 15:
            scoreboard.goto(0,0)
            scoreboard.write("GAME OVER",False,"center",FONT)
            game_is_on = False
    if player.is_at_finishline():
        player.go_to_start()
        car.level_up()
        scoreboard.increase_level()
    screen.update()












screen.exitonclick()