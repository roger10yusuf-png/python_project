import pgzrun
import random

WIDTH = 600
HEIGHT = 399

basket = Actor("basket")
basket.x = 300
basket.y = 350
pear = Actor("pear_fruit")
banana = Actor("banana")



def draw():
    screen.blit("grass.jpeg",(0,0))
    basket.draw()
    for fruit in fruit_list:
         fruit.draw()

fruits = ["pear_fruit","banana","strawberry","orange"]

fruit_list = []

score = 0

def new_fruits():  
        fruit = Actor(random.choice(fruits))
        fruit.x = random.randint(10,590)
        fruit.y = 10
        fruit_list.append(fruit)
        clock.schedule(new_fruits,random.randint(1,2))

def update():
    global score
    if keyboard.a:
        basket.x += -2.5
    elif keyboard.d:
        basket.x += 2.5
    for fruit in fruit_list:
         fruit.y += 2.5
         if fruit.colliderect(basket):
                fruit_list.remove(fruit)
         elif fruit.y >= 399:
                fruit_list.remove(fruit)
        


new_fruits()

    


    



pgzrun.go()

