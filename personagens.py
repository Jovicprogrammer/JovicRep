
class Personagens:

    def __init__(self, nome, idade, genero, cor, origem):
        self.nome = nome
        self.idade = idade
        self.genero = genero
        self.cor = cor
        self.origem = origem 

    def andar (self):
        print (""+ self.nome+" está andando")

    def dormir (self):
        print (""+ self.nome+" está dormindo")

    
Paul = Personagens("Paul Python", 31, "masculino", "verde", "Python City")
Nadia = Personagens("Nadia Natrix", 30, "feminino", "laranja", "Python City")

print (Nadia.nome)