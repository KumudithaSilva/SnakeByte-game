#  TODO 3. Generate Random Food on Screen
#  TODO 4. Detect Collision with Food
#  TODO 5. Create Scoreboard
#  TODO 6. Detect Collision with Wall
#  TODO 7. Detect Collision with snake tail

from turtle import Screen
from snake import  Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Byte Game")
screen.tracer(0)

#  TODO 1. Create the snake body
snake = Snake()

#  TODO 2. Move the snake with events
game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.1)













screen.exitonclick()



















