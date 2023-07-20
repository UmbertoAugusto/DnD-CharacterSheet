class personagem():
    def __init__(self):
        self.vida = 0
        self.caracteristicas = {}

class barbaro(personagem):
    def lvl1barbaro(self):
        self.vida = 10

class halforc(personagem):
    def halforc(self):
        self.caracteristicas['darkvision'] = 'explicacao de darkvision'
        self.darkvision

class sheet(barbaro,halforc):
    pass