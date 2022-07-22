from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.shape("turtle")
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
directions = [0, 90, 180, 270]
timmy.pensize(10)
timmy.speed('fastest')

for _ in range(200):
    timmy.color(random.choice(colours))
    angle = random.choice(directions)
    timmy.forward(30)
    timmy.setheading(angle)


screen = Screen()
screen.exitonclick()