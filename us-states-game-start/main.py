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
name_turtle = Turtle()

name_turtle.hideturtle()
name_turtle.penup()
score = 0
while score < 50:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state?").title()
    x_coord = states_data[states_data.state == answer_state].x.array
    y_coord = states_data[states_data.state == answer_state].y.array
    if answer_state in coord_list:
        name_turtle.goto(x_coord[0], y_coord[0])
        name_turtle.write(answer_state)
        coord_list.remove(answer_state)
        score += 1
turtle.write("Congratulations! All states guessed!", align="left", font=("Arial", 24, "bold"))
print("Congratulations! All states guessed!")
screen.mainloop()  # alternative to screen.exitonclick() -keeps window open after code executes, won't close if clicked


#AY solution:
import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state's name?").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)
