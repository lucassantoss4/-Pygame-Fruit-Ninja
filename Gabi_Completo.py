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

pygame.init()

# ------- Gera tela principal

### ------------
### CORES

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

LARGURA_OBJ = 15
ALTURA_OBJ = 15

# configurações da tela e fonte do jogo
janela = pygame.display.set_mode((LARGURA, ALTURA))
janela.fill(BRANCO)
fonte = pygame.font.SysFont('Comic Sans MS', 30)
texto = fonte.render('Fruit Ninja', True, PRETO, BRANCO)

backgroung = pygame.image.load('util/img/background.png').convert() #A- denominei o fundo como background
backgroung = pygame.transform.scale(backgroung, (LARGURA, ALTURA)) #A- escala
pygame.display.set_caption('Fruit Ninja')

### IMAGENS
bomba_img = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_img = pygame.transform.scale(bomba_img, (ALTURA_OBJ, LARGURA_OBJ))

adm_img = pygame.image.load('util/img/ADM.png').convert_alpha()
adm_img = pygame.transform.scale(adm_img, (ALTURA_OBJ, LARGURA_OBJ))

ccomp_img = pygame.image.load('util/img/CCOMP.png').convert_alpha()
ccomp_img = pygame.transform.scale(ccomp_img, (ALTURA_OBJ, LARGURA_OBJ))

direito_img = pygame.image.load('util/img/DIREITO.png').convert_alpha()
direito_img = pygame.transform.scale(direito_img, (ALTURA_OBJ, LARGURA_OBJ))

ecomp_img = pygame.image.load('util/img/ECOMP.png').convert_alpha()
ecomp_img = pygame.transform.scale(ecomp_img, (ALTURA_OBJ, LARGURA_OBJ))

econo_img = pygame.image.load('util/img/ECONO.png').convert_alpha()
econo_img = pygame.transform.scale(econo_img, (ALTURA_OBJ, LARGURA_OBJ))

faca_img = pygame.image.load('util/img/FACA.png').convert_alpha()
faca_img = pygame.transform.scale(faca_img, (ALTURA_OBJ, LARGURA_OBJ))

mec_img = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_img = pygame.transform.scale(mec_img, (ALTURA_OBJ, LARGURA_OBJ))

mecat_img = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_img = pygame.transform.scale(mecat_img, (ALTURA_OBJ, LARGURA_OBJ))

lista_logos = [adm_img, ccomp_img, direito_img, ecomp_img, econo_img, faca_img, mec_img, mecat_img]
## ------------


# ----- Inicia estruturas de dados

#-----------------Classes-----------------#

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
        self.speedy = random.randint(-5, -3)
        
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
        self.speedy = random.randint(-5, -3)
        
    def update(self):
        #vai atualizar a velocidade
        self.speedy += 0.2
                
        #vai atualizar a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
    
#quantidade de logos lançadas
n_logos = random.randint(0, 6)

#quantidade de bombas lançadas
n_bombas = random.randint(0, 2)   

##A- Cria grupos
todas_bombas = pygame.sprite.Group()

for i in range(n_bombas):
    bomba = Bombas(bomba_img)
    todas_bombas.add(bomba)
    
##G- Cria grupo de logos
todas_logos = pygame.sprite.Group()
for i in range(n_logos):
    imagem = random.randint(0, 6)
    fruta = Logos(lista_logos[imagem])
    

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
    todas_bombas.update()
    todas_logos.update()

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados


