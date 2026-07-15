import pygame

pygame.init()

bullets1 = []
bullets2 = []

screen = pygame.display.set_mode((700,700))

bg_image = pygame.image.load("images/space_background2.png")

class Player1(pygame.sprite.Sprite):
    def __init__(self,x1,y1):
        super().__init__()
        self.image = pygame.image.load("images/player_spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x1,y1]
        self.lastshot = pygame.time.get_ticks()
        self.lives = 3 
   
    def update(self):
        currenttime = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 2.5
        elif key[pygame.K_d]:
            self.rect.x += 2.5
        elif key[pygame.K_w] and currenttime - self.lastshot > 500:
            self.lastshot = currenttime
            bullet1 = Bullet1(self.rect.x + 30, self.rect.y)
            bullet1group.add(bullet1) 
            common_group.add(bullet1)
        collide = pygame.sprite.spritecollide(self, bullet2group, True)
        for i in collide:
            self.lives = self.lives - 1
            break
            


class Player2(pygame.sprite.Sprite):
    def __init__(self,x2,y2):
        super().__init__()
        self.image = pygame.image.load("images/enemy_spaceship.png")
        self.rect = self.image.get_rect()
        self.rect.center = [x2,y2]
        self.lastshot = pygame.time.get_ticks()
    
    
    def update(self):
        currenttime = pygame.time.get_ticks()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 2.5
        elif key[pygame.K_RIGHT]:
            self.rect.x += 2.5
        elif key[pygame.K_UP] and currenttime - self.lastshot > 500:
            self.lastshot = currenttime
            bullet2 = Bullet2(self.rect.x + 30, self.rect.y)
            bullet2group.add(bullet2)
            common_group.add(bullet2)






class Bullet1(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/player_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
            self.rect.y -= 2.0


class Bullet2(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.image.load("images/enemy_bullet.png")
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
    def update(self):
            self.rect.y += 2.0

player1 = Player1(315,600)
player2 = Player2(315,100)
common_group = pygame.sprite.Group()
player1group = pygame.sprite.Group()
player2group = pygame.sprite.Group()
bullet1group = pygame.sprite.Group()
bullet2group = pygame.sprite.Group()
common_group.add(player1)
player1group.add(player1)
common_group.add(player2)
player2group.add(player2)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg_image,(0,0))
    player1.update()
    player2.update()
    bullet1group.update()
    bullet2group.update()
    common_group.draw(screen)

    pygame.display.update()


            
