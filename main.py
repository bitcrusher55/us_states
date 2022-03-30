import turtle
import pandas
from write_on_screen import Write

screen = turtle.Screen()
screen.title("States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

write = Write()
data = pandas.read_csv("50_states.csv")
list_of_states = data.state.to_list()

game_is_on = True
while game_is_on:
    answer = screen.textinput(title=f"{write.guessed_states_count}/50 guessed", prompt="What's another state?").title()
    if len(write.guessed_states_count) == 50:
        game_is_on = False
    if answer in write.guessed_states:
        continue
    elif answer in list_of_states:
        answer_row = data[data.state == f"{answer}"]
        x_cor = int(answer_row.x)
        y_cor = int(answer_row.y)
        write.create_turtle(answer, x_cor, y_cor)
    else:
        continue









