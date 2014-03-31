import pygame #import pygame
pygame.init() #initialises pygame

from pygame.locals import * #imports additional pygame modules which are seen as not usually needed

import random #imports random module to allow for randrange and randint

width=440 #set width of screen for future use
height=400 #set height of screen for future use

window = pygame.display.set_mode((440,400)) #sets window size to 440 pixels wide, 400 pixels high
pygame.display.set_mode((width,height))
GameOver = pygame.image.load('gameover.jpg')

background = pygame.image.load('OUTERSPACE.jpg') #gives the background image
pygame.display.set_caption("Planet eater!") #displays captions/title for game
clock = pygame.time.Clock() #used to control framerate of game



MOVEX = 100 #position of rectangle
MOVEY = 300 #position of rectangle
rectDirectX=5 #this is the direction and speed of rectangle1 (first enemy)
rectDirectY=3 #direction of first enemy in y co-ords
rectDirectXtwo=4 #direction of 2nd enemy it will travel this plus MOVEXenemytwo variable so it will move and bounce around screen
rectDirectYtwo=6 #y direction of 2nd enemy

MOVEXenemytwo=300 #second enemy variables which represents X value
MOVEYenemytwo=150 #this represents second enemies Y position

score = 0# score = 0 but goes up 1 when player collects gold sprite

MOVEXenemySecond=5
MOVEYenemySecond=9

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
        pygame.draw.rect(window,red,(MOVEXenemySecond,MOVEYenemySecond,30, 9)) #this function renders the class and draws and rectangle with the attributes found in the class
        self.rect = pygame.Rect(MOVEXenemySecond, MOVEYenemySecond, self.width, self.height) #converts rectangle to one PYGAME can use



class Sprite2(pygame.sprite.Sprite):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)

    def renderSprite2(self):
        pygame.draw.rect(window, red,(MOVEX, MOVEY, 20, 20))
        self.rect = pygame.Rect(MOVEX, MOVEY, self.width, self.height)
    




class Sprite3(pygame.sprite.Sprite): #enemy sprite
    def __init__(self,x,y,width,height):
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
        self.MOVEXenemytwo = MOVEXenemytwo #x position of 2nd enemy
        self.MOVEYenemytwo = MOVEYenemytwo #y position of 2nd enemy
        self.width = width
        self.height = height
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, width, height)

    

    def renderSprite4(self):
        pygame.draw.rect(window, red,(MOVEXenemytwo, MOVEYenemytwo, 30, 20))
        self.rect = pygame.Rect(MOVEXenemytwo, MOVEYenemytwo, self.width, self.height)
        

Sprite1=Sprite(20,35,15,14)#player sprite is 200 pixels across and 250 pixels down at starting point, 15 pixels wide, 14 high

Spritethree=Sprite3(100,200,20,20)
Spritefour=Sprite4(200,172,30,15)


pygame.display.update()


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
                score+=0.2
                print score

            if (event.key==pygame.K_RIGHT): #go right x axis, 5, because adding 5 closer to right

                direc1= 4
                score+=0.2
                print score

            if (event.key==pygame.K_DOWN): #go down y axis, 5, 
                direc2 = 4
                score+=0.2
                print score

            if (event.key==pygame.K_UP): #go up 
                direc2 = -4
                score+=0.2
                print score

            if (event.key==pygame.K_ESCAPE):
                pygame.quit() #when escape button pressed, game closes

            if (event.key==pygame.K_p): #if user presses p
                
                pygame.time.wait(2700) #if user presses p the pygame program will wait a certain amount of milliseconds
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
                
        
            
    
    
        

    if MOVEXenemytwo > 440: #second enemy movement
        MOVEXenemytwo = 440
        rectDirectXtwo= - 6
    elif MOVEXenemytwo < 0:
        MOVEXenemytwo = 0
        rectDirectXtwo = 8
    elif MOVEYenemytwo > 400:
        MOVEYenemytwo = 400
        rectDirectYtwo = -3
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

    Sprite1.x+=direc1 #sprite1 has direc1 (x) co-ords inside it
    Sprite1.y+=direc2 #sprite1 has direc2 (y) co-ords inside it

            



    
    window.fill(black) #fills window with black


    
    
    if Sprite1.x  > 440: #if Sprite1 (one player controls goes out of screen, end game)
        pygame.quit() #pygame will end
        break #break will stop code after running
    
    elif Sprite1.x < 0: #if sprite1, that player controls goes off screen to the left the game will quit
        pygame.quit() #quits pygame
        break #stops loop
    elif Sprite1.y > 400:
        pygame.quit()
        break
    elif Sprite1.y < 0:
        pygame.quit()
        break

    
    window.blit(background, (20,50)) #blits background onto screen

    
    
    Sprite1.renderSprite() #renders first sprite and enables it to be seen by user
    Spritethree.renderSprite3() #defines first enemy
    Spritefour.renderSprite4() #defines second enemy
    MOVEX += rectDirectX #adds together first position plus rect direction its told to go
    MOVEY += rectDirectY
    MOVEXenemytwo += rectDirectXtwo #adds together the initial position as well as position it has been told to go resulting in random movement
    MOVEYenemytwo += rectDirectYtwo
    
    
    
    clock.tick(43) #measures speed of sprite movement



    pygame.display.flip() #this updates the whole window, and performs same function as .update

pygame.quit()







