import pygame #import pygame
pygame.init() #initialises pygame

pygame.font.init()
from pygame.locals import * #imports additional pygame modules which are seen as not usually needed

import random #imports random module to allow for randrange and randint

width=440 #set width of screen for future use
height=400 #set height of screen for future use

window = pygame.display.set_mode((440,400)) #sets window size to 440 pixels wide, 400 pixels high
pygame.display.set_mode((width,height))
GameOver = pygame.image.load('gameover.jpg')
background = pygame.image.load('OUTERSPACE.jpg') #gives the background image
pygame.display.set_caption("Planet eater!") #displays captions/title for game
START=pygame.image.load("startscreen.jpg")
clock = pygame.time.Clock()

MOVEX = 100 #position of rectangle

MOVEY = 300 #position of rectangle

rectDirectX=5 #this is the direction and speed of rectangle1 (first enemy)

rectDirectY=3 #direction of first enemy in y co-ords

rectDirectXtwo=4 #direction of 2nd enemy it will travel this plus MOVEXenemytwo variable so it will move and bounce around screen
rectDirectYtwo=6 #y direction of 2nd enemy
MOVEXenemytwo=230 #second enemy variables which represents X value
MOVEYenemytwo=150 #this represents second enemies Y position

game=0

MOVEXenemythree=200
MOVEYenemythree=90
rectDirectXthree=9
rectDirectYthree=8

score = 0# score = 0 but goes up 1 when player collects gold sprite

grey=(120,255,84) #grey colour
black = (0,0,0) #black colour
white=(255,255,255) #white colour
gold = (218,165,32) #gold colour
red= (255,20,10) #red colour

pygame.mixer.music.load('menusound.mp3') #loads music file to play
pygame.mixer.music.play(-1,0.0) #plays music, -1 means loop song infinitely, 0.0 is where from song should it start
direc1, direc2 = 0,0 #direction1 is x, direction2 is y, used to monitor where shape will go if keyboard keys pressed



class Sprite(pygame.sprite.Sprite): #creates class named sprite

    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self) #self is reference used to objects attributes

        self.x =x #x is equal to x co-ordinate
        self.y =y #y is equal to y co-ordinate#

        self.width = width #self.width is equal to width when it comes to applying it to objects inside the class
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        

    def renderSprite(self):
        pygame.draw.rect(window,grey,(self.x,self.y,self.width, self.height)) #this function renders the class and draws and rectangle with the attributes found in the class
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) #converts rectangle to one PYGAME can use


class Sprite2(pygame.sprite.Sprite): #enemy sprite
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    

    def renderSprite2(self):
        pygame.draw.rect(window, red,(MOVEXenemythree, MOVEYenemythree, 25, 20))
        self.rect = pygame.Rect(MOVEXenemythree, MOVEYenemythree, self.width, self.height)

class Sprite3(pygame.sprite.Sprite): #enemy sprite
    def __init__(self,x,y,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    

    def renderSprite3(self):
        pygame.draw.rect(window, red,(MOVEX, MOVEY, 20, 20))
        self.rect = pygame.Rect(MOVEX, MOVEY, self.width, self.height)

class Sprite4(pygame.sprite.Sprite): #enemy sprite 2nd, supposed to look and act same as first enemy sprite
    def __init__(self,MOVEXenemytwo,MOVEYenemytwo,width,height):
        pygame.sprite.Sprite.__init__(self)
        self.MOVEXenemytwo = MOVEXenemytwo #x position of 2nd enemy
        self.MOVEYenemytwo = MOVEYenemytwo #y position of 2nd enemy
        self.width = width
        self.height = height
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, width, height)

    

    def renderSprite4(self):
        pygame.draw.rect(window, red,(MOVEXenemytwo, MOVEYenemytwo, 30, 20))
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, self.width, self.height)
        

Sprite1=Sprite(20,35,15,14)#player sprite is 200 pixels across and 250 pixels down at starting point, 15 pixels wide, 14 high

Spritetwo=Sprite2(105,200,15,14) 
Spritethree=Sprite3(100,200,20,20)
Spritefour=Sprite4(200,172,30,15)



##-SCORE CODE-##
fonts = pygame.font.SysFont("freesansbold.ttf",12)
GameScore= fonts.render("Score: "+str(score),False,white)
textRectObj = GameScore.get_rect()

gameLoop = True #variable is continuing loop so program events inside can continously be used and played
    

