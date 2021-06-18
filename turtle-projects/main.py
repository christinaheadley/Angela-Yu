import turtle
from turtle import Turtle, Screen
import random
# OR
# import turtle
# tim = turtle.Turtle()
# OR
# import turtle as t
# tim = t.Turtle()
# OR
# from turtle import * (import all -- not recommended for clean code)


# turtle = Turtle()
# turtle.shape("turtle")

# #make a square
# for _ in range(4):
#     turtle.forward(100)
#     turtle.right(90)

# import heroes
# print(heroes.gen())
#draw a dashed line:
# for _ in range(10):
#     turtle.pendown()
#     turtle.forward(5)
#     turtle.penup()
#     turtle.forward(5)

#draw 3-10 sided-shapes in random color. each side length 100,
# laid out on top of each other and printed in sequence
# 360/ # of sides = degree of angle
# for number in range(3, 11):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.pencolor(r, g, b)
#     for i in range(number):
#         turtle.forward(100)
#         turtle.right(360/number)

# AY solution:
# colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
#
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         tim.forward(100)
#         tim.right(angle)
#
# for shape_side_n in range(3, 10):
#     tim.color(random.choice(colours))
#     draw_shape(shape_side_n)

# draw a random walk
# progressing by same distance, then choosing any of four directions to continue
# keep random color with each walk
# increase line thickness and speed of line drawing
#
# turtle.pensize(8)
# for number in range(333):
#     r = random.random()
#     g = random.random()
#     b = random.random()
#     turtle.pencolor(r, g, b)
#     turtle.speed(10)
#     turtle.forward(15)
#     turtle.right(float(random.choice([0, 90, 180, 270])))
#
# # AY solution:
# turtle.colormode(255)
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     random_color = (r, g, b)
#     return random_color
#
# for i in range(200):
#     turtle.color(random_color)
#     tim.setheading(random.choice(directions))
#     ...

# draw a cirle repeatedly, changing tilt a little bit each time, random color
# turtle.colormode(255)

# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     color = (r, g, b)
#     return color
#
# def draw_spirograph(gap_size):
#     for i in range(int(360/gap_size)):
#         turtle.speed("fastest")
#         turtle.color(random_color())
#         current_heading = turtle.heading()
#         turtle.setheading(current_heading + gap_size)
#         turtle.circle(100)
# draw_spirograph(3)

# ########ETCH-A-SKETCH########

screen = Screen()
screen.listen()
# def move_forwards():
#     turtle.forward(10)
#
# def move_backwards():
#     turtle.backward(10)
# def turn_left():
#     # new_heading = turtle.heading() + 10 #AY way
#     # turtle.setheading(new_heading)
#     turtle.left(10)
#     turtle.forward(10)
# def turn_right():
#     turtle.right(10)
#     turtle.forward(10)
# def reset():
#     screen.reset()

# screen.onkeypress(key="e", fun=move_forwards)
# screen.onkeypress(key="s", fun=move_backwards)
# screen.onkeypress(key="a", fun=turn_left)
# screen.onkeypress(key="z", fun=turn_right)
# screen.onkeypress(key="c", fun=reset)

 # #####TURTLE RACING########
screen.setup(width=500, height=400)
race_is_on = False
user_bet = screen.textinput(title="Make your bet", prompt="Which color will win? ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70, -40, -10, 20, 50, 80]
all_turtles = []
for i in range(len(colors)):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.setpos(x=-230, y=y_positions[i])
    turtle.color(colors[i])
    all_turtles.append(turtle)

if user_bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)
    if turtle.xcor() > 230:
        # race_is_on = False
        if user_bet.lower == turtle.pencolor():
            print(f"You won! The winner is {turtle.pencolor()}!")
        else:
            print(f"You lost! The winner was {turtle.pencolor()}!")







screen.exitonclick()
