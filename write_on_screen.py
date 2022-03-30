from turtle import Turtle


class Write(Turtle):
    def __init__(self):
        super().__init__()
        self.guessed_states = []
        self.guessed_states_count = len(self.guessed_states)
        self.hideturtle()

    def create_turtle(self, answer, x, y):
        new_turtle = Turtle()
        new_turtle.hideturtle()
        new_turtle.penup()
        new_turtle.goto(x, y)
        new_turtle.write(f"{answer}")
        self.guessed_states_count += 1
        self.guessed_states.append(f"{answer}")
