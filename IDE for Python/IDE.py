import pygame
import FileUtil
#import Modules
import tkinter as FileSave
import os
import time

code = []

##Variable Setup
Background = FileUtil.openVariableListItem("Background_Colour")
Display = FileUtil.openVariableListItem("DisplayInfo")
AutoHelp = False

BackgroundTexture = pygame.image.load("Textures/BackgroundTexture.png")
BackgroundTexture = pygame.transform.scale(BackgroundTexture, (Display[0], Display[1]))
APPIcon = pygame.image.load("Textures/APPIcon.png")

##Window Setup
pygame.init()
GameDisplay = pygame.display.set_mode((Display[0],Display[1]))
pygame.display.set_caption("IDE for Python")
pygame.display.set_icon(APPIcon)
Clock = pygame.time.Clock()
crashed = False
Update = True 
OldTime = time.time()

##Functions

def DisplayBackground(BackgroundTexture):
    GameDisplay.blit(BackgroundTexture, (0,0))

    #Handles ButtonPresses

    Cursor = pygame.mouse.get_pos()
    Cursor_Pressed = pygame.mouse.get_pressed()
    print()

pygame.font.init()
font = pygame.font.SysFont(None, 30)
white = (255, 255, 255)
text = font.render("", False, white)
string = ""

def DisplayText(TextList):
    print(TextList)

##Main Loop

while not crashed:

    for event in pygame.event.get():

        Cursor = pygame.mouse.get_pos()
        Cursor_Pressed = pygame.mouse.get_pressed()

        if event.type == pygame.QUIT:
            crashed = True

        ##Only updates on events (Efficiency)
        
        if len(str(event)) > 2:
            Update = True 
        
        
        ##Cursor is in button menu

        if Cursor[0] <= 171 and Cursor_Pressed[0] == 1:


            if 50 >= Cursor[1] >= 25:
                AutoHelp = not AutoHelp
        
        #if mod.isKeyPress(event):
            #key = mod.getKey(event)


    ##Window changing events

    if Update == True:
    
        DisplayBackground(BackgroundTexture)
        text = font.render(string, False, white)
        pygame.display.update()

        print("Frame has been written")


    #End Loop

    Clock.tick(80)
    Update = False

    

pygame.quit()