import pygame
import sys
import random
from pygame.locals import *

chooseX=random.randint(0, 1000) # random number to be used for the x axis
chooseY=random.randint(0,450) # random number to be used for the y axis

chooseX2=chooseX+250
chooseY2=chooseY+300

bgi ="shoot.jpg" #background image

mif ="scope.png" #cursor image

if chooseY > 250:
    kil ="killer_edited.png"
else:
    kil = "killer.png"



class shootingGame():
    pygame.init()
    screen=pygame.display.set_mode((1280,720),0,32)

    background=pygame.image.load(bgi).convert()
    mouse_c=pygame.image.load(mif)
    killer=pygame.image.load(kil)

    
    #rect = pygame.draw.rect(screen,red,10,10)
    #sprites_clicked = [sprite for sprite in all_my_sprites_list if sprite.rect.collidepoint(x, y)]

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN and (chooseX < x < chooseX2) and (chooseY < y < chooseY2): 
                print chooseX
                print chooseY
                chooseX=random.randint(0, 1000)
                chooseY=random.randint(0,450)
                print pygame.mouse.get_pos()
                print chooseX
                print chooseY

        screen.blit(background,(0,0))

        x,y = pygame.mouse.get_pos()
        x -= mouse_c.get_width()/2
        y -= mouse_c.get_height()/2

        screen.blit(killer,(chooseX,chooseY))
        screen.blit(mouse_c,(x,y))
        pygame.mouse.set_visible(False)
        

        pygame.display.update()

        

shootingGame()
        

