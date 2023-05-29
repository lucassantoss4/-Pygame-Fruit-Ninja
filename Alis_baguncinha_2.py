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

'''#logo da bomba
bomba_1 = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_1 = pygame.transform.scale(bomba_1, (LARGURA_OBJ-5, ALTURA_OBJ-5))

bomba_2 = pygame.image.load('util/img/BOMBA_CORTE.png').convert_alpha()
bomba_2 = pygame.transform.scale(bomba_2, (LARGURA_OBJ-5, ALTURA_OBJ-5))

bomba_3 = pygame.image.load('util/img/BOMBA_MEIO.png').convert_alpha()
bomba_3 = pygame.transform.scale(bomba_3, (LARGURA_OBJ-5, ALTURA_OBJ-5))

#logos dos cursos
adm_1 = pygame.image.load('util/img/ADM.png').convert_alpha()
adm_1 = pygame.transform.scale(adm_1, (LARGURA_OBJ, ALTURA_OBJ))

adm_2 = pygame.image.load('util/img/ADM_CORTE.png').convert_alpha()
adm_2 = pygame.transform.scale(adm_2, (LARGURA_OBJ, ALTURA_OBJ))

adm_3 = pygame.image.load('util/img/ADM_MEIO.png').convert_alpha()
adm_3 = pygame.transform.scale(adm_3, (LARGURA_OBJ, ALTURA_OBJ))

ccomp_1 = pygame.image.load('util/img/CCOMP.png').convert_alpha()
ccomp_1 = pygame.transform.scale(ccomp_1, (LARGURA_OBJ-5, ALTURA_OBJ-5))

ccomp_2 = pygame.image.load('util/img/CCOMP_CORTE.png').convert_alpha()
ccomp_2 = pygame.transform.scale(ccomp_2, (LARGURA_OBJ-5, ALTURA_OBJ-5))

ccomp_3 = pygame.image.load('util/img/CCOMP_MEIO.png').convert_alpha()
ccomp_3 = pygame.transform.scale(ccomp_3, (LARGURA_OBJ-5, ALTURA_OBJ-5))

direito_1 = pygame.image.load('util/img/DIREITO.png').convert_alpha()
direito_1 = pygame.transform.scale(direito_1, (LARGURA_OBJ+10, ALTURA_OBJ))

direito_2 = pygame.image.load('util/img/DIREITO_CORTE.png').convert_alpha()
direito_2 = pygame.transform.scale(direito_2, (LARGURA_OBJ+10, ALTURA_OBJ))

direito_3 = pygame.image.load('util/img/DIREITO_MEIO.png').convert_alpha()
direito_3 = pygame.transform.scale(direito_3, (LARGURA_OBJ+10, ALTURA_OBJ))

ecomp_1 = pygame.image.load('util/img/ECOMP.png').convert_alpha()
ecomp_1 = pygame.transform.scale(ecomp_1, (LARGURA_OBJ-10, ALTURA_OBJ+10))

ecomp_2 = pygame.image.load('util/img/ECOMP_CORTE.png').convert_alpha()
ecomp_2 = pygame.transform.scale(ecomp_2, (LARGURA_OBJ-10, ALTURA_OBJ+10))

ecomp_3 = pygame.image.load('util/img/ECOMP_MEIO.png').convert_alpha()
ecomp_3 = pygame.transform.scale(ecomp_3, (LARGURA_OBJ-10, ALTURA_OBJ+10))

econo_1 = pygame.image.load('util/img/ECONO.png').convert_alpha()
econo_1 = pygame.transform.scale(econo_1, (LARGURA_OBJ+7, ALTURA_OBJ+7))

econo_2 = pygame.image.load('util/img/ECONO_CORTE.png').convert_alpha()
econo_2 = pygame.transform.scale(econo_2, (LARGURA_OBJ+7, ALTURA_OBJ+7))

econo_3 = pygame.image.load('util/img/ECONO_MEIO.png').convert_alpha()
econo_3 = pygame.transform.scale(econo_3, (LARGURA_OBJ+7, ALTURA_OBJ+7))

mec_1 = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_1 = pygame.transform.scale(mec_1, (LARGURA_OBJ, ALTURA_OBJ))

mec_2 = pygame.image.load('util/img/MEC_CORTE.png').convert_alpha()
mec_2 = pygame.transform.scale(mec_2, (LARGURA_OBJ, ALTURA_OBJ))

mec_3 = pygame.image.load('util/img/MEC_MEIO.png').convert_alpha()
mec_3 = pygame.transform.scale(mec_3, (LARGURA_OBJ, ALTURA_OBJ))

mecat_1 = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_1 = pygame.transform.scale(mecat_1, (LARGURA_OBJ, ALTURA_OBJ))

mecat_2 = pygame.image.load('util/img/MECAT_CORTE.png').convert_alpha()
mecat_2 = pygame.transform.scale(mecat_2, (LARGURA_OBJ, ALTURA_OBJ))

mecat_3 = pygame.image.load('util/img/MECAT_MEIO.png').convert_alpha()
mecat_3 = pygame.transform.scale(mecat_3, (LARGURA_OBJ, ALTURA_OBJ))

lista_logos = [adm_1, ccomp_1, direito_1, ecomp_1, econo_1, mec_1, mecat_1]
lista_cortes = [adm_2, ccomp_2, direito_2, ecomp_2, econo_2, mec_2, mecat_2]
lista_meio = [adm_3, ccomp_3, direito_3, ecomp_3, econo_3, mec_3, mecat_3]
'''

## -----SONS-------

pygame.mixer.music.load('util/sons/FRUIT-NINJA-fundo.mp3')
pygame.mixer.music.set_volume(0.4)

#hits
hit_0 = pygame.mixer.music.load('util/hits/hit0.mp3')
hit_0 = pygame.mixer.music.set_volume(0.4)

hit_1 = pygame.mixer.music.load('util/hits/hit_1.mp3')
hit_1 = pygame.mixer.music.set_volume(0.4)

hit_2 = pygame.mixer.music.load('util/hits/hit2.mp3')
hit_2 = pygame.mixer.music.set_volume(0.4)

hit_3 = pygame.mixer.music.load('util/hits/hit3.mp3')
hit_3 = pygame.mixer.music.set_volume(0.4)

hit_4 = pygame.mixer.music.load('util/hits/hit4.mp3')
hit_4 = pygame.mixer.music.set_volume(0.4)

hit_5 = pygame.mixer.music.load('util/hits/hit5.mp3')
hit_5 = pygame.mixer.music.set_volume(0.4)

hit_6 = pygame.mixer.music.load('util/hits/hit6.mp3')
hit_6 = pygame.mixer.music.set_volume(0.4)

hit_7 = pygame.mixer.music.load('util/hits/hit7.mp3')
hit_7 = pygame.mixer.music.set_volume(0.4)

hit_8 = pygame.mixer.music.load('util/hits/hit8.mp3')
hit_8 = pygame.mixer.music.set_volume(0.4)

hit_9 = pygame.mixer.music.load('util/hits/hit9.mp3')
hit_9 = pygame.mixer.music.set_volume(0.4)

hit_10 = pygame.mixer.music.load('util/hits/hit10.mp3')
hit_10 = pygame.mixer.music.set_volume(0.4)

lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9, hit_10]

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
    bomba = Bombas(bomba_1)
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
            pygame.mixer.music.play(loops=-1)
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
            bomba = Bombas(bomba_1)
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