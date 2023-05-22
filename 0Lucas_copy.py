# ===== Inicialização =====

'''
Legendas de atualização <3
A <3
G <3
L <3
'''

# ----- Importa e inicia pacotes
import pygame
import random
# from geral import PRETO, BRANCO, VERMELHO, AMARELO, VERDE, AZUL, ROXO, LARGURA, ALTURA, LARGURA_OBJ, ALTURA_OBJ
# from Classes import Bombas, Logos

    #A- criei o arquivo geral.py pra guardar coisas que podemos usar frequentemente

PRETO = (24, 24, 24)
BRANCO = (255, 255, 255)
VERMELHO = (255, 47, 43)
AZUL = (40, 61, 193)
VERDE = (40, 174, 73)
AMARELO = (239, 238, 81)
ROXO = (169, 85, 255)

### TAMANHOS

LARGURA = 480
ALTURA = 600

pygame.init()

# ----- Gera tela principal

# configurações da tela e fonte do jogo
janela = pygame.display.set_mode((LARGURA, ALTURA))

# configuração de textos 
fonte = pygame.font.SysFont('Comic Sans MS', 30)
texto = fonte.render('Fruit Ninja', True, PRETO)

backgroung = pygame.image.load('util/img/background.png').convert() #A- denominei o fundo como background
backgroung = pygame.transform.scale(backgroung, (LARGURA, ALTURA)) #A- escala
pygame.display.set_caption('Fruit Ninja')

# ----- Inicia assets
BOMBA_LARGURA = 50
BOMBA_ALTURA = 38
bomba_img = pygame.image.load('util/img/bomba.png').convert_alpha() # desenha a bomba
bomba_img_escala = pygame.transform.scale(bomba_img, (BOMBA_LARGURA, BOMBA_ALTURA)) 
bomba_img_small = pygame.transform.scale(bomba_img, (BOMBA_LARGURA, BOMBA_ALTURA))

# ----- Inicia estruturas de dados
game = True
bomba_x = BOMBA_LARGURA
bomba_y = 250
bomba_velocidadeX = 3
bomba_velocidadeY = 6

# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 13


# ===== Loop principal =====
while game:
    clock.tick(FPS)
    # ----- Trata eventos
    for event in pygame.event.get():


        
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            game = False

    # ----- Atualiza estado do jogo
    # Atualizando a posição do meteoro
    bomba_x += bomba_velocidadeX
    bomba_y += bomba_velocidadeY
    # verifica se a bomba passar do final da tela, volta para cima
    if bomba_y > ALTURA or bomba_x + BOMBA_LARGURA < 0 or bomba_x > LARGURA:
        bomba_x = 200
        bomba_y = 200
            
    # ----- Gera saídas
    janela.fill(PRETO)  # Preenche com a cor preta
    janela.blit(backgroung, (0,0)) # desenha o fundo na janela
    janela.blit(texto, (10,10)) # desenha o texto na janela

    # ----- Atualiza estado do jogo
    janela.blit(bomba_img_small, (bomba_x, bomba_y))
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


