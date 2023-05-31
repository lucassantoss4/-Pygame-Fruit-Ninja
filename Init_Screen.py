import pygame
import sys
from Constantes import *
from Imagens import *
from Classes import *
from Sons import *

def Tela_Iniciar(janela, fundo_pixel, mouser_img):
    botao_inicia = True
    # Coordenadas e dimensões do retângulo
    x = 100
    y = 100
    largura_retangulo = 200
    altura_retangulo = 100
    retangulo = pygame.Rect(x, y, largura_retangulo, altura_retangulo)
    
    while botao_inicia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                botao_inicia = False
                state = JOGAR

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    botao_inicia = False
                    state = JOGAR
        
        # Coordenadas e dimensões do retângulo

        mouser_img_pos = pygame.mouse.get_pos()  # obtem a posição do mouse para desenhar a imagem do mouse
        pygame.draw.rect(janela, (255, 0, 0), retangulo)  # desenha o retângulo na tela
        font = pygame.font.Font("util/fonte/upheavtt.ttf", 30)
        
        # ----- Gera saídas 
        janela.blit(fundo_pixel, (0, 0))  # coloca a imagem de fundo na tela
        janela.blit(mouser_img, mouser_img_pos)  # coloca a imagem do mouse na tela

        # Desenhe o cursor do mouse
        janela.blit(mouser_img, mouser_img_pos)  # coloca a imagem do mouse na tela

        pygame.display.flip()  # Mostra o novo frame para o jogador
        
    return state