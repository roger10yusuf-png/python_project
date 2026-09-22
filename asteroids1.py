import pygame
import random
import time

pygame.init()

font = pygame.font.SysFont("bold", 70)
font1 = pygame.font.SysFont("bold", 40)

screen = pygame.display.set_mode((600,600))
background = pygame.image.load("images/space_background2.png")

asteroids = ["asteroid1.png", "asteroid2.png", "asteroid3.png"]
spaceships = ["player_spaceship.png", "player_spaceship2.png"]

class Asteroid(pygame.sprite.Sprite):
   
    def __init__(self,x,y):
        super().__init__()

        self.image = pygame.image.load("images/"+random.choice(asteroids))
        self.image = pygame.transform.scale(self.image, (100,100))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 3

    def update(self):
          self.rect.y += self.speed
  

asteroid_group = pygame.sprite.Group()


class Spaceship(pygame.sprite.Sprite):
    def __init__(self,x,y):
      super().__init__()

      self.lives = 5

      self.image = pygame.image.load("images/"+random.choice(spaceships))
      self.rect = self.image.get_rect()
      self.rect.x = x
      self.rect.y = y
      self.speed = 2

    def update(self):
        Keys = pygame.key.get_pressed()
        if Keys[pygame.K_w]:
            self.rect.y -= self.speed
        elif Keys[pygame.K_a]:
            self.rect.x -= self.speed
        elif Keys[pygame.K_d]:
            self.rect.x += self.speed
        elif Keys[pygame.K_s]:
            self.rect.y += self.speed
        collide = pygame.sprite.spritecollide(self, asteroid_group, True)
        if collide:
              self.lives = self.lives - 1

spaceship = Spaceship(270,270)      

spaceship_group = pygame.sprite.Group()
spaceship_group.add(spaceship)

currenttime = pygame.time.get_ticks()
lasttime = pygame.time.get_ticks()

clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
    screen.blit(background, (0,0))
    spaceship_group.draw(screen)
    spaceship_group.update()
    asteroid_group.draw(screen)
    asteroid_group.update()
    if currenttime - lasttime > 750:
        asteroid = Asteroid(random.randint(50,500),10)     
        asteroid_group.add(asteroid)
        lasttime = currenttime
    currenttime = pygame.time.get_ticks()
    text1 = font1.render("your lives: "+str(spaceship.lives), True, (255,255,255))
    screen.blit(text1, (425,15))
    if spaceship.lives <= 0:
        text = font.render("GAME OVER", True, (255,255,255))
        screen.blit(text, (170,250))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()



    pygame.display.update()