import pygame

pygame.init()

bullets1 = []
bullets2 = []

screen = pygame.display.set_mode((700,700))

bg_image = pygame.image.load("images/space_background2.png")

class Player1():
    def __init__(self,x1,y1):
        self.image = pygame.image.load("images/player_spaceship.png")
        self.x1 = x1
        self.y1 = y1

    
    def draw(self):
        screen.blit(self.image,(self.x1,self.y1))
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x1 -= 2.5
        elif key[pygame.K_d]:
            self.x1 += 2.5
        elif key[pygame.K_SPACE]:
            bullet1 = Bullet1(self.x1 + 30, self.y1)
            bullets1.append(bullet1)

player1 = Player1(315,600)


class Player2():
    def __init__(self,x2,y2):
        self.image = pygame.image.load("images/enemy_spaceship.png")
        self.x2 = x2
        self.y2 = y2
    
    def draw(self):
        screen.blit(self.image,(self.x2,self.y2))
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.x2 -= 2.5
        elif key[pygame.K_RIGHT]:
            self.x2 += 2.5
        elif key[pygame.K_w]:
            bullet2 = Bullet2(self.x2 + 30, self.y2)
            bullets2.append(bullet2)




player2 = Player2(315,100)



class Bullet1():
    def __init__(self,x,y):
        self.image = pygame.image.load("images/player_bullet.png")
        self.x = x
        self.y = y
    
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def update(self):
            self.y -= 2.0


class Bullet2():
    def __init__(self,x,y):
        self.image = pygame.image.load("images/enemy_bullet.png")
        self.x = x
        self.y = y

    def draw(self):
            screen.blit(self.image,(self.x,self.y))
    def update(self):
            self.y += 2.0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg_image,(0,0))
    player1.draw()
    player1.update()
    player2.draw()
    player2.update()
    for bullet in bullets1:
        bullet.draw()
        bullet.update()
    for bullet in bullets2:
        bullet.draw()
        bullet.update()
        
    pygame.display.update()


            
