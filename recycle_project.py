import pygame
import random

images = ["pencil.png", "cardboard_box.png", "paper_bag.jpeg"]

pygame.init()
screen = pygame.display.set_mode((600,600))

background = pygame.image.load("images/Glass_bg.jpeg")
background = pygame.transform.scale(background, (600,600))

class Bin(pygame.sprite.Sprite):

    def __init__(self,x,y):
        super().__init__()


        self.image = pygame.image.load("images/trash_can.jpeg")
        self.image = pygame.transform.scale(self.image, (70,70))
        self.rect = self.image.get_rect()
        self.rect.center = [x,y]
        self.speed = 4

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

bin = Bin(300,300)

class Recyclable(pygame.sprite.Sprite):

     def __init__(self,x,y):
            super().__init__()

            self.image = pygame.image.load("images/"+random.choice(images))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y


            

recyclable = Recyclable(random.randint(50,550), random.randint(50,550))

recyclable_group = pygame.sprite.Group()
recyclable_group.add(recyclable)

class Nonrecyclable(pygame.sprite.Sprite):
    
     def __init__(self,x,y):
            super().__init__()

    

Bin_group = pygame.sprite.Group()
Bin_group.add(bin)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(background, (0,0))
    Bin_group.draw(screen)
    Bin_group.update()
    recyclable_group.draw(screen)
    
    
    
    
    pygame.display.update()
    

    