import pgzrun

HEIGHT = 600
WIDTH = 600

player_spacecraft = Actor("player_spaceship")
player_spacecraft.y = 550
player_spacecraft.x = 300

bullets = []
        

def draw():
    screen.blit("space_background2",(0,0))
    player_spacecraft.draw()
    for bullet in bullets:
       bullet.draw()

def update():
    if keyboard.a and player_spacecraft.x >= 50:
     player_spacecraft.x -= 5
    elif keyboard.d and player_spacecraft.x <= 550:
       player_spacecraft.x += 5 
    for bullet in bullets:
       bullet.y -= 5



def on_key_down(key):
   if key == keys.SPACE:
        bullet = Actor("player_bullet")
        bullet.x = player_spacecraft.x
        bullet.y = player_spacecraft.y
        bullets.append(bullet)


        















pgzrun.go()