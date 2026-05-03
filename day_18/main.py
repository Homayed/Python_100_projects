from turtle import Turtle,Screen
import random

screen = Screen()
screen.setup(width=500,height=400)

user_bet = screen.textinput(title= "Enter a bet", prompt= "What color are you betting on? choose your club" )
colors = ["red", "orange", "black", "green", "blue", "purple"]
clubs = ["Arsenal" , "Liverpool" , "Man City" , "Man Utd" , "Chelsea" , "Spurs"]
y_pos = [-100 , -60 , -20 , 20 , 60 , 100]
all_turtles = []
is_race_on = False

for turtle_number in range(1,7):
    new_turtle = Turtle("turtle")
    new_turtle.penup()
    new_turtle.goto(x = -230, y = y_pos[turtle_number - 1])
    new_turtle.color(colors[turtle_number - 1])
    new_turtle.write(clubs[turtle_number-1], move=True, align="center")
    all_turtles.append(new_turtle)


if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_color = turtle.pencolor()
            is_race_on = False
            if winning_color == user_bet:
                print(f"You win. The winning club is {winning_color}")
            else:
                print(f"You lose. The winning club is {winning_color}")


        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)




screen.exitonclick()