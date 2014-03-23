import pygame #import pygame
pygame.init() #initialises pygame
from pygame.locals import *

import random #imports random module to allow for randrange and randint

width=440 #set width of screen for future use
height=400 #set height of screen for future use

window = pygame.display.set_mode((440,400)) #sets window size to 440 pixels wide, 400 pixels high

background = pygame.image.load('OUTERSPACE.jpg') #gives the background image

pygame.display.set_caption("Planet eater!") #displays captions/title for game
clock = pygame.time.Clock()

MOVEX = 60 #position of rectangle
MOVEY = 30 #position of rectangle
rectDirectX=5 #this is the direction and speed of rectangle
rectDirectY=3

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
        self.y =y #y is equal to y co-ordinate

        self.width = width #self.width is equal to width when it comes to applying it to objects inside the class
        self.height = height
        
        

    def renderSprite(self):
        pygame.draw.rect(window,grey,(self.x,self.y,self.width, self.height)) #this function renders the class and draws and rectangle with the attributes found in the class
        

class Sprite2(pygame.sprite.Sprite): #creates class named sprite with base class used to specify game objects

    def __init__(self,x,y,width,height): #self is reference used to objects attributes

        self.x =x #contains the x co-ordinates of sprite2 (brown)
        self.y =y #contains y 

        self.width = width
        self.height = height
        
        

    def renderSprite2(self):

        pygame.draw.rect(window, gold,(self.x, self.y, self.width, self.height))

class Sprite3(pygame.sprite.Sprite):
    def __init__(self,MOVEX,MOVEY,width,height):
        self.MOVEX = MOVEX
        self.MOVEY = MOVEY
        self.width = width
        self.height = height

    
            


Sprite1=Sprite(20,35,15,14)#player sprite is 200 pixels across and 250 pixels down at starting point, 15 pixels wide, 14 high

Spritetwo=Sprite2(105,200,15,14) #Score sprite, 105 across, 200 pixels down, 15 pixels wide, 14 pixels high





gameLoop = True #variable is continuing loop so program events inside can continously be used and played
while gameLoop: #while loop will contain if and for statements

    for event in pygame.event.get():
        if (event.type==pygame.QUIT): #if pygame quits gameLoop is false and program ends
            gameLoop= False

            
        

        if (event.type==pygame.KEYDOWN): #what happens when player has key down

            if (event.key==pygame.K_LEFT): #go left x axis, -5, because getting closer to left

                direc1 = -5

            if (event.key==pygame.K_RIGHT): #go right x axis, 5, because adding 5 closer to right

                direc1= 5

            if (event.key==pygame.K_DOWN): #go down y axis, 5, 
                direc2 = 5

            if (event.key==pygame.K_UP): #go up 
                direc2 = -5

            if (event.key==pygame.K_ESCAPE):
                pygame.quit() #when escape button pressed, game closes
                
        if (event.type==pygame.KEYUP): #keyup when player doesnt have fingers on keys

            if (event.key==pygame.K_LEFT): #left is 0 as player is no touching key buttons
                direc1 = 0
            if (event.key==pygame.K_RIGHT): #right is 0 as player is no touching key buttons so position doesnt change
                direc1 = 0
            if (event.key==pygame.K_UP): #up is 0 as player is no touching key buttons
                direc2 = 0
            if (event.key==pygame.K_DOWN): #down is 0 as player is no touching key buttons
                direc2 = 0
                

                
    
    

    MOVEX+= rectDirectX #this adds the MOVEX variable to the RectDirectX variable so the rectangle will move
    MOVEY+= rectDirectY #this does the same but for the Y direction


    if MOVEX > 430 or MOVEY < 0: #if MOVEX is greater than 400, needs to be less than actual width so there is a sort of 'stopping distance' between rectangle and edge of screen
        rectDirectX *= -1
    if MOVEX > 400 or MOVEY < 0:
        rectDirectY *= -1
                        

    
    window.fill(black) #fills window with black
    
    Sprite1.x+=direc1 #sprite1 has direc1 (x) co-ords inside it
    Sprite1.y+=direc2 #sprite1 has direc2 (y) co-ords inside it
    window.blit(background, (20,50))
    pygame.draw.rect(window, red,(MOVEX, MOVEY, 20, 20)) #draws rectangle with class attributes inside
    
    Sprite1.renderSprite() #renders first sprite and enables it to be seen by user
    Spritetwo.renderSprite2() #renders second sprite and enables it to be seen by user
    
    
    
    clock.tick(30) #measures speed of sprite movement

    pygame.display.flip() #this updates the whole window, and performs same function as .update

pygame.quit()



