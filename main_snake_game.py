from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard
''' Tasks:
1- create a snake body. (Done)
2- move the snake. (Done)
3- create snake food (done)
4- detect collision with food. (done) 
5- create a scoreboard (done)
6- detect collision with wall (done)
7- detect collision with tail (done)
'''

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)


snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.right, "d")
screen.onkey(snake.left, "a")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()

    #detect collision with food
    if snake.head.distance(food) < 15 :
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    #detect collision with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
        scoreboard.reset()
        snake.reset_snake()


    #detect collision with tail
    for part in snake.snake_parts[1:]:
        if snake.head.distance(part) < 10:
            scoreboard.reset()
            snake.reset_snake()
            


        

    






















screen.exitonclick()