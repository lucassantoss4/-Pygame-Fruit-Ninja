# ===== Inicialização =====
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

fundo_pixel = pygame.image.load('util/img/fundo_inicial.png.jpg').convert_alpha()
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


## -----SONS-------

pygame.mixer.music.load('util/sons/FRUIT-NINJA-fundo.mp3')
pygame.mixer.music.set_volume(0.4)



## -----SONS-------

canal1 = pygame.mixer.Channel(0)
canal2 = pygame.mixer.Channel(1)
canal3 = pygame.mixer.Channel(3)

musica_fundo = pygame.mixer.Sound('util/sons/FRUIT-NINJA-fundo.mp3')

explosao = pygame.mixer.Sound('util/sons/explode.mp3')

#hits
hit_0 = pygame.mixer.Sound('util/hits/hit0.mp3')

hit_1 = pygame.mixer.Sound('util/hits/hit1.mp3')

hit_2 = pygame.mixer.Sound('util/hits/hit2.mp3')

hit_3 = pygame.mixer.Sound('util/hits/hit3.mp3')

hit_4 = pygame.mixer.Sound('util/hits/hit4.mp3')

hit_5 = pygame.mixer.Sound('util/hits/hit5.mp3')

hit_6 = pygame.mixer.Sound('util/hits/hit6.mp3')

hit_7 = pygame.mixer.Sound('util/hits/hit7.mp3')

hit_8 = pygame.mixer.Sound('util/hits/hit8.mp3')

hit_9 = pygame.mixer.Sound('util/hits/hit9.mp3')

lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9]


# ----- Inicia estruturas de dados

#-----------------Classes-----------------#

