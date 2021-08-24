import turtle
import pandas

screen = turtle.Screen()
screen.screensize(1150, 1150)
screen.title("India states game")
image = "india_map.gif"
screen.addshape(image)
turtle.shape(image)

data = pandas.read_csv("list-indian-states-and-capitals-28.csv")
all_states = data["state"].to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_State = screen.textinput(title="Guess the state",
                                    prompt="Whats another state?").title()

    if answer_State == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states missed")
        break

    if answer_State in all_states:
        guessed_states.append(answer_State)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_State]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_State)

screen.exitonclick()
