from turtle import Turtle



class Scoreboard(Turtle):

    def __init__(self,position):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.r_score = 0
        self.goto(position)
        self.color("white")
        self.write(f"{self.score}", False, "center", ("ariel", 50, "normal"))

    def hold_score(self):
        self.clear()
        self.score = self.score + 1
        self.write(f"{self.score}", False, "center", ("ariel", 50, "normal"))




