import pgzrun

WIDTH = 600
HEIGHT = 450

basket = Actor("basket")
basket.x = 300
basket.y = 350
pear = Actor("pear_fruit")

def draw():
    basket.draw()
    pear.draw()



pgzrun.go()

