STARTING_POSITION = (0, -270)
from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.reset_position()
        self.seth(90)

    def move(self):
        new_y = self.ycor() + 10
        self.goto(self.xcor(), new_y)

    def reset_position(self):
        self.goto(STARTING_POSITION)
