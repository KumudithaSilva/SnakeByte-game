from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-30, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)