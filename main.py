from turtle import Turtle, Screen
import random
import turtle as turtle_module
from extract_colors import color_list
screen = Screen()
tom = Turtle()
turtle_module.colormode(255)
tom.hideturtle()
tom.speed("fastest")
screen.screensize()


def draw_dots(colors):
    for _ in range(10):
        tom.color(random.choice(colors))
        tom.dot(20)
        tom.penup()
        tom.forward(50)
        tom.pendown()


x = -300
y = -200
tom.teleport(x, y)
for _ in range(10):
    draw_dots(color_list)
    y += 50
    tom.teleport(x, y)


screen.exitonclick()
