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


#logo machado

machado_img = pygame.image.load('util/img/MACHADO.png').convert_alpha()
machado_img = pygame.transform.scale(machado_img, (LARGURA_OBJ+10, ALTURA_OBJ+10))

#logo da bomba
bomba_1 = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_1 = pygame.transform.scale(bomba_1, (ALTURA_OBJ, LARGURA_OBJ))

#logos dos cursos
adm_1 = pygame.image.load('util/img/ADM.png').convert_alpha()
adm_1 = pygame.transform.scale(adm_1, (ALTURA_OBJ, LARGURA_OBJ))

ccomp_1 = pygame.image.load('util/img/CCOMP.png').convert_alpha()
ccomp_1 = pygame.transform.scale(ccomp_1, (ALTURA_OBJ, LARGURA_OBJ))

direito_1 = pygame.image.load('util/img/DIREITO.png').convert_alpha()
direito_1 = pygame.transform.scale(direito_1, (ALTURA_OBJ, LARGURA_OBJ))

ecomp_1 = pygame.image.load('util/img/ECOMP.png').convert_alpha()
ecomp_1 = pygame.transform.scale(ecomp_1, (ALTURA_OBJ, LARGURA_OBJ))

econo_1 = pygame.image.load('util/img/ECONO.png').convert_alpha()
econo_1 = pygame.transform.scale(econo_1, (ALTURA_OBJ, LARGURA_OBJ))

mec_1 = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_1 = pygame.transform.scale(mec_1, (ALTURA_OBJ, LARGURA_OBJ))

mecat_1 = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_1 = pygame.transform.scale(mecat_1, (ALTURA_OBJ, LARGURA_OBJ))

###SONS

# #hits
# hit_0 = pygame.mixer.music.load('util/hits/hit0.mp3')
# hit_0 = pygame.mixer.music.set_volume(0.4)

# hit_1 = pygame.mixer.music.load('util/hits/hit_1.mp3')
# hit_1 = pygame.mixer.music.set_volume(0.4)

# hit_2 = pygame.mixer.music.load('util/hits/hit2.mp3')
# hit_2 = pygame.mixer.music.set_volume(0.4)

# hit_3 = pygame.mixer.music.load('util/hits/hit3.mp3')
# hit_3 = pygame.mixer.music.set_volume(0.4)

# hit_4 = pygame.mixer.music.load('util/hits/hit4.mp3')
# hit_4 = pygame.mixer.music.set_volume(0.4)

# hit_5 = pygame.mixer.music.load('util/hits/hit5.mp3')
# hit_5 = pygame.mixer.music.set_volume(0.4)

# hit_6 = pygame.mixer.music.load('util/hits/hit6.mp3')
# hit_6 = pygame.mixer.music.set_volume(0.4)

# hit_7 = pygame.mixer.music.load('util/hits/hit7.mp3')
# hit_7 = pygame.mixer.music.set_volume(0.4)

# hit_8 = pygame.mixer.music.load('util/hits/hit8.mp3')
# hit_8 = pygame.mixer.music.set_volume(0.4)

# hit_9 = pygame.mixer.music.load('util/hits/hit9.mp3')
# hit_9 = pygame.mixer.music.set_volume(0.4)

# hit_10 = pygame.mixer.music.load('util/hits/hit10.mp3')
# hit_10 = pygame.mixer.music.set_volume(0.4)

#listas
lista_logos = [adm_1, ccomp_1, direito_1, ecomp_1, econo_1, mec_1, mecat_1]
# lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9, hit_10]


#FOGO E FUMACA
fogo1 = pygame.image.load('util/img/FOGO1.png').convert_alpha()
fogo1 = pygame.transform.scale(fogo1, (ALTURA_OBJ, LARGURA_OBJ))

fogo2 = pygame.image.load('util/img/FOGO2.png').convert_alpha()
fogo2 = pygame.transform.scale(fogo2, (ALTURA_OBJ, LARGURA_OBJ))

fogo3 = pygame.image.load('util/img/FOGO3.png').convert_alpha()
fogo3 = pygame.transform.scale(fogo3, (ALTURA_OBJ, LARGURA_OBJ))

fogo4 = pygame.image.load('util/img/FOGO4.png').convert_alpha()
fogo4 = pygame.transform.scale(fogo4, (ALTURA_OBJ, LARGURA_OBJ))

fumaca1 = pygame.image.load('util/img/FUMACA1.png').convert_alpha()
fumaca1 = pygame.transform.scale(fumaca1, (ALTURA_OBJ, LARGURA_OBJ))

fumaca2 = pygame.image.load('util/img/FUMACA2.png').convert_alpha()
fumaca2 = pygame.transform.scale(fumaca2, (ALTURA_OBJ, LARGURA_OBJ))

fumaca3 = pygame.image.load('util/img/FUMACA3.png').convert_alpha()
fumaca3 = pygame.transform.scale(fumaca3, (ALTURA_OBJ, LARGURA_OBJ))

