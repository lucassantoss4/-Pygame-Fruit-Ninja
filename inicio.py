# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random

pygame.init()

# ----- Gera tela principal
LARGURA = 480
ALTURA = 600

janela = pygame.display.set_mode((LARGURA, ALTURA))

backgroung = pygame.image.load('util/img/background.png').convert()
backgroung = pygame.transform.scale(backgroung, (LARGURA, ALTURA))

#######gabi começou a mexer aqui
pygame.display.set_caption('Fruit Ninja')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.KEYUP:
            game = False

    # ----- Gera saídas
    janela.fill((0, 0, 0))  # Preenche com a cor preta
    janela.blit(backgroung, (0,0))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

#criando a classe de logos
class Logos(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA-50) #as 'frutinhas' são lançadas de baixo pracima, e não são lançadas no canto
        self.rect.y = 600 #as 'frutinhas' são lançadas de baixo
        
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-2, 2)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(4, 6)
        
######gabi mexeu até aqui