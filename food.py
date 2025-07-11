from turtle import  Turtle
import  random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('snake_food.gif')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.speed(0)
        self.refresh()

    def refresh(self):
        x_param = random.randint(-280, 280)
        y_param = random.randint(-280, 280)

        self.goto(x_param, y_param)
