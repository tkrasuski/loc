# -*- coding: utf-8 -*-
# LOC Map designer 
import pygame
from config import ConfigManager
import maps
cfg = ConfigManager()
gridSize = dict(x=10,y=100,size=80)

pygame.init()
scrinfo = pygame.display.Info()
x = scrinfo.current_w - 100
y = scrinfo.current_h - 100

display = pygame.display.set_mode((x,y))
pygame.display.set_caption(u'LOC Designer')
pygame.display.update()

def designerLoop():
    endDesigner = False
    palette = []
    while not endDesigner:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                endDesigner = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print (pos)
    pygame.quit()
    quit()

if __name__ == '__main__':
    designerLoop()