class shootingGame():
        
            background = pygame.image.load(bgi).convert()
            mouse_c = pygame.image.load(mif)
            killer = pygame.image.load(kil)
                
            def gunSound():
                pygame.mixer.music.load(gun) #loads gun file from global variable gun.
                pygame.mixer.music.play(0,0)           
           
            while True:
                for event in pygame.event.get():
                    
                    if event.type == QUIT:
                        pygame.quit()
                        sys.exit()
                        
                    if event.type == pygame.MOUSEBUTTONDOWN and (not(chooseX < x < chooseX2) or not (chooseY < y < chooseY2)): 
                        gunSound()
                        missed+=1
                        totalMissed+=1
                        chooseX=random.randint(0, 1000)
                        chooseY=random.randint(0,450)
                        chooseX2=chooseX+169
                        chooseY2=chooseY+191
                        
                    if event.type == pygame.MOUSEBUTTONDOWN and (chooseX < x < chooseX2) and (chooseY < y < chooseY2): 
                        gunSound()
                        killed+=1
                        missed=0
                        chooseX=random.randint(0, 1000)
                        chooseY=random.randint(0,450)
                        chooseX2=chooseX+169
                        chooseY2=chooseY+191
                        
                    if missed >= 3:
                        print "game over"
                        print totalMissed
                        #pygame.quit()
                        #sys.exit()

                score = font.render("Score:"+str(killed),True,color)
                missedText = font.render("Missed:"+str(missed),True,color)
                
                
                screen.blit(background,(0,0))
                x,y = pygame.mouse.get_pos()
                screen.blit(score,(1100,50))
                screen.blit(missedText,(1100,100))
                screen.blit(killer,(chooseX,chooseY))
                screen.blit(mouse_c,(x-106,y-106))
                pygame.mouse.set_visible(False)
                

                clock.tick(30) 

                pygame.display.update()
