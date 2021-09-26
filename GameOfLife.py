# -*- coding: utf-8 -*-
"""
Created on Sun Sep 26 18:08:09 2021

@author: danef
"""

import pygame,sys,copy,keyboard
D = 0
A = 1

Dead = (255,255,255)
Alive = (0,0,0)

TileColour = {D : Dead, A : Alive}
TileSize = 40
Mapwidth = 30
Mapheight = 30

Map = [[D for i in range(Mapwidth)] for j in range(Mapheight)]
GameMap = [[0 for i in range(Mapwidth)] for j in range(Mapheight)]



pygame.init()
pygame.display.set_caption('Game of Life')
display = pygame.display.set_mode((Mapwidth*TileSize,Mapheight*TileSize))
draw = True;

def drawBoard():      
    for row in range(Mapheight):
        for col in range(Mapwidth):
            pygame.draw.rect(display,TileColour[Map[row][col]],(col*TileSize,row*TileSize,TileSize,TileSize))
    for i in range(Mapwidth + 1):
        pygame.draw.line(display, Alive, [TileSize*i, 0], [TileSize*i,Mapwidth*TileSize], 3)
        pygame.draw.line(display, Alive, [0,TileSize*i], [Mapwidth*TileSize,TileSize*i], 3)
    pygame.display.update()

drawBoard()




while True:
  
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
     
        
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            i = int(pos[0]/(TileSize))
            j = int(pos[1]/(TileSize))
            Map[j][i] = A
            GameMap[j][i] = 1
            drawBoard()
            
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                
                
                for k in range(100):
                    newGameMap = [[0 for i in range(Mapwidth)] for j in range(Mapheight)]
                    Map = [[D for i in range(Mapwidth)] for j in range(Mapheight)]
                    
                    for i in range(Mapwidth):
                        for j in range(Mapheight):
                            count = 0
                            if i > 0:
                                count += GameMap[j][i-1]
                                if j > 0:
                                    count += GameMap[j-1][i-1]
                                if j < Mapheight -1:
                                    count += GameMap[j+1][i-1]
                            if i < Mapwidth -1:
                                count += GameMap[j][i+1]
                                if j > 0:
                                    count += GameMap[j-1][i+1]
                                if j < Mapheight -1:
                                    count += GameMap[j+1][i+1]
                            if j > 0:
                                count += GameMap[j-1][i]
                            if j < Mapheight -1:
                                count += GameMap[j+1][i]
                            
                            if GameMap[j][i] == 1:
                                if count == 3 or count == 2:
                                    newGameMap[j][i] = 1
                                    Map[j][i] = A
                            elif GameMap[j][i] == 0:
                                if count == 3:
                                    newGameMap[j][i] = 1
                                    Map[j][i] = A
                    oldGameMap = copy.deepcopy(GameMap)
                    GameMap = newGameMap
                    
                    pygame.event.clear()
                    
                    
                    if oldGameMap == newGameMap:
                        break
                    
                    drawBoard()      
                    pygame.display.update()
                    pygame.time.wait(200)
              

            elif event.key == pygame.K_TAB:
                Map = [[D for i in range(Mapwidth)] for j in range(Mapheight)]
                GameMap = [[0 for i in range(Mapwidth)] for j in range(Mapheight)]
                drawBoard()
            elif event.key == pygame.K_x:       
                for k in range(1):
                    newGameMap = [[0 for i in range(Mapwidth)] for j in range(Mapheight)]
                    Map = [[D for i in range(Mapwidth)] for j in range(Mapheight)]
                    
                    for i in range(Mapwidth):
                        for j in range(Mapheight):
                            count = 0
                            if i > 0:
                                count += GameMap[j][i-1]
                                if j > 0:
                                    count += GameMap[j-1][i-1]
                                if j < Mapheight -1:
                                    count += GameMap[j+1][i-1]
                            if i < Mapwidth -1:
                                count += GameMap[j][i+1]
                                if j > 0:
                                    count += GameMap[j-1][i+1]
                                if j < Mapheight -1:
                                    count += GameMap[j+1][i+1]
                            if j > 0:
                                count += GameMap[j-1][i]
                            if j < Mapheight -1:
                                count += GameMap[j+1][i]
                            
                            if GameMap[j][i] == 1:
                                if count == 3 or count == 2:
                                    newGameMap[j][i] = 1
                                    Map[j][i] = A
                            elif GameMap[j][i] == 0:
                                if count == 3:
                                    newGameMap[j][i] = 1
                                    Map[j][i] = A
                    oldGameMap = copy.deepcopy(GameMap)
                    GameMap = newGameMap
                    
                    pygame.event.clear()
                    
                    
                    if oldGameMap == newGameMap:
                        break
                    
                    drawBoard()      
                    pygame.display.update()
                    pygame.time.wait(200)

pygame.display.update()

