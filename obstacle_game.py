import pgzrun
import random

WIDTH = 700
HEIGHT = 525

mario = Actor("mario")

mario.x = 40
mario.y = 400

lives = 3
score = 0
time = 10

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

pwr_up_list = []

def power_ups():
     power_up = Actor("mario_power_up")
     pwr_up_list.append(power_up)
     power_up.x = 660
     power_up.y = 420
     clock.schedule(power_ups,random.randint(120,200))
clock.schedule(power_ups,random.randint(120,200))

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
    for power_up in pwr_up_list:
         power_up.draw()
    screen.draw.text("lives:"+str(lives),center = (50,10))
    screen.draw.text("score:"+str(score),center = (50,25))

    if power == 1:
         screen.draw.text("power mode: on",center = (625,20), fontname = "timesnewroman")
         screen.draw.text("time:"+ str(time),center = (625,40))
    elif power == 0:
         screen.draw.text("power mode: off",center = (625,20), fontname = "timesnewroman")

         
         

                 
                 





def on_key_down(key):
    if key == keys.SPACE and mario.y == 400:
        mario.y += -180

power = 0
power_time = -1

def update():
     global lives
     global score
     global power
     global power_time 
     global time    
     if lives < 0:
            
             return   
     if power == 1:
            power_time = power_time + 1
            if power_time % 60 == 0:
                   time -= 1
            if power_time == 600:
                 power = 0
                 power_time = 0
     if mario.y < 400:
        mario.y += 2
     for obstacle in obstacle_list:
        obstacle.y = 420
        obstacle.x += -2
        if mario.colliderect(obstacle) and power == 0:
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
     for power_up in pwr_up_list:
            power_up.x += -2
            if mario.colliderect(power_up):
                 power = 1
                 pwr_up_list.remove(power_up)
               



                 
        
    
     
                    
            
  
        
     
    
            














pgzrun.go()
