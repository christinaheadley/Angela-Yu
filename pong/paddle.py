from turtle import Turtle


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.create_paddle()

    def create_paddle(self):
        self.penup()
        self.speed("fastest")
        self.setheading(270)
        self.shape("square")
        self.color("red")
        self.turtlesize(stretch_wid=None, stretch_len=5, outline=None)

    def up(self):
        self.setheading(90)
        if self.ycor() < 260:
            self.forward(20)

    def down(self):
        self.setheading(270)
        if self.ycor() > -260:
            self.forward(20)