fumaca4 = pygame.image.load('util/img/FUMACA4.png').convert_alpha()
fumaca4 = pygame.transform.scale(fumaca4, (ALTURA_OBJ, LARGURA_OBJ))

lista_fogo = [fogo4, fogo3, fogo2, fogo1]
lista_fumaca = [fumaca4, fumaca3, fumaca2, fumaca1]

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
                    game = False
                if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    if self.botao_reiniciar < mouse_x < self.botao_reiniciar + self.largura and self.botao_reiniciar < mouse_y < self.botao_reiniciar + self.altura:
                        self.reiniciar = True

            self.screen.fill((0, 0, 0))
            self.screen.blit(self.text, self.text_rect)
            pygame.draw.rect(self.screen, (255, 255, 255), self.botao_reiniciar)
            self.screen.blit(self.botao_reiniciar_texto, self.botao_reiniciar_texto_rect)
            pygame.display.flip()
            
            
# class Fogo(pygame.sprite.Sprite):
#     # Construtor da classe.
#     def __init__(self, center, img):
#         # Construtor da classe mãe (Sprite).
#         pygame.sprite.Sprite.__init__(self)

#         # Armazena a animação de explosão
#         self.explosion_anim = lista_fogo

#         # Inicia o processo de animação colocando a primeira imagem na tela.
#         self.frame = 0  # Armazena o índice atual na animação
#         self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
#         self.rect = self.image.get_rect()
#         self.rect.center = center  # Posiciona o centro da imagem

#         # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
#         self.last_update = pygame.time.get_ticks()

#         # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
#         # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
#         # próxima imagem da animação será mostrada
#         self.frame_ticks = 50

#     def update(self):
#         # Verifica o tick atual.
#         now = pygame.time.get_ticks()
#         # Verifica quantos ticks se passaram desde a ultima mudança de frame.
#         elapsed_ticks = now - self.last_update

#         # Se já está na hora de mudar de imagem...
#         if elapsed_ticks > self.frame_ticks:
#             # Marca o tick da nova imagem.
#             self.last_update = now

#             # Avança um quadro.
#             self.frame += 1

#             # Verifica se já chegou no final da animação.
#             if self.frame == len(self.explosion_anim):
#                 # Se sim, tchau explosão!
#                 self.kill()
#             else:
#                 # Se ainda não chegou ao fim da explosão, troca de imagem.
#                 center = self.rect.center
#                 self.image = self.explosion_anim[self.frame]
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center
                
# class Fumaca(pygame.sprite.Sprite):
#     # Construtor da classe.
#     def __init__(self, center, img):
#         # Construtor da classe mãe (Sprite).
#         pygame.sprite.Sprite.__init__(self)

#         # Armazena a animação de explosão
#         self.explosion_anim = lista_fumaca

#         # Inicia o processo de animação colocando a primeira imagem na tela.
#         self.frame = 0  # Armazena o índice atual na animação
#         self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
#         self.rect = self.image.get_rect()
#         self.rect.center = center  # Posiciona o centro da imagem

#         # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
#         self.last_update = pygame.time.get_ticks()

#         # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
#         # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
#         # próxima imagem da animação será mostrada
#         self.frame_ticks = 50

#     def update(self):
#         # Verifica o tick atual.
#         now = pygame.time.get_ticks()
#         # Verifica quantos ticks se passaram desde a ultima mudança de frame.
#         elapsed_ticks = now - self.last_update

#         # Se já está na hora de mudar de imagem...
#         if elapsed_ticks > self.frame_ticks:
#             # Marca o tick da nova imagem.
#             self.last_update = now

#             # Avança um quadro.
#             self.frame += 1

#             # Verifica se já chegou no final da animação.
#             if self.frame == len(self.explosion_anim):
#                 # Se sim, tchau explosão!
#                 self.kill()
#             else:
#                 # Se ainda não chegou ao fim da explosão, troca de imagem.
#                 center = self.rect.center
#                 self.image = self.explosion_anim[self.frame]
#                 self.rect = self.image.get_rect()
#                 self.rect.center = center
                
# class Machado(pygame.sprite.Sprite):
#     def __init__(self, img):
        
        
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
machado_img_rect = machado_img.get_rect()


#------------ Jogo -----------#
    
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 40

#variáveis do jogo
Score = 0
vida = 3

game = True

# ===== Loop principal =====
# pygame.mixer.music.play(loops=-1) #para tocar a música de fundo em loop

while game:
    #definindo tempo para execução do loop
    clock.tick(FPS)
    
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False
            
    if vida == 0:
        game_over_screen = GameOverScreen(LARGURA, ALTURA, 1)  # escreve "Game Over" por # segundos e encessa o jogo
        game_over_screen.run()

    todas_bombas.update()
    todas_logos.update()
    
    
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