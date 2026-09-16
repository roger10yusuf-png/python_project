import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))
screen.fill("white")

Jordan = pygame.image.load("images/Jumpman_logo.jpeg")
Jordan = pygame.transform.scale(Jordan, (100,100))

Nike = pygame.image.load("images/swoosh.jpg")
Nike = pygame.transform.scale(Nike, (100,100))

PS = pygame.image.load("images/Playstation.jpg")
PS = pygame.transform.scale(PS, (100,100))

apple = pygame.image.load("images/apple.png")
apple = pygame.transform.scale(apple, (100,100))

font = pygame.font.SysFont("arial", 50)
font1 = pygame.font.SysFont("arial", 20)

text2 = font1.render("apple", True,(0,0,0))
text3 = font1.render("Nike", True,(0,0,0))
text4 = font1.render("PS", True,(0,0,0))
text5 = font1.render("Jordan", True,(0,0,0))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (0,0,0), position, 20, 0)
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            position2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, (0,0,0), position, position2, 5)
            pygame.draw.circle(screen, (0,0,0), position2, 20, 0)
            pygame.display.update()


    text1 = font.render("guess the logo ", True,(0,0,0))
    screen.blit(text1,(120,5))
    screen.blit(text2,(10,215))
    screen.blit(text3,(10,105))
    screen.blit(text4,(10,435))
    screen.blit(text5,(10,325))


    screen.blit(Jordan, (500,75))
    screen.blit(Nike, (500,185))
    screen.blit(PS, (500,295))
    screen.blit(apple, (500,405))

   
   
    pygame.display.update()






