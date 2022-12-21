class AlunoAcademia ():
    def __init__(self, identificador, nome, idade, peso, altura):
        self._identificador = identificador
        self._nome = nome
        self._idade = idade
        self._peso = peso
        self._altura = altura


    @property
    def identificador(self):
        return self._identificador

    @identificador.setter
    def setidentificador (self, identificador):
        self._identificador = identificador 
 

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def setnome (self,nome):
        self._nome = nome

    @property
    def idade (self):
        return (self._idade)

    @idade.setter
    def setidade (self, idade):
        self._idade = idade

    @property
    def peso (self):
        return self._peso

    @peso.setter
    def setpeso (self, peso):
        self._peso = peso

    @property
    def altura (self):
        return self._altura

    @altura.setter
    def setaltura (self, altura):
        self._altura = altura

    @property
    def CalcularIMC (self):
        altura_quadrado = self.altura*self._altura
        divisao = self._peso // altura_quadrado
        imc = float(divisao)
        print(imc)
        
    @property
    def Imprime (self):
        print (f' O ID é {self._identificador}, O nome é {self._nome}, A idade é {self._idade}, O peso é {self._peso} E a altura é {self._altura}')


odair = AlunoAcademia(691, "Odair", 25, 80.0, 1.76)

odair.CalcularIMC

odair.Imprime

odair.nome()

    



    