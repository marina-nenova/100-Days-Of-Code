import turtle
from turtle import Turtle
import random


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(360 // size_of_gap):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)


timmy = Turtle()
turtle.colormode(255)
timmy.speed("fastest")

draw_spirograph(5)

screen = turtle.Screen()
screen.exitonclick()
