def aguardar_botao_iniciar(janela, fundo_pixel, mouser_img):
    botao_inicia = True

    while botao_inicia:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.MOUSEBUTTONDOWN:
                botao_inicia = False

        mouser_img_pos = pygame.mouse.get_pos()  # obtem a posição do mouse para desenhar a imagem do mouse

        # ----- Gera saídas
        janela.blit(fundo_pixel, (0, 0))  # coloca a imagem de fundo na tela

        # Desenhe o cursor do mouse
        janela.blit(mouser_img, mouser_img_pos)  # coloca a imagem do mouse na tela

        pygame.display.flip()  # Mostra o novo frame para o jogador

janela = pygame.display.set_mode((LARGURA, ALTURA))
fundo_pixel = pygame.Surface((LARGURA, ALTURA))
# mouser_img = pygame.Surface((10, 10))  # Substitua pelo caminho da imagem do cursor personalizado
aguardar_botao_iniciar(janela, fundo_pixel, mouser_img)