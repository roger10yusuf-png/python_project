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

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.rect.x -= 2.5
        elif key[pygame.K_d]:
            self.rect.x += 2.5    
\
player1group = pygame.sprite.Group()   
player1 = Player1(315,600)     
player1group.add(player1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg_image,(0,0))
    player1group.draw(screen)
    player1group.update()

    pygame.display.update()
        