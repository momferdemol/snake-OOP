import time
from turtle import Screen

from classes.food import Food
from classes.scoreboard import Scoreboard
from classes.snake import Snake

# game is active true/false
game_is_on = True

# set game screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Jake the snake")

# set new game objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()

# set game control keys
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# keep the game going until game over
while game_is_on:
    screen.update()
    time.sleep(0.1)

    # move Mr. Jake the snake
    snake.move()

    # detect eating food and extend snake
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add_point()

    # detect collision with wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        scoreboard.game_over()

    # detect collision with tail
    # fetch each segement without the head
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            scoreboard.game_over()

# keep screen visible until user clicks the canvas
screen.exitonclick()
