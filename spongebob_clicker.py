import pgzrun
import random
HEIGHT = 343
WIDTH = 600
spongebob = Actor("spongebob")
spongebob.pos = (100,250)
patrick = Actor("patrick_star")
patrick.pos = (220,250)
def draw():
    screen.blit("landscape1",(0,0))
    spongebob.draw()
    patrick.draw()
def on_mouse_down(pos):
    if spongebob.collidepoint(pos):
        spongebob.x = (random.randint(0,600))
        spongebob.y = (random.randint(0,343))

    patrick.pos = pos
        
pgzrun.go()                                 