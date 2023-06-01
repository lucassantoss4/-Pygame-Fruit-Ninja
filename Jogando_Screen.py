from Importações import *

def Jogando(janela):
    
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    FPS = 60

    #variáveis do jogo
    Score = 0
    vida = 3 
    
    #------- transforma o mouse em machado
    pygame.mouse.set_visible(False) #tira o mouse da tela
    machado_img_rect = machado_img.get_rect() 

    #------------ Jogo -----------#
    
    game = True

    # ===== Loop principal =====
    while game:
        clock.tick(FPS)  # Limita o FPS do jogo
        
        for event in pygame.event.get():  # Obtém todos os eventos do Pygame
            if event.type == pygame.QUIT:  # Verifica se o evento é o de fechar a janela
                pygame.quit()
                sys.exit()
            
                
        if vida == 0:  # Verifica se a vida do jogador é igual a zero
            state = PERDEU #muda o estado para tela de game over
            game = False  # Encerra o jogo
            

        mouse_x, mouse_y = pygame.mouse.get_pos()  # Obtém a posição do mouse
        
        for logo in todas_logos:  # Percorre todos os objetos do grupo "todas_logos"
            if logo.rect.x < mouse_x < (logo.rect.x + ALTURA_OBJ) and logo.rect.y < mouse_y < (logo.rect.y + LARGURA_OBJ):
                # Verifica se a posição do mouse está dentro das coordenadas do objeto "logo"
                logo.kill()  # Remove o objeto do grupo
                Score += 100  # Incrementa a pontuação do jogador
                canal2.stop()
                canal2.play(random.choice(lista_hits))
                fumaca = Fumaca(logo.rect.center, lista_fumaca)  # Cria um objeto "Fumaca" na posição do objeto "logo"
                animacoes.add(fumaca)


            if logo.rect.x > LARGURA or logo.rect.x + LARGURA_OBJ < 0:
                # Verifica se o objeto "logo" está fora dos limites da tela horizontalmente
                Score -= 50 #Diminiu os 50 pontos se não corta o objeto
                logo.kill()  # Remove o objeto do grupo
            if logo.rect.y > ALTURA:
                Score -= 50 #Diminiu os 50 pontos se não corta o objeto
                # Verifica se o objeto "logo" está fora dos limites da tela verticalmente
                logo.kill()  # Remove o objeto do grupo

        for bomba in todas_bombas:  # Percorre todos os objetos do grupo "todas_bombas"
            if bomba.rect.x < mouse_x < (bomba.rect.x + ALTURA_OBJ) and bomba.rect.y < mouse_y < (bomba.rect.y + LARGURA_OBJ):
                # Verifica se a posição do mouse está dentro das coordenadas do objeto "bomba"
                bomba.kill()  # Remove o objeto do grupo
                vida -= 1  # Decrementa a vida do jogador
                fogo = Fogo(bomba.rect.center, lista_fogo)  # Cria um objeto "Fumaca" na posição do objeto "logo"
                animacoes.add(fogo)
            
                canal2.stop()
                canal3.stop()
                canal3.play(explosao)
            if bomba.rect.x > LARGURA or bomba.rect.x + LARGURA_OBJ < 0:
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
        animacoes.update() 
                
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
        animacoes.draw(janela)
        

        pygame.display.update()  # Atualiza a tela para o jogador ver o novo frame
        
    return state, Score
