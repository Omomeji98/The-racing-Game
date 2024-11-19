from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=600, height=500)
is_race_on = False
user_bet = screen.textinput(title= "The Turtle racing Game", prompt="Choose the color that will win: ")
y_position = [-150, -100, -50, 0, 50, 100, 150]
turtle_color = ["red", "green", "black", "grey", "pink", "yellow", "indigo"]
all_turtle = []
for position_turtle in range(0,7):
    turtle = Turtle("turtle")
    turtle.penup()
    turtle.color(turtle_color[position_turtle])
    turtle.goto(x=-250, y=y_position[position_turtle])
    all_turtle.append(turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() > 280:
            is_race_on = False
            winning_turtle = turtle.pencolor()
            if winning_turtle == user_bet:
                print(f"You win. The winner is {winning_turtle}")
            else:
                print(f"You lost. The winner is {winning_turtle}")
        movement = random.randint(0,20)
        turtle.forward(movement)

screen.exitonclick()


