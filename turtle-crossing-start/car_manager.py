from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        random_y = random.randint(-250, 250)
        self.sety(random_y)
        random_x = random.randint(-300, 300)
        self.setx(random_x)
        self.shape("square")
        self.shapesize(1, 2, 0)
        self.setheading(-180)
        self.showturtle()
        self.color(random.choice(COLORS))
        self.move_speed = STARTING_MOVE_DISTANCE

    def move_car(self):
        if self.xcor() > -300:
            new_x = self.xcor() - MOVE_INCREMENT
            self.goto(new_x, self.ycor())
        else:
            new_x = 300
            self.goto(new_x, self.ycor())

    def speed_up(self):
        self.move_speed += MOVE_INCREMENT


# class Ball(Turtle):
#
#     def __init__(self):
#         super().__init__()
#         self.color("blue")
#         self.shape("circle")
#         self.penup()
#         self.x_move = 3
#         self.y_move = 3
#         self.move_speed = 0.1
#
#     def move(self):
#         new_x = self.xcor() + self.x_move
#         new_y = self.ycor() + self.y_move
#         self.goto(new_x, new_y)

# Create cars that are 20px high by 40px wide that are randomly generated along the
# y-axis and move to the left edge of the screen. No cars should be generated in the
# top and bottom 50px of the screen (think of it as a safe zone for our little turtle).
# Hint: generate a new car only every 6th time the game loop runs. If you get stuck,
# check the video walkthrough in Step 4.