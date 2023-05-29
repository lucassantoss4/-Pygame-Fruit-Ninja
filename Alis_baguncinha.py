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
import time
import sys

pygame.init()
pygame.mixer.init() # inicializa os sons

# ------- Gera tela principal

PAUSE = 5000

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

LARGURA = 900
ALTURA = 600

ALTURA_OBJ = 60
LARGURA_OBJ = 60

# configurações da tela e fonte do jogo
janela = pygame.display.set_mode((LARGURA, ALTURA))
janela.fill(BRANCO)
fonte = pygame.font.Font("util/fonte/upheavtt.ttf", 48)
texto = fonte.render('Cursos Ninja', True, PRETO, BRANCO)

background = pygame.image.load('util/img/background_inteiro.png').convert() #A- denominei o fundo como background
background = pygame.transform.scale(background, (LARGURA, ALTURA)) #A- escala
pygame.display.set_caption('Cursos Ninja')

### IMAGENS
machado_img = pygame.image.load('util/img/MACHADO.png').convert_alpha()
machado_img = pygame.transform.scale(machado_img, (LARGURA_OBJ+10, ALTURA_OBJ+10))

bomba_img = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_img = pygame.transform.scale(bomba_img, (LARGURA_OBJ-5, ALTURA_OBJ-5))

faca_img = pygame.image.load('util/img/FACA.png').convert_alpha()
faca_img = pygame.transform.scale(faca_img, (LARGURA_OBJ, ALTURA_OBJ))

adm_img = pygame.image.load('util/img/ADM.png').convert_alpha()
adm_img = pygame.transform.scale(adm_img, (LARGURA_OBJ, ALTURA_OBJ))

ccomp_img = pygame.image.load('util/img/CCOMP.png').convert_alpha()
ccomp_img = pygame.transform.scale(ccomp_img, (LARGURA_OBJ-5, ALTURA_OBJ-5))

direito_img = pygame.image.load('util/img/DIREITO.png').convert_alpha()
direito_img = pygame.transform.scale(direito_img, (LARGURA_OBJ+10, ALTURA_OBJ))

ecomp_img = pygame.image.load('util/img/ECOMP.png').convert_alpha()
ecomp_img = pygame.transform.scale(ecomp_img, (LARGURA_OBJ-10, ALTURA_OBJ+10))

econo_img = pygame.image.load('util/img/ECONO.png').convert_alpha()
econo_img = pygame.transform.scale(econo_img, (LARGURA_OBJ+7, ALTURA_OBJ+7))

mec_img = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_img = pygame.transform.scale(mec_img, (LARGURA_OBJ, ALTURA_OBJ))

mecat_img = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_img = pygame.transform.scale(mecat_img, (LARGURA_OBJ, ALTURA_OBJ))

lista_logos = [adm_img, ccomp_img, direito_img, ecomp_img, econo_img, mec_img, mecat_img]


## -----SONS-------

pygame.mixer.music.load('util/sons/FRUIT-NINJA-fundo.mp3')
pygame.mixer.music.set_volume(0.4)

# ----- Inicia estruturas de dados

#-----------------Classes-----------------#

