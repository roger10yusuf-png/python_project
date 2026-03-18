import pgzrun
import random

WIDTH = 700
HEIGHT = 455

bird = Actor("bird.png")
bird.x = 30
bird.y = 233
bird_food = Actor("grain")
bird_food.x = 670
bird_food.y = random.randint(30,425)
pebbles = Actor("pebbles")

grains = []

def grain():
    bird_food = Actor("grain")
    bird_food.x = 670
    bird_food.y = random.randint(30,425)
    grains.append(bird_food)
    clock.schedule(grain,3)
    
grain()

def draw():
    screen.blit("bird_sky",(0,0))
    bird.draw()
    for bird_food in grains:
        bird_food.draw()
    pebbles.draw()

def update():
    for bird_food in grains:
        bird_food.x -= 5

    




pgzrun.go()



