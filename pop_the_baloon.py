import turtle
import random
import time
turtle.colormode(255)

screen = turtle.Screen()
screen.setup(600, 600)
screen.bgcolor("skyblue")

triangle = turtle.Turtle()
triangle.shape("triangle")
triangle.color("black")
triangle.penup()
triangle.goto(0, -280)
triangle.setheading(90)

def move_left():
    x = triangle.xcor() - 10
    if x > -290:
        triangle.setx(x)

def move_right():
    x = triangle.xcor() + 10
    if x < 290:
        triangle.setx(x)

screen.listen()
screen.onkey(move_left, "a")
screen.onkey(move_right, "d")

def balloons():
    balloon = turtle.Turtle()
    balloon.hideturtle()
    balloon.shape("circle")
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    balloon.color(r,g,b)
    balloon.penup()
    balloon.goto(random.randint(-280, 280), 280)
    balloon.showturtle()
    return balloon
balloon = balloons()

score = 0
pen = turtle.Turtle()
pen.penup()
pen.hideturtle()
pen.goto(250,250)
pen.write("Score:" + str(score),font = ("arial", 20))
 
while True:
    y = balloon.ycor() -4
    balloon.sety(y)
    if balloon.ycor() <= -280:
     balloon.hideturtle()
     balloon = balloons()
    if balloon.distance(triangle) <= 10:
        balloon.hideturtle()
        score = score + 1
        pen.clear()
        pen.write("Score:" + str(score),font = ("arial", 20))


    



turtle.done()







