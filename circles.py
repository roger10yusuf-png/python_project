import turtle
import random
import time
pen = turtle.Turtle()
pen.speed(100)
screen = turtle.Screen()
screen.setup(600,600)
turtle.colormode(255)
pen.goto(0,0)


def circles(size):
    pen.color("red")
    pen.begin_fill()
    pen.circle(size)
    pen.end_fill()

size = 0    

for i in range(10):
    size += 15
    circles(size)
    time.sleep(0.25)
    pen.clear()

for i in range(10):
    size -= 10
    circles(size)
    time.sleep(0.25)
    pen.clear()
