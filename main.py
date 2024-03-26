from turtle import Screen
from food import Food
from score import Score
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)  # turn turtle animation on/off and set delay for update drawings.

score = Score()
snake = Snake()  # create snake object
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)  # delay the refresh
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # food is 10x15
        food.refresh()
        snake.extend()
        score.increase_score()

    #  Defect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 295 or snake.head.ycor() < -295:
        # game_is_on = False
        # score.game_over()
        score.reset()
        snake.reset()

    # Defect collision with tail
    # if head collides with any segment in the tail, trigger game over
    for segment in snake.segments[1:]:  # slice to skip the snake head
        if snake.head.distance(segment) < 10:
            # game_is_on = False
            # score.game_over()
            score.reset()
            snake.reset()
screen.exitonclick()

# TODO 1: Implement play again feature
# TODO 2: Implement level feature (+speed)
