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


tim = Turtle()
tim.shape("turtle")

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
#     tim.setheading(random.choice(directions)
#     ...

# draw a cirle repeatedly, changing tilt a little bit each time, randcom color
turtle.colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

def draw_spirograph(gap_size):
    for i in range(int(360/gap_size)):
        turtle.speed("fastest")
        turtle.color(random_color())
        current_heading = turtle.heading()
        turtle.setheading(current_heading + gap_size)
        turtle.circle(100)
draw_spirograph(3)









screen = Screen()
screen.exitonclick()
