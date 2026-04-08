import pgzrun
import random

HEIGHT = 600
WIDTH = 600

player_spacecraft = Actor("player_spaceship")
player_spacecraft.y = 550
player_spacecraft.x = 300

enemy_spaceships = []
player_bullets = []
enemy_bullets = []

def new_enemy_bullet():
       enemy_bullet = Actor("enemy_bullet")
       enemy_spaceship = random.choice(enemy_spaceships)
       enemy_bullet.x = enemy_spaceship.x
       enemy_bullet.y = enemy_spaceship.y
       enemy_bullets.append(enemy_bullet)
       clock.schedule(new_enemy_bullet,1)
      
def enemies():
       for i in range(5):
             enemy_spacecraft = Actor("enemy_spaceship")
             enemy_spacecraft.x = i * 120 + 60
             enemy_spacecraft.y = 50
             enemy_spaceships.append(enemy_spacecraft)
            

enemies()

new_enemy_bullet()

def draw():
    screen.blit("space_background2",(0,0))
    player_spacecraft.draw()
    for bullet in player_bullets:
       bullet.draw()
    for enemy_spacecraft in enemy_spaceships:
          enemy_spacecraft.draw()
    for enemy_bullet in enemy_bullets:
          enemy_bullet.draw()



def update():
    if keyboard.a and player_spacecraft.x >= 50:
     player_spacecraft.x -= 5
    elif keyboard.d and player_spacecraft.x <= 550:
       player_spacecraft.x += 5 
    for bullet in player_bullets:
       bullet.y -= 5
       for enemy_spacecraft in enemy_spaceships:
             if bullet.colliderect(enemy_spacecraft):
                   enemy_spaceships.remove(enemy_spacecraft)
                   player_bullets.remove(bullet)
    for enemy_bullet in enemy_bullets:
          enemy_bullet.y += 5

             
    for enemy_spacecraft in enemy_spaceships:
          enemy_spacecraft.y += 1
    
def on_key_down(key):
   if key == keys.SPACE:
        bullet = Actor("player_bullet")
        bullet.x = player_spacecraft.x
        bullet.y = player_spacecraft.y
        player_bullets.append(bullet)


        















pgzrun.go()