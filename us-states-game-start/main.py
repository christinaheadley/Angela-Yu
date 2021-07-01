from turtle import Turtle, Screen
import pandas

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


screen.onscreenclick(get_mouse_click_coor)

# keep track of total correct out of 50 in title
states_data = pandas.read_csv("50_states.csv")
coord_list = states_data["state"].to_list()
# print(coord_list)
# print(type(coord_list))
name_turtle = Turtle()
name_turtle.hideturtle()
name_turtle.penup()
while len(coord_list) > 0:
    answer_state = screen.textinput(title="Guess the State", prompt="What's another state?").title()
    #get row containing answer state
    # coords_row =
    # answer_state = states_data.state
    # print(f"X: {states_data[states_data.state == answer_state]}")
    x_coord = states_data[states_data.state == answer_state].x.array
    y_coord = states_data[states_data.state == answer_state].y.array
    # print(f"X is {x_coord}")
    # print(type(x_coord))
    # print(f"Y is {y_coord}")
    # print(y_coord)

    # print(f"Coordinates :{x_coord[0]}, {y_coord[0]}")
    # print(coords_row)
    if answer_state in coord_list:
        # print("truE")
        name_turtle.goto(x_coord[0], y_coord[0])
        name_turtle.write(answer_state)
        coord_list.remove(answer_state)
        # print(coord_list)
    else:
        print("Congratulations! All states guessed!")
screen.mainloop() # alternative to screen.exitonclick() -keeps window open after code executes, doesn't close if clicked

