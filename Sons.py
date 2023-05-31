import pygame
from Tela_inicial import *

## -----SONS-------

pygame.mixer.music.load('util/sons/FRUIT-NINJA-fundo.mp3')
pygame.mixer.music.set_volume(0.4)

## -----SONS-------

canal1 = pygame.mixer.Channel(0)
canal2 = pygame.mixer.Channel(1)
canal3 = pygame.mixer.Channel(3)

musica_fundo = pygame.mixer.Sound('util/sons/FRUIT-NINJA-fundo.mp3')

explosao = pygame.mixer.Sound('util/sons/explode.mp3')

#hits
hit_0 = pygame.mixer.Sound('util/hits/hit0.mp3')

hit_1 = pygame.mixer.Sound('util/hits/hit1.mp3')

hit_2 = pygame.mixer.Sound('util/hits/hit2.mp3')

hit_3 = pygame.mixer.Sound('util/hits/hit3.mp3')

hit_4 = pygame.mixer.Sound('util/hits/hit4.mp3')

hit_5 = pygame.mixer.Sound('util/hits/hit5.mp3')

hit_6 = pygame.mixer.Sound('util/hits/hit6.mp3')

hit_7 = pygame.mixer.Sound('util/hits/hit7.mp3')

hit_8 = pygame.mixer.Sound('util/hits/hit8.mp3')

hit_9 = pygame.mixer.Sound('util/hits/hit9.mp3')

lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9]