import random
from turtle import Turtle, Screen

screen = Screen()
turtle = Turtle()
color_list = [(216, 227, 244), (107, 178, 218), (15, 105, 187), (223, 152, 75), (219, 77, 151), (225, 118, 186), (226, 205, 90), (234, 209, 233), (16, 188, 112), (36, 132, 49), (35, 37, 150), (205, 9, 44), (102, 198, 161), (4, 11, 98), (239, 65, 33), (194, 165, 42), (16, 181, 219), (140, 210, 233), (182, 41, 76), (235, 223, 202), (213, 153, 225), (207, 235, 226), (109, 38, 26), (100, 33, 21), (206, 49, 25), (173, 177, 231), (150, 214, 193), (84, 119, 188), (71, 13, 40), (47, 97, 22)]
screen.colormode(255)
print(color_list[0])
# print painting 10 x 10 color dots
turtle.penup()
turtle.setpos(-250.00, -250.00)
turtle.speed("fastest")
i = 0
print(random.choice(color_list))
while i < 100:
    color = random.choice(color_list)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(10)
    turtle.end_fill()
    turtle.penup()
    turtle.forward(50)
    i += 1
    if i % 10 == 0:
        turtle.setpos(-250.00, -250.00 + i*5)
    else:
        continue

screen.exitonclick()

AY solution:
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)