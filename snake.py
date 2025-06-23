from turtle import Turtle

MOVE_DISTANCE = 20
DEFAULT_X_COORDINATE = 20
SNAKE_SIZE = 3
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:
    def __init__(self):
        self.snake_color = "green"
        self.snake_shape = "square"
        self.snake_x_coordinates = 0.00
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

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
        self.head.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def move_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def move_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def move_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)




