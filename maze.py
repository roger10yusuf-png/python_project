import turtle

pen = turtle.Turtle()
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor("green")
maze = ["xxxxxxxxxxxxxxxx",
        "x              x",
        "x xxxxx  x xxxxx",
        "xxxx  x        x",
        "x     x  xx  x x",
        "x xx     x  x  x",
        "xx xxx  x  x   x",
        "x x    x   x   x",
        "x   x x xxxx   x",
        "x x   x    x   x",
        "x x x  x       x",
        "x  x  x  xxxxxxx",
        "xxx  xxx       x",
        "xxxxxxxxxxxxxx f"]
hurdles = []
for y in range(len (maze)):
    for x in range(len(maze[y])):
        if maze [y][x] == "x":
            bricks = turtle.Turtle()
            bricks.shape("square")
            bricks.up()
            bricks.speed(100)
            bricks_x = -288 + (x * 24)
            bricks_y = 288 - (y * 24)
            bricks.goto(bricks_x,bricks_y)
            hurdles.append(bricks)
        elif maze [y][x] == "f":
              food = turtle.Turtle()
              food.shape("circle")
              food.color("orange")
              food.up()
              food_x = -288 + (x * 24)
              food_y = 288 - (y * 24)
              food.goto(food_x,food_y)
                  
def valid_move(x,y):
    for brick in hurdles:
        if brick.xcor() == x and brick.ycor() == y:
            return False
    return True    
         

def up():
      x = pen.xcor()
      y = pen.ycor() + 24
      if valid_move(x,y):
            pen.goto(x,y)


def right():
  x = pen.xcor() + 24
  y = pen.ycor()
  if valid_move(x,y):
            pen.goto(x,y)

def left():
  x = pen.xcor() - 24
  y = pen.ycor()
  if valid_move(x,y):
            pen.goto(x,y)


def down():
  x = pen.xcor()
  y = pen.ycor() - 24
  if valid_move(x,y):
            pen.goto(x,y)
        
screen.listen()    
screen.onkey(up, "Up")
screen.onkey(left, "Left")
screen.onkey(right, "Right")
screen.onkey(down, "Down")

pen.penup()
pen.goto(-264,264)
pen.pendown()

while True:
  if pen.distance(food) <= 10:
        print("you have beat the maze")
        break 
turtle.exitonclick()


 
