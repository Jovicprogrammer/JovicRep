# duck typing = concept where the class of an object is less important than the methods/attributes
#               class type is not checked if minimum methods/attributes are present
#               “If it walks like a duck, and it quacks like a duck, then it must be a duck.”

class Pato:

    def andar(self):
        print("O pato está andando")

    def falar(self):
        print("O pato está fazendo quack")

class Galinha:

    def andar(self):
        print("A galinha está andando")

    def falar(self):
        print("A galinha está cacarejando")

class Pessoa():

    def pegar(self, pato): 
        pato.andar()
        pato.falar()
        print("Você pegou o bicho!")


pato = Pato()
galinha = Galinha()
pessoa = Pessoa()

pessoa.pegar(galinha)