import pygame
from IDE import *

shift = False
alt = False

cursor = (0, 0)
global cursor

def translateEvent(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RSHIFT or event.key == K_LSHIFT:
            shift = True
            return None
        if key == pygame.K_RALT or key == K_RALT:
            alts = True
            return None
        if event.key == pygame.K_BACKSPACE: return "back"
        if event.key == pygame.K_SPACE: return "nl"
        if event.key == pygame.K_DELETE: return "del"
        if event.key == pygame.UP: return "up"
        if event.key == pygame.UP: return "down"
        if event.key == pygame.UP: return "left"
        if event.key == pygame.UP: return "right"
        return event.unicode
    if event.type == pygame.KEYUP:
        key = event.key
        if key == pygame.K_RSHIFT or key == K_LSHIFT: shift = False
        if key == pygame.K_RALT or key == K_RALT: alt = False
        return None
    return None

def translateSpecialToList(key):
    linePos = cursor[0]
    letterPos = cursor[1]
    line = IDE.code[linePos]
    if key == "back" and letterPos != 0:
        newLine = line[:letterPos-1] + line[letterPos:]
        IDE.code[linePos] = newLine
    if key == "del" and letterPos != len(line):
        newLine = line[:letterPos] + line[letterPos+1:]
        IDE.code[linePos] = newLine
    if key == "nl":
        newLine = line[letterPos:]
        IDE.code[linePos] = line[:letterPos]
        IDE.code.insert(linePos+1, newLine)
    if key == "right" and not (letterPos == len(line) and linePos == len(IDE.code)):
        if len(line) == letterPos:
            cursor = (linePos+1, 0)
        else:
            cursor = (linePos, letterPos+1)
    if key == "left" and not (letterPos == 0 and linePos == 0):
        if letterPos == 0:
            cursor = (linePos-1, len(IDE.code[linePos-1]))
        else:
            cursor = (linePos, letterPos-1)
    if key == "up" and linePos != 0:
        if len(IDE.code[linePos-1]) < letterPos:
            cursor = (linePos-1, len(IDE.code[linePos-1]))
        else:
            cursor = (linePos-1, letterPos)
    if key == "down" and len(IDE.code) > linePos:
        if len(IDE.code[linePos+1]) < letterPos:
            cursor = (linePos+1, len(IDE.code[linePos+1]))
        else:
            cursor = (linePos+1, letterPos)

def translateToList(key):
    linePos = cursor[0]
    letterPos = cursor[1]
    line = IDE.code[linePos]
    newLine = line[:letterPos] + key + line[letterPos:]
    IDE.code[linePos] = newLine