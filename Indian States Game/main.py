import turtle
import pandas as pd

screen = turtle.Screen()
IMAGE = 'India_map_blank.gif'
screen.title("INDIA States Quiz")
screen.addshape(IMAGE)
turtle.shape(IMAGE)

df = pd.read_csv('Indian_States.csv')
all_states = df['state'].to_list()
guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)}/50 States Correct!",
                                  prompt="What's another state's name?").title()

    if user_input == 'Exit':
        missed_states = [state for state in all_states if state not in guessed_states]
        missed_data = pd.DataFrame(missed_states)
        missed_data.to_csv('States_you_missed.csv')
        break

    if user_input in all_states:
        guessed_states.append(user_input)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = df[df.state == user_input]
        t.goto(int(state_data.x.item()), int(state_data.y.item()))
        t.write(user_input)

screen.exitonclick()
