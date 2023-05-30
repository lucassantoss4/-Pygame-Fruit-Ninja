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
janela = pygame.display.set_mode((LARGURA, ALTURA)) # tela como janela
janela.fill(BRANCO) # cor de fundo da janela
fonte = pygame.font.Font("util/fonte/upheavtt.ttf", 48) # fonte do jogo
texto = fonte.render('Cursos Ninja', True, PRETO, BRANCO)   # texto do jogo

background = pygame.image.load('util/img/background_inteiro.png').convert() #carrega a imagem de fundo
background = pygame.transform.scale(background, (LARGURA, ALTURA)) # redimensiona a imagem de fundo

fundo_pixel = pygame.image.load('util/img/fundo_pixel.jpg').convert_alpha()
fundo_pixel = pygame.transform.scale(fundo_pixel, (LARGURA, ALTURA))

pygame.display.set_caption('Cursos Ninja') # nome da janela

### IMAGENS
machado_img = pygame.image.load('util/img/MACHADO.png').convert_alpha()
machado_img = pygame.transform.scale(machado_img, (LARGURA_OBJ+10, ALTURA_OBJ+10))

mouser_img = pygame.image.load('util/img/MAO_MOSER.png').convert_alpha() # mouse
mouser_img = pygame.transform.scale(mouser_img, (LARGURA_OBJ, ALTURA_OBJ))



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

pygame.mouse.set_visible(False) #tira o mouse da tela
# faca_img_rect = faca_img.get_rect()
machado_img_rect = machado_img.get_rect() 
mouser_img_rect = mouser_img.get_rect() #cria um retângulo para o mouse


#------------ Jogo -----------#
    
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

#variáveis do jogo
Score = 0
vida = 3 


######### Tela de início #########
botao_inicia = True
while botao_inicia:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            botao_inicia = False

    mouser_img_pos = pygame.mouse.get_pos() #obtem a posição do mouse para desenhar a imagem do mouse

    # ----- Gera saídas
    # janela.fill((0, 0, 0))  # Preenche com a cor preta no fundo
    janela.blit(fundo_pixel , (0, 0)) #coloca a imagem de fundo na tela

    # Desenhe o cursor do mouse
    # pygame.draw.circle(janela, VERMELHO, mouser_img, 10) #desenha um círculo vermelho no mouse
    # Desenha a imagem do cursor personalizado na posição do mouse
    
    # pygame.draw.polygon
    janela.blit(mouser_img, mouser_img_pos) #coloca a imagem do mouse na tela

    pygame.display.flip()  # Mostra o novo frame para o jogador

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
            game = False
            
    if vida == 0:
        game = False

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
    
    fonte_score = pygame.font.Font("util/fonte/upheavtt.ttf", 35) #cria uma fonte
    texto_score = fonte_score.render('Score {0}'.format(Score), True, PRETO) #cria um texto com a fonte criada
    texto_vidas = fonte_score.render('Vidas {0}'.format(vida), True, PRETO) #cria um texto com a fonte criada
    
    janela.blit(background, (0,0)) # fundo na janela
    janela.blit(texto_score, (100, 5))# texto da pontuação na janela
    janela.blit(texto_vidas, (700,5)) # texto das vidas na janela
    # faca_img_rect.center = pygame.mouse.get_pos()
    machado_img_rect.center = pygame.mouse.get_pos()  # coloquei o machado na posição do mouse
    # janela.blit(faca_img, faca_img_rect) 
    janela.blit(machado_img, machado_img_rect) # coloca o machado na janela na posição do mouse
    #------- Desenha bombas e logos
    todas_bombas.draw(janela)
    todas_logos.draw(janela)
    
    pygame.display.update()  # Mostra o novo frame para o jogador

# se o jogador apertar o botão de fechar a tela, o jogo fecha
if event.type != pygame.QUIT:    
    Tela_Game_Final = True
    tempo_maximo = 1  # tempo máximo para a tela de game over
    tempo_inicial = time.time()  # tempo inicial do jogo
    while Tela_Game_Final:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # sys.exit()

        screen = pygame.display.set_mode((LARGURA, ALTURA))  # cria a tela
        pygame.display.set_caption('Game Over')  # nome da tela
        font = pygame.font.Font("util/fonte/upheavtt.ttf", 60)
        text = font.render('Game Over', True, (200, 0, 0))  # cor do texto e escrita
        text_rect = text.get_rect(center=(LARGURA // 2, ALTURA // 2 - 10))  # posição do texto

        # ----- Gera saídas

        screen.fill((0, 0, 0)) # Preenche com a cor preta no fundo
        screen.blit(text, text_rect)  # coloca o texto na tela
        pygame.display.flip()  # atualiza a tela

        # Verificar se o tempo máximo foi atingido
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial  # tempo decorrido desde o início do jogo
        if tempo_decorrido >= tempo_maximo:
            game = False

            Tela_Game_Final = False

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