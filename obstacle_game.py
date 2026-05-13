import pgzrun
import random

WIDTH = 700
HEIGHT = 525

mario = Actor("mario")

mario.x = 40
mario.y = 400

lives = 3
score = 0

obstacles = ["plant_obstacle","spikeball_obstacle","spike_obstacle"]
obstacle_list = []

def new_obstacles():
    obstacle = Actor(random.choice(obstacles))
    obstacle.x = 660
    obstacle.y = 420
    obstacle_list.append(obstacle)
    clock.schedule(new_obstacles,(random.randint(3,5)))

new_obstacles()
    
lives_list = []

def new_lives():
     live = Actor("mario_live")
     lives_list.append(live)
     live.x = 660
     live.y = 420
     clock.schedule(new_lives,random.randint(120,200))
clock.schedule(new_lives,random.randint(120,200))



def draw():
    global lives
    global score
    screen.blit("obstacle_game_bg",(0,0))
    if lives <= 0:
         screen.blit("mario_game_over_screen",(0,0)) 
         return   
    mario.draw()
    for obstacle in obstacle_list:
         obstacle.draw()
    for live in lives_list:
          live.draw()
    screen.draw.text("lives:"+str(lives),center = (50,10))
    screen.draw.text("score:"+str(score),center = (50,25))




def on_key_down(key):
    if key == keys.SPACE and mario.y == 400:
        mario.y += -180


def update():
     global lives
     global score
     if lives < 0:
            
             return   
     if mario.y < 400:
        mario.y += 2
     for obstacle in obstacle_list:
        obstacle.y = 420
        obstacle.x += -2
        if mario.colliderect(obstacle):
            lives = lives - 1
            obstacle_list.remove(obstacle)
        if obstacle.x < 0:
            obstacle_list.remove(obstacle)
            score = score + 1
     for live in lives_list:
            live.x += -2
            if mario.colliderect(live):
                 lives = lives + 1
                 lives_list.remove(live)
    
     
                    
            
  
        
     
    
            














pgzrun.go()
