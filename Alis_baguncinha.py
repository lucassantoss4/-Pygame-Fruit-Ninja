import pygame
import random
from geral import PRETO, BRANCO, VERMELHO, AMARELO, VERDE, AZUL, ROXO, LARGURA, ALTURA, LARGURA_OBJ, ALTURA_OBJ, bomba_img, lista_logos
from Classes import Bombas, Logos

#criando a classe de logos
class Logos(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA-50) #as 'frutinhas' não são lançadas no canto
        self.rect.y = 600 #as 'frutinhas' são lançadas de baixo
        
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-1, 1)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-3, -5)
        
    def update(self):
        #vai atualizar a velocidade
        self.speedy += 0.2
                
        #vai atualizar a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy
            
        
#usar a mesma lógica para construir a série de bombas
class Bombas(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA-50) #as bombas não são lançadas no canto
        self.rect.y = 600 #as bombas são lançadas de baixo
                
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-1, 1)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-3, -5)
        
    def update(self):
        #vai atualizar a velocidade
        self.speedy += 0.2
                
        #vai atualizar a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
    
 
#quantidade de frutas lançadas
n_frutas = random.randint(0, 6)

#quantidade de bombas lançadas
n_bombas = random.randint(0, 2)


# ----- Gera tela principal

# configurações da tela e fonte do jogo
janela = pygame.display.set_mode((LARGURA, ALTURA))
janela.fill(BRANCO)
fonte = pygame.font.SysFont('Comic Sans MS', 30)
texto = fonte.render('Fruit Ninja', True, PRETO, BRANCO)

backgroung = pygame.image.load('util/img/background.png').convert() #A- denominei o fundo como background
backgroung = pygame.transform.scale(backgroung, (LARGURA, ALTURA)) #A- escala
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
    janela.fill(PRETO)  # Preenche com a cor preta
    janela.blit(backgroung, (0,0)) #A - coloquei o fundo na janela

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

