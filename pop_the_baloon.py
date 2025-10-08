import turtle
import random

screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("skyblue")
triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.up()
triangle.goto(0,-280)
triangle.left(90)

def move_left():
    left = triangle.xcor() -10
    triangle.setx(left)
def move_right():
    right = triangle.xcor() +10
    triangle.setx(right)

screen.listen()
screen.onkey(move_left,"a")
screen.onkey(move_right,"d")
turtle.exitonclick()






