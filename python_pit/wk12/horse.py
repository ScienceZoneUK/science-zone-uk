import turtle
import random

class Horse:
    def __init__(self, name, color, y_pos, finish_line=200):
        self.name = name
        self.color = color
        self.y_pos = y_pos
        self.finish_line = finish_line
        self.has_won = False  # Win flag

        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color(color)
        self.t.penup()
        self.t.goto(-200, y_pos)

    def move(self):
        step = random.randint(1, 10)
        self.t.forward(step)
        self.check_win()

    def get_position(self):
        return self.t.xcor()

    def check_win(self):
        if self.t.xcor() >= self.finish_line:
            self.has_won = True
        return self.has_won

    def celebrate(self):
        self.t.write(" I won!", font=("Arial", 14, "bold"))

    def draw_lane(self):
        lane = turtle.Turtle()
        lane.hideturtle()
        lane.speed(0)
        lane.color("gray")
        lane.penup()
        lane.goto(-210, self.y_pos - 10)
        lane.pendown()
        lane.forward(self.finish_line + 10)
