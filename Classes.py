import pygame
import random
from geral import PRETO, BRANCO, VERMELHO, AMARELO, VERDE, AZUL, ROXO, LARGURA, ALTURA

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
    
### problemas/coias que a gabi pensou

