from turtle import  Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "bold")
GAME_OVER_FONT = ("Courier", 35, "bold")
FILE_NAME = "game_data/data.txt"

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-10, 270)
        self.read_data(FILE_NAME)
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align=ALIGNMENT, font=FONT)
        self.score_update()

    def read_data(self, data_file):
        with open(data_file, mode="r") as file:
            self.high_score = int(file.read())

    def write_data(self):
        with open(FILE_NAME, mode="w") as file:
            file.write(str(self.high_score))

    def score_update(self):
        self.clear()
        self.write(f"Score : {self.score}, High Score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1

    def rest(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_data()
        self.score = 0
        self.score_update()


