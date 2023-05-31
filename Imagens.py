import pygame
from Constantes import *
from Tela_inicial import *

## Imagens
#imagem da bomba
bomba_img = pygame.image.load('util/img/BOMBA.png').convert_alpha()
bomba_img = pygame.transform.scale(bomba_img, (ALTURA_OBJ, LARGURA_OBJ))

#imagens do cursor
machado_img = pygame.image.load('util/img/MACHADO.png').convert_alpha()
machado_img = pygame.transform.scale(machado_img, (LARGURA_OBJ+10, ALTURA_OBJ+10))

mouser_img = pygame.image.load('util/img/MAO_MOSER.png').convert_alpha() # mouse
mouser_img = pygame.transform.scale(mouser_img, (LARGURA_OBJ, ALTURA_OBJ))

#imagens das Logos
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


#imagens de fundo
background = pygame.image.load('util/img/background_inteiro.png').convert() #carrega a imagem de fundo
background = pygame.transform.scale(background, (LARGURA, ALTURA)) # redimensiona a imagem de fundo

fundo_pixel = pygame.image.load('util/img/fundo_inicial.png.jpg').convert_alpha()
fundo_pixel = pygame.transform.scale(fundo_pixel, (LARGURA, ALTURA))

#listas das imagens
lista_logos = [adm_img, ccomp_img, direito_img, ecomp_img, econo_img, mec_img, mecat_img]
lista_fogo = [fogo4, fogo3, fogo2, fogo1]
lista_fumaca = [fumaca4, fumaca3, fumaca2, fumaca1]
