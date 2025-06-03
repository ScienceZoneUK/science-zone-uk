import turtle
import random

class Horse:
    def __init__(self, name, color, y_pos):
        self.name = name
        self.color = color
        self.y_pos = y_pos
        self.t = turtle.Turtle()
        self.t.shape("turtle")
        self.t.color(color)
        self.t.penup()
        self.t.goto(-200, y_pos)

    def move(self):
        step = random.randint(1, 10)
        self.t.forward(step)

    def get_position(self):
        return self.t.xcor()

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
        lane.forward(420)
