import pygame
import sys
from Constantes import *
from Imagens import *
from Classes import *
from Sons import *

def Tela_Game_Over(LARGURA, ALTURA, Score):
    Tela_Game_Final = True # variável para o loop da tela de game over
    pygame.mouse.set_visible(True)
    
    #cria tudo que vai aparecer na tela final
    screen = pygame.display.set_mode((LARGURA, ALTURA))  # cria a tela
    pygame.display.set_caption('Insper Ninjas')  # nome da tela
    font = pygame.font.Font("util/fonte/upheavtt.ttf", 60)  # fonte do texto
    font2 = pygame.font.Font("util/fonte/upheavtt.ttf", 90) # fonte do score
    font3 = pygame.font.Font("util/fonte/upheavtt.ttf", 30) # fonte do reinicar
    text = font.render('Game Over', True, VERMELHO)  # cor do texto e escrita
    score = font2.render('Score: ' + str(Score), True, BRANCO)  # cor do texto e escrita
    text_rect = text.get_rect(center=(LARGURA // 2, ALTURA // 2))  # posição do texto
    score_rect = score.get_rect(center=(LARGURA // 2, ALTURA // 2 - 90))  # posição do texto
    text3 = font3.render('Pressione qualquer tecla para reiniciar', True, BRANCO) #intruções para reiniciar o jogo
    text3_rect = text3.get_rect(center=(LARGURA // 2, ALTURA // 2 + 80))

    # ----- Gera saídas

    screen.fill((0, 0, 0))  # Preenche com a cor preta no fundo
    screen.blit(text, text_rect)  # coloca o texto na tela
    screen.blit(score, score_rect)  # coloca o texto na tela
    screen.blit(text3, text3_rect)
    pygame.display.flip()  # atualiza a tela

    while Tela_Game_Final: 
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYUP:
                state = INICIAR
                Tela_Game_Final = False
                
                
    return state 