while gameLoop: #while loop will contain if and for statements
    

    
        
    
    
    for event in pygame.event.get():
        if (event.type==pygame.QUIT): #if pygame quits gameLoop is false and program ends
            gameLoop= False


        if (event.type==pygame.KEYDOWN): #what happens when player has key down

            if (event.key==pygame.K_LEFT): #go left x axis, -5, because getting closer to left

                direc1 = -4
                score+=1
                GameScore= fonts.render("Score: "+str(score),True,white)

            if (event.key==pygame.K_RIGHT): #go right x axis, 5, because adding 5 closer to right

                direc1= 4
                score+=1
                GameScore= fonts.render("Score: "+str(score),True,white)

            if (event.key==pygame.K_DOWN): #go down y axis, 5, 
                direc2 = 4
                score+=1
                GameScore= fonts.render("Score: "+str(score),True,white)

            if (event.key==pygame.K_UP): #go up 
                direc2 = -4
                score+=1
                GameScore= fonts.render("Score: "+str(score),True,white)

            if (event.key==pygame.K_ESCAPE):
                pygame.quit() #when escape button pressed, game closes

            if (event.key==pygame.K_p): #if user presses p
                pygame.time.wait(3000) #if user presses p the pygame program will wait a certain amount of milliseconds
                #3000 milliseconds is equal to 3 seconds
                        
        if (event.type==pygame.KEYUP): #keyup when player doesnt have fingers on keys

            if (event.key==pygame.K_LEFT): #left is 0 as player is no touching key buttons
                direc1 = 0
            if (event.key==pygame.K_RIGHT): #right is 0 as player is no touching key buttons so position doesnt change
                direc1 = 0
            if (event.key==pygame.K_UP): #up is 0 as player is no touching key buttons
                direc2 = 0
            if (event.key==pygame.K_DOWN): #down is 0 as player is no touching key buttons
                direc2 = 0
                        

            
   
    if MOVEXenemythree > 420:
        MOVEXenemythree = 420
        rectDirectXthree = -3
    elif MOVEXenemythree < 0:
        MOVEXenemythree = 0
        rectDirectXthree = 5
    elif MOVEYenemythree > 400:
        MOVEYenemythree = 395
        rectDirectYthree = - 4
    elif MOVEYenemythree < 0:
        MOVEYenemythree = 0
        rectDirectYthree = 6
  
        

    if MOVEXenemytwo > 440:
        MOVEXenemytwo = 440
        rectDirectXtwo= -4
    elif MOVEXenemytwo < 0:
        MOVEXenemytwo = 0
        rectDirectXtwo = 4
    elif MOVEYenemytwo > 400:
        MOVEYenemytwo = 400
        rectDirectYtwo = -4
    elif MOVEYenemytwo < 0:
        MOVEYenemytwo = 0
    

    if MOVEX >=440: #MOVEX is greater than 440 (width of screen) then set MOVEX to 0 so it doesnt go off screen
        MOVEX = 440
        rectDirectX = -5 #rectDirectX = -5 to stop if disappearing from screen by certain pixels
    elif MOVEX <0:
        MOVEX = 0
        rectDirectX = 5
    elif MOVEY >400:
        MOVEY = 400
        rectDirectY = -5
    elif MOVEY <0:
        MOVEY = 0
        rectDirectY = 5

    pygame.display.update()


    if game==0:
        window.blit(START,(0,0))
        
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game+=1

    if game==1:
        window.blit(background,(0,0))
        Sprite1.renderSprite() #renders first sprite and enables it to be seen by user
        Spritetwo.renderSprite2() #defines enemy
        Spritethree.renderSprite3() #defines first enemy
        Spritefour.renderSprite4() #defines second enemy
        MOVEX += rectDirectX
        MOVEY += rectDirectY
        MOVEXenemytwo += rectDirectXtwo
        MOVEYenemytwo += rectDirectYtwo
        MOVEXenemythree += rectDirectXthree
        MOVEYenemythree += rectDirectYthree
        Sprite1.x+=direc1 #sprite1 has direc1 (x) co-ords inside it
        Sprite1.y+=direc2 #sprite1 has direc2 (y) co-ords inside it

    if Sprite1.x  > 440:
        game+=1

    elif Sprite1.x <0:
        game+=1
        
    elif Sprite1.y > 400:
        game+=1
        
    elif Sprite1 < 0:
        game+=1

    if pygame.sprite.collide_rect(Sprite1, Spritethree): #sprite collides with enemy
        game+=1
    if pygame.sprite.collide_rect(Sprite1, Spritefour):
        game+=1

    if pygame.sprite.collide_rect(Sprite1,Spritetwo):
        game+=1
        

    if pygame.sprite.collide_rect(Sprite1,Spritetwo):
        game+=1
        

    if game==2:
        window.blit(GameOver,(0,0))
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_SPACE:
                game=0

    
    
##    window.fill(black) #fills window with black


    
    
    
    

    
    
    
    

    
    
    
    
    clock.tick(40) #measures speed of sprite movement

    pygame.display.flip() #this updates the whole window, and performs same function as .update




#play = 0
    #if play == 0:
    #window.blit(


