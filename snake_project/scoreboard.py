from turtle import Turtle
file = open("data.txt")
content = file.read()

ALIGNMENT = "center"
FONT = ("courier", 20, "normal")
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.set_score = 0
        self.highest_score = int(content)
        self.count_on = True
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Total Score: {self.set_score} Highest Score: {self.highest_score}", False, ALIGNMENT ,FONT)

    def track_score(self):
        self.set_score += 1
        self.show_score()

    def reset(self):
        if self.set_score > self.highest_score:
            self.highest_score = self.set_score
            file = open("data.txt",mode ="w")
            file.write(f"{self.highest_score}")
            file.close()
        self.set_score = 0
        self.show_score()







