import pygame
import sys
import time

ALTURA = 800
LARGURA = 600
class GameOverScreen:
    def __init__(self, LARGURA, ALTURA, tempo_maximo):
        pygame.init()
        self.LARGURA = LARGURA
        self.ALTURA = ALTURA
        self.tempo_maximo = tempo_maximo
        self.tempo_inicial = time.time()
        self.screen = pygame.display.set_mode((self.LARGURA, self.ALTURA))
        pygame.display.set_caption('Game Over')
        self.font = pygame.font.SysFont('Comic Sans MS', 48)
        self.text = self.font.render('Game Over', True, (255, 0, 0))
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

            # Verificar se o tempo máximo foi atingido
            tempo_atual = time.time()
            tempo_decorrido = tempo_atual - self.tempo_inicial
            if tempo_decorrido >= self.tempo_maximo:
                pygame.quit()
                sys.exit()

# Exemplo de uso
game_over_screen = GameOverScreen(ALTURA, LARGURA, 5)  # Tempo máximo de 5 segundos
game_over_screen.run()
