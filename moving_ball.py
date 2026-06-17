import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("green")

pygame.display.update()

class Ball():
    def __init__(self,color,pos,radius,width):
        self.color = color
        self.pos = pos
        self.radius = radius
        self.width = width
        self.screen = screen

    def draw(self):
        pygame.draw.circle(self.screen,self.color,self.pos,self.radius,self.width)

    def update(self):
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.pos[0] += 1


ball1 = Ball("blue",[300,300],25,0)
        
while True:
    screen.fill("green")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    ball1.draw()
    ball1.update()
    pygame.display.update()

