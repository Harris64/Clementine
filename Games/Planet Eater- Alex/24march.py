import pygame #import pygame
pygame.init() #initialises pygame
from pygame.locals import * #imports additional pygame modules which are seen as not usually needed

import random #imports random module to allow for randrange and randint

width=440 #set width of screen for future use
height=400 #set height of screen for future use

window = pygame.display.set_mode((440,400)) #sets window size to 440 pixels wide, 400 pixels high

background = pygame.image.load('OUTERSPACE.jpg') #gives the background image
font = pygame.font.Font(None, 36)
pygame.display.set_caption("Score: 0            Planet eater!") #displays captions/title for game
clock = pygame.time.Clock()

MOVEX = 100 #position of rectangle
MOVEY = 300 #position of rectangle
rectDirectX=5 #this is the direction and speed of rectangle1 (first enemy)
rectDirectY=3 #direction of first enemy in y co-ords
rectDirectXtwo=4 #direction of 2nd enemy it will travel this plus MOVEXenemytwo variable so it will move and bounce around screen
rectDirectYtwo=6 #y direction of 2nd enemy

MOVEXenemytwo=300 #second enemy variables which represents X value
MOVEYenemytwo=150 #this represents second enemies Y position

score = []# score = 0 but goes up 1 when player collects gold sprite

grey=(120,255,84) #grey colour
black = (0,0,0) #black colour
white=(255,255,255) #white colour
gold = (218,165,32) #gold colour
red= (255,20,10) #red colour

pygame.mixer.music.load('menusound.mp3') #loads music file to play
pygame.mixer.music.play(-1,0.0) #plays music, -1 means loop song infinitely, 0.0 is where from song should it start
direc1, direc2 = 0,0 #direction1 is x, direction2 is y, used to monitor where shape will go if keyboard keys pressed


    

class Sprite(pygame.sprite.Sprite): #creates class named sprite

    def __init__(self,x,y,width,height): #self is reference used to objects attributes

        self.x =x #x is equal to x co-ordinate
        self.y =y #y is equal to y co-ordinate#

        self.width = width #self.width is equal to width when it comes to applying it to objects inside the class
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
        

    def renderSprite(self):
        pygame.draw.rect(window,grey,(self.x,self.y,self.width, self.height)) #this function renders the class and draws and rectangle with the attributes found in the class
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height) #converts rectangle to one PYGAME can use



class Sprite2(pygame.sprite.Sprite): #creates class named sprite with base class used to specify game objects

    def __init__(self,x,y,width,height): #self is reference used to objects attributes

        self.x =x #contains the x co-ordinates of sprite2 (brown)
        self.y =y #contains y 

        self.width = width
        self.height = height
        
        self.rect = pygame.Rect(x, y, width, height)

    def resetPos(self):
        self.rect.x = random.randrange(0, width)
        
    

        
    def renderSprite2(self):

        pygame.draw.rect(window, gold,(self.x, self.y, self.width, self.height))

##GoldSprite=pygame.sprite.Group()
##GoldSprite.add(Sprite2)
##GoldSprite.add(Sprite)

##class Sprite3(pygame.sprite.Sprite): #enemy sprite
##    def __init__(self,x,y,width,height):
##        self.x = x
##        self.y = y
##        self.width = width
##        self.height = height
##        self.rect = pygame.Rect(x, y, width, height)
##
##    
##
##    def renderSprite3(self):
##        pygame.draw.rect(window, red,(MOVEX, MOVEY, 20, 20))
##        self.rect = pygame.Rect(MOVEX, MOVEY, self.width, self.height)

class Sprite4(pygame.sprite.Sprite): #enemy sprite 2nd, supposed to look and act same as first enemy sprite
    def __init__(self,MOVEXenemytwo,MOVEYenemytwo,width,height):
        self.MOVEXenemytwo = MOVEXenemytwo #x position of 2nd enemy
        self.MOVEYenemytwo = MOVEYenemytwo #y position of 2nd enemy
        self.width = width
        self.height = height
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, width, height)

    

    def renderSprite4(self):
        pygame.draw.rect(window, red,(MOVEXenemytwo, MOVEYenemytwo, 30, 20))
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, self.width, self.height)
        

