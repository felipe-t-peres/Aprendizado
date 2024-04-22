#Esse não deu certo
'''import pygame
pygame.init()
pygame.mixer.music.load('_Girls_M5.mp3')
pygame.mixer.music.play()
pygame.event.wait()'''

#Corrigido
import pygame
pygame.init()
pygame.mixer.music.load('_Girls_M5.mp3')
pygame.mixer.music.play()
input()
pygame.event.wait()