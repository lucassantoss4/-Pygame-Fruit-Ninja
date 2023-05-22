#criando a classe de logos
class Logos(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA-50) #as 'frutinhas' não são lançadas no canto
        self.rect.y = 600 #as 'frutinhas' são lançadas de baixo
    
        #quantidade de frutas lançadas
        self.qtd = random.randint(0, 6)
        
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-2, 2)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-4, -6)
        
        def update(self):
            #vai atualizar as posições das frutas    
            self.rect.x += self.speedx
            self.rect.y += self.speedy
            
        
#usar a mesma lógica para construir a série de bombas
class Bombas(pygame.sprite.Sprite):
    def __init__(self, img):
        # Construtor da classe mãe (Sprite).
        pygame.sprite.Sprite.__init__(self)
        
        self.image = img
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(50, LARGURA-50) #as bombas não são lançadas no canto
        self.rect.y = 600 #as bombas são lançadas de baixo
        
        #vão ser lançadas 0, 1 ou duas bombas cada vez
        self.qtd = random.randint(0, 2)
        
        #a velocidade tem que mudar de sentido em algum momento 
        #no eixo x a velocidade inicial pode ser positiva ou negativa, mas não quero velocidades tõ diferentes 
        self.speedx = random.randint(-2, 2)
        #no eixo y eu quero que as velocidades não sejam tão diferentes
        self.speedy = random.randint(-4, -6)
        
        



### problemas/coias que a gabi pensou

        """
        
Falta fazer o update de cada classe
não sei como imitar o efeito de queda livre (fazer a fruta desacelerar)

eu quero que as frutas sejam lançadas de novo 
somente quando todas as outras frutas (lançadas anteriormente) 
tiverem saído da tela      

as frutas não precisam ser lançadas todas ao mesmo tempo, pode ter um 
intervalo de lançameto entre elas, teria como fazer isso?  




        """