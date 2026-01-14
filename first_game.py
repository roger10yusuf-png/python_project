import pgzrun
TITLE = "My Game"
HEIGHT = 343
WIDTH = 600
jerry = Actor("jerry")
jerry.pos = (100,300)
def draw():
    screen.blit("landscape1",(0,0))
    jerry.draw()

pgzrun.go()
