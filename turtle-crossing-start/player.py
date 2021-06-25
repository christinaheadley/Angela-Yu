from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.pu()
        self.goto(0, -280)
        self.seth(90)
        self.color("black")
        self.shape("turtle")
        self.move_speed = "fastest"

    def move_up(self):
        self.forward(20)
        
    def speed_up(self):


# Create a turtle player that starts at the bottom of the screen and
# listen for the "Up" keypress to move the turtle north. If you get stuck,
# check the video walkthrough in Step 3.

# Detect when the turtle player collides with a car and stop the game
# if this happens. If you get stuck, check the video walkthrough in Step 5.

# Detect when the turtle player has reached the top edge of the screen
# (i.e., reached the FINISH_LINE_Y). When this happens, return the turtle to the
# starting position and increase the speed of the cars.
# Hint: think about creating an attribute and using the MOVE_INCREMENT to increase
# the car speed. If you get stuck, check the video walkthrough in Step 6.