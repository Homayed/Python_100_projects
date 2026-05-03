import turtle
from turtle import Screen, Turtle
import pandas

data = pandas.read_csv("50_states.csv")

screen = Screen()

screen.title("U.S. State Game")
image = "img.gif"
screen.addshape(image)

turtle.shape(image)

screen.tracer(0)

import turtle

game_is_on = True
correct_guess_number = 0
cn = 0
list1 = []

state_list = data.state.to_list()



print(state_list)


while len(list1) < 50:
    answer_state = screen.textinput(f"You guessed {len(list1)}/50", "Whats your guess?").title()
    if answer_state == "Exit":
        list2 = [item for item in state_list if item not in list1]
        missing_state = pandas.DataFrame(list2)
        missing_state.to_csv("missing_state.csv")
        break
    elif answer_state in state_list:
        if answer_state not in list1:
            list1.append(answer_state)
            state = data[data["state"] == answer_state]
            turtle.penup()
            turtle.hideturtle()
            turtle.color("black")
            turtle.goto(x=state.x.item(), y=state.y.item())
            turtle.write(answer_state, True, "center", ("ariel", 12, "bold"))
            turtle.home()
    else:
        pass




screen.update()















