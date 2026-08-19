import pygame

pygame.init()

screen = pygame.display.set_mode((600,600))

subway_surfers = pygame.image.load("images/subway_surfers.jpeg")
subway_surfers = pygame.transform.scale(subway_surfers, (100,100))

Geometry_dash = pygame.image.load("images/Geometry_dash.jpeg")
Geometry_dash = pygame.transform.scale(Geometry_dash, (100,100))

Roblox = pygame.image.load("images/Roblox.jpeg")
Roblox = pygame.transform.scale(Roblox, (100,100))

Clash_Royale = pygame.image.load("images/Clash_Royale.jpeg")
Clash_Royale = pygame.transform.scale(Clash_Royale, (100,100))

font = pygame.font.SysFont("arial", 50)
font1 = pygame.font.SysFont("arial", 20)

text2 = font1.render("Roblox", True,(255,255,255))
text3 = font1.render("Clash Royale", True,(255,255,255))
text4 = font1.render("Geometry Dash", True,(255,255,255))
text5 = font1.render("subway surfers", True,(255,255,255))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            position = pygame.mouse.get_pos()
            pygame.draw.circle(screen, (255,255,255), position, 20, 0)
            pygame.display.update()

        elif event.type == pygame.MOUSEBUTTONUP:
            position2 = pygame.mouse.get_pos()
            pygame.draw.line(screen, (255,255,255), position, position2, 5)
            pygame.draw.circle(screen, (255,255,255), position2, 20, 0)
            pygame.display.update()


    text1 = font.render("guess the logo ", True,(255,255,255))
    screen.blit(text1,(120,5))
    screen.blit(text2,(10,215))
    screen.blit(text3,(10,105))
    screen.blit(text4,(10,435))
    screen.blit(text5,(10,325))


    screen.blit(subway_surfers, (500,75))
    screen.blit(Geometry_dash, (500,185))
    screen.blit(Roblox, (500,295))
    screen.blit(Clash_Royale, (500,405))

   
   
    pygame.display.update()






