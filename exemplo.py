class personagem():
    '''Sugestão para criar uma classe que sirva de base para todo o resto. Nela, definiriamos todas as coisas que um personagem precisa ter, tipo as características
    (como darkvision), nome do personagem (e outras coisas de lore), vida, AC etc. Aqui, podemos definir tudo zerado ou vazio e quando o usuario escolher uma classe pro
    seu personagem, ai atribuimos valores de fato.'''
    def __init__(self):
        self.vida = 0
        self.caracteristicas = {}

class barbaro(personagem):
    '''Para as classes do jogo, podemos criar uma class para cada uma. Minha sugestão é não ter um método __init__ aqui, apenas métodos para quando o usuário upar de nivel.
    Assim, sempre q ele upar de nivel, as mudanças ocorrem baseado nisso aqui. Talvez seja interessante definir alguma interface gráfica para o usuário poder fazer as esoclhas
    que ele precisa'''
    def lvl1barbaro(self):
        self.vida = 10

class halforc(personagem):
    '''Também acho legal criarmos class para cada raça e, no nível 1, o usuário escolhe qual raça ele vai querer pro personagem. Também acho melhor não ter um método __init__
    e sim um só metodo para quando o usuário escolhar essa raça.'''
    def halforc(self):
        self.caracteristicas['darkvision'] = 'explicacao de darkvision'
        self.darkvision

class sheet(barbaro,halforc):
    '''Aqui seria onde definiriamos de fato a caracter sheet. Quase todas as coisas do tkinter podem ser criadas aqui e essa seria a class que nós usuríamos para rodas o
    programa. Ela herda todas as class ja criadas para que o usuário possa escolher livremente.'''
    pass


#CHEGUEIII