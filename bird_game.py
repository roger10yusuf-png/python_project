import pgzrun
import random

WIDTH = 700
HEIGHT = 455

bird = Actor("bird.png")
bird.x = 30
bird.y = 233
bird_hinderance = Actor("pebble")
bird_hinderance.x = 670
bird_hinderance.y = random.randint(30,425)

grains = []

def grain():
    bird_food = Actor("grain")
    bird_food.x = 670
    bird_food.y = random.randint(30,425)
    grains.append(bird_food)
    clock.schedule(grain,random.randint(1,2))
    
grain()

pebbles = []

def pebble():
    bird_hinderance = Actor("pebble")
    bird_hinderance.x = 670
    bird_hinderance.y = random.randint(30,425)
    pebbles.append(bird_hinderance)
    clock.schedule(pebble,random.randint(1,2))

pebble()

score = 0

def draw():
    screen.blit("bird_sky",(0,0))
    bird.draw()
    for bird_food in grains:
        bird_food.draw()
    for bird_hinderance in pebbles:
        bird_hinderance.draw()
    screen.draw.text("score:"+str(score),center = (50,10))

def update():
    global score
    for bird_food in grains:
        bird_food.x -= random.randint(3,6)
    for bird_hinderance in pebbles:
        bird_hinderance.x -= random.randint(3,6)
    if keyboard.w:
        bird.y += -5
    elif keyboard.s:
        bird.y += 5
    for bird_food in grains:
        if bird.colliderect(bird_food):
            score = score +1
            grains.remove(bird_food)
        if bird_food.x <= 0:
            grains.remove(bird_food)
    for bird_hinderance in pebbles:
        if bird.colliderect(bird_hinderance):
            score = score -1
            pebbles.remove(bird_hinderance)
    


    




pgzrun.go()



