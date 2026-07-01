import pygame

pygame.init()

screen = pygame.display.set_mode((700,700))

bg_image = pygame.image.load("images/space_background2.png")

class Player1():
    def __init__(self,x,y):
        self.image = pygame.image.load("images/player_spaceship.png")
        self.x = x
        self.y = y
    
    def draw(self):
        screen.blit(self.image,(self.x,self.y))
    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_a]:
            self.x -= 2.5
        elif key[pygame.K_d]:
            self.x += 2.5



player1 = Player1(315,600)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(bg_image,(0,0))
    player1.draw()
    player1.update()
    pygame.display.update()


            
