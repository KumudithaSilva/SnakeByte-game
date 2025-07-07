from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 270)
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def score_update(self):
        self.clear()
        self.score += 1
        self.write(f"Score : {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)

