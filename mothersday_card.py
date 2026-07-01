import pygame

pygame.init()

screen = pygame.display.set_mode((497,698))

image = pygame.image.load("images/mothersdaycard.jpg")

image2 = pygame.image.load("images/heart.png")

font = pygame.font.SysFont("arial",20)

y = 404

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.blit(image,(0,0))
    text = font.render("HAPPY MOTHERSDAY!", True,(0,0,0))
    screen.blit(text,(25,200))
    screen.blit(image2,(10,y))
    y = y-3
    pygame.display.update()