class Fogo(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = lista_fogo

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
class Fumaca(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = lista_fumaca

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
            

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
        
            
class Fogo(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = lista_fogo

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center
                
class Fumaca(pygame.sprite.Sprite):
    # Construtor da classe.
    def __init__(self, center, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)

        # Armazena a animação de explosão
        self.explosion_anim = lista_fumaca

        # Inicia o processo de animação colocando a primeira imagem na tela.
        self.frame = 0  # Armazena o índice atual na animação
        self.image = self.explosion_anim[self.frame]  # Pega a primeira imagem
        self.rect = self.image.get_rect()
        self.rect.center = center  # Posiciona o centro da imagem

        # Guarda o tick da primeira imagem, ou seja, o momento em que a imagem foi mostrada
        self.last_update = pygame.time.get_ticks()

        # Controle de ticks de animação: troca de imagem a cada self.frame_ticks milissegundos.
        # Quando pygame.time.get_ticks() - self.last_update > self.frame_ticks a
        # próxima imagem da animação será mostrada
        self.frame_ticks = 50

    def update(self):
        # Verifica o tick atual.
        now = pygame.time.get_ticks()
        # Verifica quantos ticks se passaram desde a ultima mudança de frame.
        elapsed_ticks = now - self.last_update

        # Se já está na hora de mudar de imagem...
        if elapsed_ticks > self.frame_ticks:
            # Marca o tick da nova imagem.
            self.last_update = now

            # Avança um quadro.
            self.frame += 1

            # Verifica se já chegou no final da animação.
            if self.frame == len(self.explosion_anim):
                # Se sim, tchau explosão!
                self.kill()
            else:
                # Se ainda não chegou ao fim da explosão, troca de imagem.
                center = self.rect.center
                self.image = self.explosion_anim[self.frame]
                self.rect = self.image.get_rect()
                self.rect.center = center


# função para exibir a tela de game over
def Tela_Game_Over(LARGURA, ALTURA):
    Tela_Game_Final = True # variável para o loop da tela de game over
    tempo_maximo = 1  # tempo máximo para a tela de game over
    tempo_inicial = time.time()  # tempo inicial do jogo

    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen = pygame.display.set_mode((LARGURA, ALTURA))  # cria a tela
    pygame.display.set_caption('Game Over')  # nome da tela
    font = pygame.font.Font("util/fonte/upheavtt.ttf", 60)
    text = font.render('Game Over', True, (200, 0, 0))  # cor do texto e escrita
    text_rect = text.get_rect(center=(LARGURA // 2, ALTURA // 2 - 10))  # posição do texto

    # ----- Gera saídas

    screen.fill((0, 0, 0))  # Preenche com a cor preta no fundo
    screen.blit(text, text_rect)  # coloca o texto na tela
    pygame.display.flip()  # atualiza a tela
    
    
    
    while Tela_Game_Final: 

        # Verificar se o tempo máximo foi atingido
        tempo_atual = time.time()
        tempo_decorrido = tempo_atual - tempo_inicial  # tempo decorrido desde o início do jogo
        if tempo_decorrido >= tempo_maximo:
            Tela_Game_Final = False

# função para exibir a tela de game over
def Tela_Iniciar_Botao(janela, fundo_pixel, mouser_img):
    botao_inicia = True
    # Coordenadas e dimensões do retângulo
    x = 100
    y = 100
    largura_retangulo = 200
    altura_retangulo = 100
    retangulo = pygame.Rect(x, y, largura_retangulo, altura_retangulo)
    
    while botao_inicia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                botao_inicia = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    botao_inicia = False
        
        # Coordenadas e dimensões do retângulo

        mouser_img_pos = pygame.mouse.get_pos()  # obtem a posição do mouse para desenhar a imagem do mouse
        pygame.draw.rect(janela, (255, 0, 0), retangulo)  # desenha o retângulo na tela
        font = pygame.font.Font("util/fonte/upheavtt.ttf", 30)
        
        # ----- Gera saídas 
        janela.blit(fundo_pixel, (0, 0))  # coloca a imagem de fundo na tela
        janela.blit(mouser_img, mouser_img_pos)  # coloca a imagem do mouse na tela

        # Desenhe o cursor do mouse
        janela.blit(mouser_img, mouser_img_pos)  # coloca a imagem do mouse na tela

        pygame.display.flip()  # Mostra o novo frame para o jogador


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
machado_img_rect = machado_img.get_rect() 

#------------ Jogo -----------#
    
# Variável para o ajuste de velocidade
clock = pygame.time.Clock()
FPS = 60

#variáveis do jogo
Score = 0
vida = 3 


######### Tela de início #########


Loop =  True

while Loop:

    Tela_Iniciar_Botao(janela, fundo_pixel, mouser_img) # chama a função para exibir a tela de início

    game = True

    # ===== Loop principal =====
    canal1.play(musica_fundo, -1 )

    while game:
        clock.tick(FPS)  # Limita o FPS do jogo
        
        for event in pygame.event.get():  # Obtém todos os eventos do Pygame
            if event.type == pygame.QUIT:  # Verifica se o evento é o de fechar a janela
                pygame.quit()
                sys.exit()
                Loop = False
            
                
        if vida == 0:  # Verifica se a vida do jogador é igual a zero
            game = False  # Encerra o jogo

        mouse_x, mouse_y = pygame.mouse.get_pos()  # Obtém a posição do mouse
        
        for logo in todas_logos:  # Percorre todos os objetos do grupo "todas_logos"
            if logo.rect.x < mouse_x < (logo.rect.x + ALTURA_OBJ) and logo.rect.y < mouse_y < (logo.rect.y + LARGURA_OBJ):
                # Verifica se a posição do mouse está dentro das coordenadas do objeto "logo"
                logo.kill()  # Remove o objeto do grupo
                Score += 100  # Incrementa a pontuação do jogador
                canal2.stop()
                canal2.play(random.choice(lista_hits))
                # Fumaca(logo.rect.x, logo.rect.y)  # Cria um objeto "Fumaca" na posição do objeto "logo"

            if logo.rect.x > LARGURA or logo.rect.x - ALTURA_OBJ < 0:
                # Verifica se o objeto "logo" está fora dos limites da tela horizontalmente
                logo.kill()  # Remove o objeto do grupo
            if logo.rect.y > ALTURA:
                # Verifica se o objeto "logo" está fora dos limites da tela verticalmente
                logo.kill()  # Remove o objeto do grupo

        for bomba in todas_bombas:  # Percorre todos os objetos do grupo "todas_bombas"
            if bomba.rect.x < mouse_x < (bomba.rect.x + ALTURA_OBJ) and bomba.rect.y < mouse_y < (bomba.rect.y + LARGURA_OBJ):
                # Verifica se a posição do mouse está dentro das coordenadas do objeto "bomba"
                bomba.kill()  # Remove o objeto do grupo
                vida -= 1  # Decrementa a vida do jogador
                canal2.stop()
                canal3.stop()
                canal3.play(explosao)
            if bomba.rect.x > LARGURA or bomba.rect.x - ALTURA_OBJ < 0:
                # Verifica se o objeto "bomba" está fora dos limites da tela horizontalmente
                bomba.kill()  # Remove o objeto do grupo
            if bomba.rect.y > ALTURA:
                # Verifica se o objeto "bomba" está fora dos limites da tela verticalmente
                bomba.kill()  # Remove o objeto do grupo
                
        if len(todas_bombas) == 0 and len(todas_logos) == 0:
            # Verifica se não existem mais objetos nos grupos "todas_bombas" e "todas_logos"
            n_logos = random.randint(0, 6)  # Gera um número aleatório de logos
            n_bombas = random.randint(0, 2)  # Gera um número aleatório de bombas
            
            for i in range(n_bombas):
                # Cria e adiciona objetos do tipo "bomba" ao grupo "todas_bombas"
                bomba = Bombas(bomba_img)
                todas_bombas.add(bomba)

            for i in range(n_logos):
                # Cria e adiciona objetos do tipo "fruta" ao grupo "todas_logos"
                imagem = random.randint(0, 6)  # Escolhe uma imagem aleatória para a fruta
                fruta = Logos(lista_logos[imagem])
                todas_logos.add(fruta)        

        todas_bombas.update()  # Atualiza a posição e o estado dos objetos do grupo "todas_bombas"
        todas_logos.update()  # Atualiza a posição e o estado dos objetos do grupo "todas_logos"        
                
        fonte_score = pygame.font.Font("util/fonte/upheavtt.ttf", 35)  # Cria uma fonte para o texto
        texto_score = fonte_score.render('Score {0}'.format(Score), True, PRETO)  # Renderiza o texto da pontuação
        texto_vidas = fonte_score.render('Vidas {0}'.format(vida), True, PRETO)  # Renderiza o texto das vidas
        
        janela.blit(background, (0,0))  # Desenha o fundo na janela
        janela.blit(texto_score, (100, 5))  # Desenha o texto da pontuação na janela
        janela.blit(texto_vidas, (700,5))  # Desenha o texto das vidas na janela
        machado_img_rect.center = pygame.mouse.get_pos()  # Posiciona o machado na posição do mouse
        janela.blit(machado_img, machado_img_rect)  # Desenha o machado na janela na posição do mouse

        todas_bombas.draw(janela)  # Desenha todos os objetos do grupo "todas_bombas" na janela
        todas_logos.draw(janela)  # Desenha todos os objetos do grupo "todas_logos" na janela

        pygame.display.update()  # Atualiza a tela para o jogador ver o novo frame

    if event.type != pygame.QUIT:  # Verifica se o evento não é o de fechar a janela
        Tela_Game_Over(LARGURA, ALTURA)  # Exibe a tela de game over
        if event.type == event.type == pygame.KEYDOWN:
            game = True 
        

# ===== Finalização =====
pygame.quit()  # Encerra os recursos utilizados pelo Pygame


"""
Colocar score - OK
Fazer animações
criar loop 
Quebrar o código
"""
