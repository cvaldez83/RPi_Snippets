#!/usr/lib python3.5
import pygame
pygame.init()
##pygame.mixer.music.load("tron.wav")
a = pygame.mixer.Sound("tron.wav")

##pygame.mixer.music.play()
print("audio length is seconds: " + str(a.get_length()))