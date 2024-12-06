class Pessoa:
    def __init__(self, nome, idade):#está a defenir o construtor
        self.nome = nome #self= propria classe
        self.idade = idade #self= propria classe
 
    def saudacao(self):
        return f"O meu nome é {self.nome} e tenho {self.idade} anos."
     
class escola:
    def __init__(self, ba):
        self.ba = ba

    def saudacao(self):
         return f"o meu ba é {self.ba}."
    

class medida:
    def __init__(self,altura):
        self.altura = altura
    
    def alturas(self):
        return f"a minha altura é {self.altura}"
    

class medida_peso:
    def __init__(self,peso):
        self.peso = peso

    def peso_eu(self):
        return f"o meu peso é {self.peso}kg "
    
class morada:
    def __init__(self,casa):
        self.casa = casa

    def minha_morada(self):
        return f"a minha morada é {self.casa}"
    

class minha_escola:
    def  __init__(self,epbjc):
        self.escola = epbjc

    def a_minha_escola(self):
        return f"a minha escola é a {self.escola}"


class musica_favorita:
    def __init__(self,musica):
        self.musica = musica
    
    def musica_favorita(self):
        return f"a minha musica favorita é do {self.musica}"



    
