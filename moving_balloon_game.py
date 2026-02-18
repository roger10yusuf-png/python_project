import pgzrun
import random

WIDTH = 600
HEIGHT = 300

mickey_mouse = Actor("mickey_mouse")
balloon = Actor("balloon.png")

def draw():
    screen.blit("disney_landscape.jpg",(0,0))
    mickey_mouse.draw()
    balloon.draw()
    screen.draw.text("score:"+str(score),center = (50,10))
score = 0

def update():
    global score
    if keyboard.d:
        mickey_mouse.x += 5
    elif keyboard.a:
        mickey_mouse.x += -5
    elif keyboard.w:
        mickey_mouse.y += -5
    elif keyboard.s:
        mickey_mouse.y += 5
    if balloon.colliderect(mickey_mouse):
        score = score +1
        balloon.x = random.randint(50,550)
        balloon.y = random.randint(50,250)
    

def moving_balloon():
    balloon.x += random.randint(-75,75)
    balloon.y += random.randint(-75,75)
    if balloon.x >= WIDTH or balloon.y  >= HEIGHT or balloon.x <= 0 or balloon.y <= 0:
        balloon.x = random.randint(50,550)
        balloon.y = random.randint(50,250)
    clock.schedule(moving_balloon, 0.1)
moving_balloon()


pgzrun.go()