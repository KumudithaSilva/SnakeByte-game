from turtle import Turtle, Screen

MOVE_DISTANCE = 20
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 360

class Snake:
    def __init__(self):
        self.snake_color = "blue"
        self.snake_shape = "square.gif"
        self.segment = []
        self.create_snake()
        self.head = self.segment[0]

    def create_snake(self):
        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle(self.snake_shape)
        new_turtle.color(self.snake_color)
        new_turtle.penup()
        new_turtle.goto(position)
        self.segment.append(new_turtle)

    def extend_segment(self):
        self.add_segment(self.segment[-1].position())

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

    def reset_snake(self):
        for seg in self.segment:
            seg.hideturtle()
            seg.clear()
        self.segment.clear()
        self.create_snake()
        self.head = self.segment[0]






