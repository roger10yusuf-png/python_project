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
    if score < 0:
         screen.blit("game_over.png",(150,50)) 
         return   
    screen.blit("grass.jpeg",(0,0))
    basket.draw()
    for fruit in fruit_list:
         fruit.draw()
    for bomb in bomb_list:
         bomb.draw()
    screen.draw.text("score:"+str(score),center = (50,10))
score = 0

fruits = ["pear_fruit","banana","strawberry","orange"]

fruit_list = []
bomb_list = []

def new_fruits():  
        fruit = Actor(random.choice(fruits))
        fruit.x = random.randint(10,590)
        fruit.y = 10
        fruit_list.append(fruit)
        clock.schedule(new_fruits,random.randint(1,2))

def imp_bomb():
     bomb =  Actor("bomb")
     bomb.x = random.randint(10,590)
     bomb.y = 10
     bomb_list.append(bomb)
     clock.schedule(imp_bomb,random.randint(8,9))

def update():
    global score
    if score < 0:
         return   
    if keyboard.a:
        basket.x += -2.5
    elif keyboard.d:
        basket.x += 2.5
    for fruit in fruit_list:
         fruit.y += 2.5
         if fruit.colliderect(basket):
                fruit_list.remove(fruit)
                score = score + 1
         elif fruit.y >= 399:
                fruit_list.remove(fruit)
    for bomb in bomb_list:
         bomb.y += 2.5
         if bomb.colliderect(basket):
                bomb_list.remove(bomb)
                score = score - 1

            
        
new_fruits()
imp_bomb()

    


    



pgzrun.go()

