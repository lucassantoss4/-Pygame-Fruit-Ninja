# ----- Importa e inicia pacotes
import pygame
import random
import time
import sys

LARGURA = 800
ALTURA = 600

class TelaInicial:
    def __init__(self, LARGURA, ALTURA):
        pygame.init()
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        # self.tempo_maximo = tempo_maximo
        # self.tempo_inicial = time.time()
        self.screen = pygame.display.set_mode((self.LARGURA, self.ALTURA)) 
        # pygame.display.set_caption('Click na Tela Para o Jogo Inicia') ## nome da janela
        self.font = pygame.font.SysFont('Comic Sans MS', 48)
        self.text = self.font.render('Click na Tela Para o Jogo Inicia', True, (255, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.LARGURA // 2, self.ALTURA // 2))

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text, self.text_rect)
            pygame.display.flip()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()                

            

game_over_screen = TelaInicial(LARGURA, ALTURA)  # escreve "Game Over" por # segundos e encessa o jogo
game_over_screen.run()