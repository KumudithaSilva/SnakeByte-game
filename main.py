from turtle import Screen, Turtle

from food import Food
from scoreboard import Score
from snake import  Snake
import time

screen = Screen()

screen.register_shape('square.gif')
screen.register_shape('easter-egg.gif')
screen.bgpic("snake-game.gif")

screen.setup(width=600, height=600)
screen.title("Snake Byte Game")
screen.tracer(0)

#  TODO 1. Create the snake body
snake = Snake()
food = Food()
score = Score()

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
        snake.extend_segment()
        #  TODO 5. Create Scoreboard
        score.score_update()

    #  TODO 6. Detect Collision with Wall
    if (snake.head.xcor() > 280 or snake.head.xcor() < -280
            or snake.head.ycor() > 280 or snake.head.ycor() < -280):
        game_is_on = False
        score.game_over()

    #  TODO 7. Detect Collision with snake tail
    for segments in snake.segment:
        if segments == snake.head:
            pass
        elif snake.head.distance(segments) < 10:
            game_is_on = False
            score.game_over()


screen.exitonclick()



















