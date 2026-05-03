from turtle import Turtle

FONT = ("Courier", 24, "normal")
LEVEL = 1

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-230,250)
        self.color("black")
        self.write(f"Level:{self.level}",False,"center",FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level:{self.level}", False, "center", FONT)
