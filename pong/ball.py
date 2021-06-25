from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.speed(0)
        self.shape("circle")
        self.color("yellow")
        self.move(self.position)
        self.hit_wall()
        # self.hit_paddle()

    def move(self, position):
        self.setheading(45)
        while self.ycor() < 290:
            self.forward(1)

    def hit_wall(self):
        if self.ycor() >= 290 and self.xcor() <= 340:
            self.right(90)
            while self.ycor() > -290:
                self.forward(1)

