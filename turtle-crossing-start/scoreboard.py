from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.pu()
        self.goto(0, 270)
        self.level = 0
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def end_game(self):
        self.goto(0, 0)
        self.color("black")
        self.write("GAME OVER", align="center", font=FONT)

    def update_score(self):
        self.clear()
        self.goto(0, 270)
        self.level += 1
        self.write(f"Level: {self.level}", align="center", font=FONT)


# Create a scoreboard that keeps track of which level the user is on. Every time the
# turtle player does a successful crossing, the level should increase. When the turtle hits a car,
# GAME OVER should be displayed in the centre. If you get stuck, check the video walkthrough in Step 7.