#criando a classe de logos
class Logos(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(150, 750) #as 'frutinhas' não são lançadas no canto
        self.rect.y = 600-LARGURA_OBJ #as 'frutinhas' são lançadas de baixo
        
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-2, 2)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-15, -10)
        
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
        self.rect.x = random.randint(150, 750) #as bombas não são lançadas no canto
        self.rect.y = 600-LARGURA_OBJ #as bombas são lançadas de baixo
                
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-2, 2)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-15, -10)
        
    def update(self):
        #vai atualizar a velocidade
        self.speedy += 0.2
                
        #vai atualizar a posição
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        
#-----------------Classe Da Tela -----------------#
class GameOverScreen:
    def __init__(self, largura, altura, tempo_maximo):
        pygame.init()
        self.largura = largura
        self.altura = altura
        self.tempo_maximo = tempo_maximo
        self.tempo_inicial = time.time()
        self.screen = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption('Game Over')
        self.font = pygame.font.Font("util/fonte/upheavtt.ttf", 60)
        self.text = self.font.render('Game Over', True, (200, 0, 0))
        self.text_rect = self.text.get_rect(center=(self.largura // 2, self.altura // 2 - 10))
        self.reiniciar = False
        self.botao_reiniciar = pygame.Rect(self.largura // 2 - 100, self.altura // 2 + 50, 200, 50)
        self.botao_reiniciar_texto = pygame.font.Font("util/fonte/upheavtt.ttf", 30).render('Reiniciar', True, (0, 0, 0))
        self.botao_reiniciar_texto_rect = self.botao_reiniciar_texto.get_rect(center=self.botao_reiniciar.center)

    def run(self):
        while True:
            pygame.mouse.set_visible(True)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    if self.botao_reiniciar.collidepoint(event.pos):
                        self.reiniciar = True

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text, self.text_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.botao_reiniciar)
            self.screen.blit(self.botao_reiniciar_texto, self.botao_reiniciar_texto_rect)
            pygame.display.flip()

            '''tempo_atual = time.time()
            tempo_decorrido = tempo_atual - self.tempo_inicial
            if tempo_decorrido >= self.tempo_maximo:
                pygame.quit()
                sys.exit()'''


##A- Cria grupos
todas_bombas = pygame.sprite.Group()
todas_logos = pygame.sprite.Group()

#adiciona elementos nos grupos
    #sorteia a quantidade de elementos de cada
n_logos = random.randint(0, 6)
n_bombas = random.randint(0, 2)  

for i in range(n_bombas):
    bomba = Bombas(bomba_img)
    todas_bombas.add(bomba)

for i in range(n_logos):
    imagem = random.randint(0, 6)
    fruta = Logos(lista_logos[imagem])
    todas_logos.add(fruta)
    
    
#------- mouse

pygame.mouse.set_visible(False)
# faca_img_rect = faca_img.get_rect()
machado_img_rect = machado_img.get_rect()


#------------ Jogo -----------#
    
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

#variáveis do jogo
Score = 0
vida = 3

game = True

# ===== Loop principal =====
pygame.mixer.music.play(loops=-1) #para tocar a música de fundo em loop
while game:
    #definindo tempo para execução do loop
    clock.tick(FPS)
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
            
    if vida == 0:
        game_over_screen = GameOverScreen(LARGURA, ALTURA, 5)  # Ajuste o tempo de exibição se desejar
        while not game_over_screen.reiniciar:
            game_over_screen.run()

        Score = 0
        vida = 3
            
    #obtem a posição do mouse para cortar as frutas  
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    
    #--------- trata das logos e bombas
    for logo in todas_logos:
        if logo.rect.x < mouse_x < (logo.rect.x + ALTURA_OBJ) and logo.rect.y < mouse_y < (logo.rect.y + LARGURA_OBJ):
            logo.kill()
            Score += 100
        if logo.rect.x > LARGURA or logo.rect.x - ALTURA_OBJ < 0:
            logo.kill()
        if logo.rect.y > ALTURA:
            logo.kill()
    
    for bomba in todas_bombas:
        if bomba.rect.x < mouse_x < (bomba.rect.x + ALTURA_OBJ) and bomba.rect.y < mouse_y < (bomba.rect.y + LARGURA_OBJ):
            bomba.kill()
            vida -= 1
        if bomba.rect.x > LARGURA or bomba.rect.x - ALTURA_OBJ < 0:
            bomba.kill()
        if bomba.rect.y > ALTURA:
            bomba.kill()
            
        
    if len(todas_bombas) == 0 and len(todas_logos) == 0:
        #adiciona elementos nos grupos
            #sorteia a quantidade de elementos de cada
        n_logos = random.randint(0, 6)
        n_bombas = random.randint(0, 2)  
        
        for i in range(n_bombas):
            bomba = Bombas(bomba_img)
            todas_bombas.add(bomba)

        for i in range(n_logos):
            imagem = random.randint(0, 6)
            fruta = Logos(lista_logos[imagem])
            todas_logos.add(fruta)        

        
    # ----- Atualiza estado do jogo
   
    todas_bombas.update()
    todas_logos.update()        
            
    # ----- Gera saídas
    
    fonte_score = pygame.font.Font("util/fonte/upheavtt.ttf", 35)
    texto_score = fonte_score.render('Score {0}'.format(Score), True, PRETO)
    texto_vidas = fonte_score.render('Vidas {0}'.format(vida), True, PRETO)
    
    janela.blit(background, (0,0)) #A - coloquei o fundo na janela
    janela.blit(texto_score, (100, 5))
    janela.blit(texto_vidas, (700,5))
    # faca_img_rect.center = pygame.mouse.get_pos()
    machado_img_rect.center = pygame.mouse.get_pos()  
    # janela.blit(faca_img, faca_img_rect) 
    janela.blit(machado_img, machado_img_rect)
    #------- Desenha bombas e logos
    todas_bombas.draw(janela)
    todas_logos.draw(janela)
    
    pygame.display.update()  # Mostra o novo frame para o jogador
    
    
# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

"""
queria dar um tempinho até que as coisas sejam lançadas de novo   

as frutas não precisam ser lançadas todas ao mesmo tempo, pode ter um 
intervalo de lançameto entre elas, teria como fazer isso?  


fazer o efeito de corte das frutas
colocar som no corte e no jogo


"""

##### Sons 