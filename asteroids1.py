import pygame
import random

pygame.init()

screen = pygame.display.set_mode((600,600))
background = pygame.image.load("images/space_background2.png")

'''
class Asteroid():
'''
   









while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
          pygame.quit()
    screen.blit(background, (0,0))



    pygame.display.update()