Sprite1=Sprite(20,35,15,14)#player sprite is 200 pixels across and 250 pixels down at starting point, 15 pixels wide, 14 high

Spritetwo=Sprite2(105,200,15,14) #Score sprite, 105 across, 200 pixels down, 15 pixels wide, 14 pixels high
Spritethree=Sprite3(100,200,20,20)
Spritefour=Sprite4(200,172,30,15)


playerScore=pygame.sprite.collide_rect(Sprite1, Spritetwo)

pygame.display.flip()

gameLoop = True #variable is continuing loop so program events inside can continously be used and played
    

while gameLoop: #while loop will contain if and for statements
    if pygame.sprite.collide_rect(Sprite1, Spritethree): #sprite collides with enemy
        pygame.quit()
        break
    if pygame.sprite.collide_rect(Sprite1, Spritefour):
        pygame.quit()
        break
    
    
    for event in pygame.event.get():
        if (event.type==pygame.QUIT): #if pygame quits gameLoop is false and program ends
            gameLoop= False


        if (event.type==pygame.KEYDOWN): #what happens when player has key down

            if (event.key==pygame.K_LEFT): #go left x axis, -5, because getting closer to left

                direc1 = -4

            if (event.key==pygame.K_RIGHT): #go right x axis, 5, because adding 5 closer to right

                direc1= 4

            if (event.key==pygame.K_DOWN): #go down y axis, 5, 
                direc2 = 4

            if (event.key==pygame.K_UP): #go up 
                direc2 = -4

            if (event.key==pygame.K_ESCAPE):
                pygame.quit() #when escape button pressed, game closes

            if direc1 > 440:
                pygame.quit()
            elif direc2 > 400:
                pygame.quit()

                
        if (event.type==pygame.KEYUP): #keyup when player doesnt have fingers on keys

            if (event.key==pygame.K_LEFT): #left is 0 as player is no touching key buttons
                direc1 = 0
            if (event.key==pygame.K_RIGHT): #right is 0 as player is no touching key buttons so position doesnt change
                direc1 = 0
            if (event.key==pygame.K_UP): #up is 0 as player is no touching key buttons
                direc2 = 0
            if (event.key==pygame.K_DOWN): #down is 0 as player is no touching key buttons
                direc2 = 0
                
    if pygame.sprite.collide_rect(Sprite1, Spritetwo):
        Spritetwo=random.randint(0,440)
   
    
  
        

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
    

##    if MOVEX >=440: #MOVEX is greater than 440 (width of screen) then set MOVEX to 0 so it doesnt go off screen
##        MOVEX = 440
##        rectDirectX = -5 #rectDirectX = -5 to stop if disappearing from screen by certain pixels
##    elif MOVEX <0:
##        MOVEX = 0
##        rectDirectX = 5
##    elif MOVEY >400:
##        MOVEY = 400
##        rectDirectY = -5
##    elif MOVEY <0:
##        MOVEY = 0
##        rectDirectY = 5
    
    window.fill(black) #fills window with black


    
    Sprite1.x+=direc1 #sprite1 has direc1 (x) co-ords inside it
    Sprite1.y+=direc2 #sprite1 has direc2 (y) co-ords inside it
    if Sprite1.x  > 440:
        pygame.quit()
        break
    elif Sprite1.y > 400:
        pygame.quit()
        break

    
##    Sprite1.renderSprite() #renders first sprite and enables it to be seen by user
##    Spritetwo.renderSprite2() #renders second sprite and enables it to be seen by user
##    Spritethree.renderSprite3() #defines first enemy
##    Spritefour.renderSprite4() #defines second enemy
##    MOVEX += rectDirectX
##    MOVEY += rectDirectY
##    MOVEXenemytwo += rectDirectXtwo
##    MOVEYenemytwo += rectDirectYtwo
    
    
    
    clock.tick(40) #measures speed of sprite movement

    pygame.display.flip() #this updates the whole window, and performs same function as .update

pygame.quit()







