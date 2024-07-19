from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
user_bet = screen.textinput("Bet", "Which colour would win the race? Enter the colour: ")
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
y_position = [100, 60, 20, -20, -60, -100]
all_turtles = []

for i in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_position[i])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 210:
            is_race_on = False
            win_colour = turtle.pencolor()
            if win_colour == user_bet:
                print(f"You've won! The {win_colour} turtle is the winner.")
            else:
                print(f"You lost! The {win_colour} turtle is the winner.")

        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
