import pygame
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

### IMAGENS

#logo da bomba
bomba_img = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_img = pygame.transform.scale(bomba_img, (ALTURA_OBJ, LARGURA_OBJ))

#logo da faca
faca_img = pygame.image.load('util/img/FACA.png').convert_alpha()
faca_img = pygame.transform.scale(faca_img, (ALTURA_OBJ, LARGURA_OBJ))

#logos dos cursos
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

mec_img = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_img = pygame.transform.scale(mec_img, (ALTURA_OBJ, LARGURA_OBJ))

mecat_img = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_img = pygame.transform.scale(mecat_img, (ALTURA_OBJ, LARGURA_OBJ))



###SONS

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

#listas
lista_logos = [adm_img, ccomp_img, direito_img, ecomp_img, econo_img, faca_img, mec_img, mecat_img]
lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9, hit_10]