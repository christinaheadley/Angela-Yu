from turtle import Screen, Turtle
import time
from snake import Snake

screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor("black")
screen.title("A Snake Game")
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")

# screen.onkey(snake.seth(180), "e")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
