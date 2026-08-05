import pygame
import random
import time

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load("images/fruitsy.png")
background = pygame.transform.scale(background, (800,600))

game_over_bg = pygame.image.load("images/game_over.png")
game_over_bg = pygame.transform.scale(game_over_bg, (800,600))

fruit_names = ["images/strawberry.png", "images/banana.png", "images/orange.png"]

font = pygame.font.SysFont("arial", 40)

score = 0

class Basket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("basket.png")
        self.image = pygame.transform.scale(self.image, (250,150))
        self.rect = self.image.get_rect()
        self.rect.center = [400,525]
        self.speed = 4

    def update(self):
        global score
        text1 = font.render("your score: "+str(score), True,(0,0,0))
        screen.blit(text1,(10,10))

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed
        
        collide = pygame.sprite.spritecollide(self, fruit_group, True)
        for i in collide:
            score = score + 1
        

lives = 3

class Fruit(pygame.sprite.Sprite):

    def __init__(self,fruit_images):
        super().__init__()

        self.image = pygame.image.load(fruit_images)
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 800 - 50)
        self.rect.y = 0

    def update(self):
        global lives
        self.rect.y += 2.5
        if self.rect.y >= 600:
            lives = lives - 1
            fruit_group.remove(self)
            print(lives)
        text2 = font.render("your lives: "+str(lives), True,(0,0,0))
        screen.blit(text2,(10,55))



    

basket_group = pygame.sprite.Group()
fruit_group = pygame.sprite.Group()

currenttime = pygame.time.get_ticks()
lasttime = pygame.time.get_ticks()

basket = Basket()


basket_group.add(basket)

while True:
    currenttime = pygame.time.get_ticks()
    screen.blit(background, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if currenttime - lasttime > 750:
        fruit = Fruit(random.choice(fruit_names))
        fruit_group.add(fruit)
        lasttime = currenttime
    fruit_group.update()
    fruit_group.draw(screen)
    basket_group.draw(screen)
    basket_group.update()
    if lives <= 0:
        screen.blit(game_over_bg,(0,0))
        pygame.display.update()
        time.sleep(5)
        pygame.quit()
    



    pygame.display.update()

