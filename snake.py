from turtle import Turtle

MOVE_DISTANCE = 20
DEFAULT_X_COORDINATE = 20
SNAKE_SIZE = 3

class Snake:
    def __init__(self):
        self.snake_color = "white"
        self.snake_shape = "square"
        self.snake_x_coordinates = 0.00
        self.segment = []
        self.create_snake()

    def create_snake(self):
        self.snake_x_coordinates = 0.00
        for _ in range(SNAKE_SIZE):
            new_turtle = Turtle(self.snake_shape)
            new_turtle.color(self.snake_color)
            new_turtle.penup()
            new_turtle.goto(self.snake_x_coordinates, 0.00)
            self.snake_x_coordinates -= DEFAULT_X_COORDINATE
            self.segment.append(new_turtle)

    def move_snake(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            new_x = self.segment[seg - 1].xcor()
            new_y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(new_x, new_y)
        self.segment[0].forward(MOVE_DISTANCE)
        self.segment[0].left(90)

