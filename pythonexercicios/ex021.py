#Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3
import pygame  # Load the popular external library

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('ex021.mp3')
pygame.mixer.music.play()
pygame.event.wait()




    