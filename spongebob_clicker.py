import pgzrun
import random
HEIGHT = 343
WIDTH = 600
spongebob = Actor("spongebob")
spongebob.pos = (100,300)
def draw():
    screen.blit("landscape1",(0,0))
    spongebob.draw()
def on_mouse_down(pos):
    if spongebob.collidepoint(pos):
        spongebob.x = (random.randint(0,600))
        spongebob.y = (random.randint(0,343))
pgzrun.go()