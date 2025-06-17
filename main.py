#  TODO 2. Move the snake with events
#  TODO 3. Generate Random Food on Screen
#  TODO 4. Detect Collision with Food
#  TODO 5. Create Scoreboard
#  TODO 6. Detect Collision with Wall
#  TODO 7. Detect Collision with snake tail

from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Byte Game")

#  TODO 1. Create the snake body
x = 0.00
for _ in range(3):
    turtle = Turtle("square")
    turtle.color("white")
    turtle.goto(x, 0.00)
    x -= 20





screen.exitonclick()