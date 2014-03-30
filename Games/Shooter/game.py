import pygame, sys,random
from pygame.locals import *

chooseX=random.randint(0, 1000) # random number to be used for the x axis
chooseY=random.randint(0,450) # random number to be used for the y axis

chooseX2=chooseX+250
chooseY2=chooseY+300

bgi ="shoot.jpg" #background image

mif ="scope.png" #cursor image

gun ="gunshot.wav" #gunshot sound

if chooseY > 250:
    kil ="killer_edited.png"
else:
    kil = "killer.png"

killed=0

pygame.init()
screen=pygame.display.set_mode((1280,720),0,32)
pygame.display.set_caption("Shooter")


#class Menu():
    

class shootingGame():
    
    background=pygame.image.load(bgi).convert()
    mouse_c=pygame.image.load(mif)
    killer=pygame.image.load(kil)

    
    clock = pygame.time.Clock()

    textFont = pygame.font.SysFont("Arial", 15)
   
    def score():
        label = textFont.render("Score:",(255,255,0))
        screen.blit(label, (100, 100))

    def gunSound():
        pygame.mixer.music.load(gun) #loads bang file from global variable gun.
        pygame.mixer.music.play(0,0) 
    
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:# and (chooseX < x < chooseX2) and (chooseY < y < chooseY2): 
                gunSound()
                killed+=1
                print killed
                chooseX=random.randint(0, 1000)
                chooseY=random.randint(0,450)
                

        screen.blit(background,(0,0))

        x,y = pygame.mouse.get_pos()
        x -= mouse_c.get_width()/2
        y -= mouse_c.get_height()/2

        screen.blit(killer,(chooseX,chooseY))
        screen.blit(mouse_c,(x,y))
        pygame.mouse.set_visible(False)

        clock.tick(30) 

        pygame.display.update()

        

shootingGame()
        

