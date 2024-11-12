import turtle
from turtle import Screen, Turtle
import pandas

sc = Screen()
sc.title("U.S.States Game")

image = "blank_states_img.gif"
sc.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
states = data.state.to_list()


guesses = []

while len(guesses) < 50:
    state_guess = sc.textinput(title=f"{len(guesses)}/{len(states)} States guessed", prompt="What's another state name? ").title()

    if state_guess == "Exit":
        missing_states = []
        for i in states:
            if i not in guesses:
                missing_states.append(i)

        print("Missing States --> ",missing_states)
        # missin = pandas.DataFrame(missing_states)
        # missin.to_csv("States_to_learn.csv")
        break

    if state_guess in states:
        guesses.append(state_guess)
        t = Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == state_guess]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(state_guess)