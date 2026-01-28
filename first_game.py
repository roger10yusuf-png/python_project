import pgzrun
TITLE = "My Game"
HEIGHT = 343
WIDTH = 600
jerry = Actor("jerry")
jerry.pos = (100,280)

tom = Actor("angry_tom")
tom.pos = (185,280)

def draw():
    screen.blit("landscape1",(0,0))
    jerry.draw()
    tom.draw()

pgzrun.go()
