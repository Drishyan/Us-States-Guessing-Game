import turtle
import pandas

screen = turtle.Screen()
screen.title("US State Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()
guessed_states = []
missed_states = []
while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 states correct",prompt="Whats another state name?").title()
    if answer_state == "Exit":
        for state in states:
            if state not in guessed_states:
                missed_states.append(state)
        new_data = pandas.DataFrame(missed_states)
        new_data.to_csv("missed_states.csv")
        break
    if answer_state in states:
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        state_data = data[data["state"] == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        guessed_states.append(answer_state)

screen.exitonclick()
