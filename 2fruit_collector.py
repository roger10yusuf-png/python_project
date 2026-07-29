import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

background = pygame.image.load("images/fruitsy.png")
background = pygame.transform.scale(background, (800,600))

fruit_names = ["images/strawberry.png", "images/banana.png", "images/orange.png"]

font = pygame.font.SysFont("arial", 40)

score = 0

class Basket(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("basket.png")
        self.image = pygame.transform.scale(self.image, (250,150))
        self.rect = self.image.get_rect()
        self.rect.center = [200,525]
        self.speed = 8

    def update(self):

        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rect.x -= self.speed

        if keys[pygame.K_d]:
            self.rect.x += self.speed


class Fruit(pygame.sprite.Sprite):

    def __init__(self,fruit_images):
        super().__init__()

        self.image = pygame.image.load(fruit_images)
        self.rect = self.image.get_rect()

        self.rect.x = random.randint(0, 800 - 50)
        self.rect.y = 0

    def update(self):
        self.rect.y += 4



    

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
    if currenttime - lasttime > 500:
        fruit = Fruit(random.choice(fruit_names))
        fruit_group.add(fruit)
        lasttime = currenttime
    fruit_group.update()
    fruit_group.draw(screen)
    basket_group.draw(screen)
    basket_group.update()


    pygame.display.update()

