import pgzrun
import random

WIDTH = 700
HEIGHT = 525

mario = Actor("mario")

mario.x = 40
mario.y = 400

obstacles = ["plant_obstacle","spikeball_obstacle","spike_obstacle"]
obstacle_list = []

def new_obstacles():
    obstacle = Actor(random.choice(obstacles))
    obstacle.x = 660
    obstacle.y = 420
    obstacle_list.append(obstacle)
    clock.schedule(new_obstacles,(random.randint(1,2)))

new_obstacles()
    

def draw():
    screen.blit("obstacle_game_bg",(0,0))
    mario.draw()
    for obstacle in obstacle_list:
         obstacle.draw()

def on_key_down(key):
    if key == keys.SPACE and mario.y >= 370:
        mario.y += -50


def update():
     if mario.y <= 400:
        mario.y += 1
     for obstacle in obstacle_list:
        obstacle.y = 420
        obstacle.x += -5
     
    
            














pgzrun.go()
