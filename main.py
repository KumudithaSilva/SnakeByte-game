#  TODO 5. Create Scoreboard
#  TODO 6. Detect Collision with Wall
#  TODO 7. Detect Collision with snake tail

from turtle import Screen

from food import Food
from snake import  Snake
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.title("Snake Byte Game")
screen.tracer(0)

#  TODO 1. Create the snake body
snake = Snake()
food = Food()

#  TODO 2. Move the snake with events
screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.move_left, "Left")
screen.onkey(snake.move_right, "Right")

game_is_on = True
while game_is_on:
    snake.move_snake()
    screen.update()
    time.sleep(0.1)

    #  TODO 4. Detect Collision with Food
    if snake.head.distance(food) < 15:
        #  TODO 3. Generate Random Food on Screen
        food.refresh()











screen.exitonclick()



















