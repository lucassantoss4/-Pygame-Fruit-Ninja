import pygame
from Constantes import *

pygame.init()
pygame.mixer.init() # inicializa os sons

janela = pygame.display.set_mode((LARGURA, ALTURA)) # tela como janela

pygame.display.set_caption('Insper Ninja') # nome da janela
