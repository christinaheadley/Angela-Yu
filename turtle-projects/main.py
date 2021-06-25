from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.pu()
        self.shape("square")
        self.shapesize(1, 2, 0)
        self.setheading(180)
        self.setx(260)
        for color in COLORS:
            random_y = random.randint(-250, 250)
            self.sety(random_y)
            self.color(color)