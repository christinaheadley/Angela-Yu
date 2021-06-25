from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# paddle = Paddle()
# paddle.tracer()
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer()

right_paddle = Paddle()
right_paddle.goto((350, 0))
left_paddle = Paddle()
left_paddle.goto((-350, 0))

screen.listen()
screen.onkeypress(key="Up", fun=right_paddle.up)
screen.onkeypress(key="Down", fun=right_paddle.down)
screen.onkeypress(key="a", fun=left_paddle.up)
screen.onkeypress(key="s", fun=left_paddle.down)

# ball.move(45)
# ball.hit_wall()
# turtle = Turtle()
# turtle.color("blue")
# turtle.setheading(45)
# while turtle.ycor() < 290:
#     turtle.forward(1)
# while turtle.ycor() >= 290:
#     turtle.right(90)
#     turtle.forward(500)

# def hit_paddle(self):


play = True
while play:
    time.sleep(0.1)
    screen.update()
    ball = Ball()
    # if ball.distance(right_paddle) < 50 and ball.xcor() > 340:
    #     print("contact")
    # ball.hit_wall()
    if ball.xcor() > 340:
        print("contact")
screen.exitonclick()
