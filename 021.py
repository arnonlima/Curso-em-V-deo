#Faça um programa em que abra e reproduza o áudio de um arquivo MP3.#

import pygame

pygame.init()
pygame.mixer.music.load('ex021.mp3') #Arquivo de áudio,mesma pasta do arquivo .py
pygame.mixer.music.play()       
pygame.event.wait() #Espera o áudio terminar de tocar para encerrar o programa  