import pygame, sys,random
from pygame.locals import *

chooseX=random.randint(0, 1000) # random number to be used for the x axis
chooseY=random.randint(0,450) # random number to be used for the y axis

chooseX2=chooseX+169
chooseY2=chooseY+191

x=0
y=0

bgi ="shoot.jpg" #background image
mif ="scope.png" #cursor image
gun ="gun.wav" #gunshot sound
kil = "killer.png"# the target image
mbg="range.jpg" #menu backround 
over="game_over.png"

killed=0 # the variable for the amount of targets hit
missed=0 # the variable for the amount of targets missed


play=0
sound=1

pygame.init()

screen=pygame.display.set_mode((1200,698),0,32)
pygame.display.set_caption("Shooter")


clock = pygame.time.Clock()


orange= (255,128,0)
white=(255,255,255)


Font = pygame.font.Font("freesansbold.ttf", 15)
score = Font.render("Score:"+str(killed),True,orange)
missedText = Font.render("Missed:"+str(missed),True,orange)
playText = Font.render("PLAY",True,orange)
esc=escText = Font.render("Press Escape 'ESC' to return to the main menu",True,orange)
spc=escText = Font.render("Press the space bar to try again!",True,orange)
options = Font.render("OPTIONS",True,orange)
textRectObj = score.get_rect()


titleFont = pygame.font.Font("freesansbold.ttf", 50)
Title = titleFont.render("Shooter!",True,white)

subTitleFont = pygame.font.Font("freesansbold.ttf", 30)
menuHint = subTitleFont.render("Shoot a Target to Select an Option!",True,white)

class shootingGame():

    startBackground=pygame.image.load(mbg).convert()
    background = pygame.image.load(bgi).convert()
    mouse_c = pygame.image.load(mif)
    killer = pygame.image.load(kil)
    gameOver = pygame.image.load(over)


    def gunSound():
        if sound == 1:
            pygame.mixer.music.load(gun) #loads gun file from global variable gun.
            pygame.mixer.music.play(0,0)
    

    while True:
         for event in pygame.event.get():

            
                
            
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
                
            if event.type == pygame.MOUSEBUTTONDOWN and (not(chooseX < x < chooseX2) or not (chooseY < y < chooseY2)): 
                if sound ==1:
                    gunSound()
                missed+=1
                chooseX=random.randint(0, 1000)
                chooseY=random.randint(0,450)
                chooseX2=chooseX+169
                chooseY2=chooseY+191
                
            if event.type == pygame.MOUSEBUTTONDOWN and (chooseX < x < chooseX2) and (chooseY < y < chooseY2): 
                if sound ==1:
                    gunSound()
                killed+=1
                missed=0
                chooseX=random.randint(0, 1000)
                chooseY=random.randint(0,450)
                chooseX2=chooseX+169
                chooseY2=chooseY+191

            score = Font.render("Score:"+str(killed),True,orange)
            missedText = Font.render("Missed:"+str(missed),True,orange)
    
            if play == 0:
                sound=0
                screen.blit(startBackground,(0,0))
                screen.blit(playText,(375,420))
                screen.blit(Title,(500,50))
                screen.blit(menuHint,(345,125))
                if event.type == pygame.MOUSEBUTTONDOWN and (346 < x <445 ) and (274 < y < 400 ):
                    play+=1
                    missed=0
                    killed=0
                    sound+=1
                
    
            x,y = pygame.mouse.get_pos()
            print x,y,play
            
            if play == 1:
                screen.blit(background,(0,0))
                screen.blit(score,(1100,50))
                screen.blit(missedText,(1100,100))
                x,y = pygame.mouse.get_pos()
                screen.blit(killer,(chooseX,chooseY))
                screen.blit(mouse_c,(x-106,y-106))
                
        
                if missed >= 3:
                    play+=1
                    sound=0

            if play == 2:
                screen.blit(gameOver,(-50,0))
                screen.blit(score,(1100,50))
                screen.blit(esc,(400,500))
                screen.blit(spc,(450,520))
                if event.type==pygame.KEYDOWN:
                     if (event.key==pygame.K_ESCAPE):
                        play=0
                        missed=0
                        killed=0
                        
                     if (event.key==pygame.K_SPACE):
                        play=1
                        missed=0
                        killed=0
                        sound+=1
                        
                    
               
            
                
                                
        

            clock.tick(30) 

            pygame.display.update()


    


    

