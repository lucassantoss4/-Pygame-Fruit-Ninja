# ===== Inicialização =====
# ----- Importa e inicia pacotes
from Importações import *
from Constantes import *
from Jogando_Screen import *
from Init_Screen import*
from Gameover_screen import*


######## Música de fundo ########
canal1.play(musica_fundo, -1 )

state = INICIAR

while state != CANSOU:
    
    if state == INICIAR:
        #Tela de início
        state = Tela_Iniciar(janela, fundo_pixel, mouser_img) # chama a função para exibir a tela de início
        
    elif state == JOGAR:
        #Tela do jogo
        retornos = Jogando(janela)
        state = retornos[0]
        Score = retornos[1]   
    
    elif state == PERDEU:
        #Tela de Game
        state = Tela_Game_Over(LARGURA, ALTURA, Score)
    
    else:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                state = CANSOU


# ===== Finalização =====
pygame.quit()  # Encerra os recursos utilizados pelo Pygame
