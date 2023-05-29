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


#logo da faca
faca_img = pygame.image.load('util/img/FACA.png').convert_alpha()
faca_img = pygame.transform.scale(faca_img, (ALTURA_OBJ, LARGURA_OBJ))

#logo da bomba
bomba_1 = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_1 = pygame.transform.scale(bomba_1, (ALTURA_OBJ, LARGURA_OBJ))

bomba_2 = pygame.image.load('util/img/BOMBA_CORTE.png').convert_alpha()
bomba_2 = pygame.transform.scale(bomba_2, (ALTURA_OBJ, LARGURA_OBJ))

bomba_3 = pygame.image.load('util/img/BOMBA_MEIO.png').convert_alpha()
bomba_3 = pygame.transform.scale(bomba_3, (ALTURA_OBJ, LARGURA_OBJ))

#logos dos cursos
adm_1 = pygame.image.load('util/img/ADM.png').convert_alpha()
adm_1 = pygame.transform.scale(adm_1, (ALTURA_OBJ, LARGURA_OBJ))

adm_2 = pygame.image.load('util/img/ADM_CORTE.png').convert_alpha()
adm_2 = pygame.transform.scale(adm_2, (ALTURA_OBJ, LARGURA_OBJ))

adm_3 = pygame.image.load('util/img/ADM_MEIO.png').convert_alpha()
adm_3 = pygame.transform.scale(adm_3, (ALTURA_OBJ, LARGURA_OBJ))

ccomp_1 = pygame.image.load('util/img/CCOMP.png').convert_alpha()
ccomp_1 = pygame.transform.scale(ccomp_1, (ALTURA_OBJ, LARGURA_OBJ))

ccomp_2 = pygame.image.load('util/img/CCOMP_CORTE.png').convert_alpha()
ccomp_2 = pygame.transform.scale(ccomp_2, (ALTURA_OBJ, LARGURA_OBJ))

ccomp_3 = pygame.image.load('util/img/CCOMP_MEIO.png').convert_alpha()
ccomp_3 = pygame.transform.scale(ccomp_3, (ALTURA_OBJ, LARGURA_OBJ))

direito_1 = pygame.image.load('util/img/DIREITO.png').convert_alpha()
direito_1 = pygame.transform.scale(direito_1, (ALTURA_OBJ, LARGURA_OBJ))

direito_2 = pygame.image.load('util/img/DIREITO_CORTE.png').convert_alpha()
direito_2 = pygame.transform.scale(direito_2, (ALTURA_OBJ, LARGURA_OBJ))

direito_3 = pygame.image.load('util/img/DIREITO_MEIO.png').convert_alpha()
direito_3 = pygame.transform.scale(direito_3, (ALTURA_OBJ, LARGURA_OBJ))

ecomp_1 = pygame.image.load('util/img/ECOMP.png').convert_alpha()
ecomp_1 = pygame.transform.scale(ecomp_1, (ALTURA_OBJ, LARGURA_OBJ))

ecomp_2 = pygame.image.load('util/img/ECOMP_CORTE.png').convert_alpha()
ecomp_2 = pygame.transform.scale(ecomp_2, (ALTURA_OBJ, LARGURA_OBJ))

ecomp_3 = pygame.image.load('util/img/ECOMP_MEIO.png').convert_alpha()
ecomp_3 = pygame.transform.scale(ecomp_3, (ALTURA_OBJ, LARGURA_OBJ))

econo_1 = pygame.image.load('util/img/ECONO.png').convert_alpha()
econo_1 = pygame.transform.scale(econo_1, (ALTURA_OBJ, LARGURA_OBJ))

econo_2 = pygame.image.load('util/img/ECONO_CORTE.png').convert_alpha()
econo_2 = pygame.transform.scale(econo_2, (ALTURA_OBJ, LARGURA_OBJ))

econo_3 = pygame.image.load('util/img/ECONO_MEIO.png').convert_alpha()
econo_3 = pygame.transform.scale(econo_3, (ALTURA_OBJ, LARGURA_OBJ))

mec_1 = pygame.image.load('util/img/MEC.png').convert_alpha()
mec_1 = pygame.transform.scale(mec_1, (ALTURA_OBJ, LARGURA_OBJ))

mec_2 = pygame.image.load('util/img/MEC_CORTE.png').convert_alpha()
mec_2 = pygame.transform.scale(mec_2, (ALTURA_OBJ, LARGURA_OBJ))

mec_3 = pygame.image.load('util/img/MEC_MEIO.png').convert_alpha()
mec_3 = pygame.transform.scale(mec_3, (ALTURA_OBJ, LARGURA_OBJ))

mecat_1 = pygame.image.load('util/img/MECAT.png').convert_alpha()
mecat_1 = pygame.transform.scale(mecat_1, (ALTURA_OBJ, LARGURA_OBJ))

mecat_2 = pygame.image.load('util/img/MECAT_CORTE.png').convert_alpha()
mecat_2 = pygame.transform.scale(mecat_2, (ALTURA_OBJ, LARGURA_OBJ))

mecat_3 = pygame.image.load('util/img/MECAT_MEIO.png').convert_alpha()
mecat_3 = pygame.transform.scale(mecat_3, (ALTURA_OBJ, LARGURA_OBJ))



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
lista_logos = [adm_1, ccomp_1, direito_1, ecomp_1, econo_1, mec_1, mecat_1]
lista_cortes = [adm_2, ccomp_2, direito_2, ecomp_2, econo_2, mec_2, mecat_2]
lista_meio = [adm_3, ccomp_3, direito_3, ecomp_3, econo_3, mec_3, mecat_3]
lista_hits = [hit_0, hit_1, hit_2, hit_3, hit_4, hit_5, hit_6, hit_7, hit_8, hit_9, hit_10]