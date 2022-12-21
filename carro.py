
class Carro:
    def __init__(self, modelo, cor, consumo):
        self.modelo = modelo
        self.cor = cor
        self.consumo = consumo
        self.tanque_litros = 0


    def pintar(self, sua_cor):
        sua_cor = int(input("Escolha: [1]PRATA; [2]PRETA; [3]BRANCO [4]CROMADA"))
        if sua_cor != 1 and sua_cor != 2 and sua_cor != 3 and sua_cor != 4:
            print ("Cor não disponível!")
        else:
            lista_de_cor = [0, "Prata", "Preto", "Branco", "Cromada"]
            self.cor = lista_de_cor[sua_cor]

    def pintado (self):
        return f'A cor do seu carro é {self.cor}'

    def verificar_tanque (self, litros):
        capacidade_tanque = 40
        if ((self.tanque_litros + litros) <= capacidade_tanque):
            return litros
        else:
            return (capacidade_tanque - self.tanque_litros)        

    def abastecer (self, litros):
        abastecer = self.verificar_tanque(litros)
        self.tanque_litros += abastecer
        print (f"Seu tanque foi abastecido em {litros} litros de combustivel e tem {self.tanque_litros} litros.")

    def pode_andar(self, distancia):
        consumo = (distancia/self.consumo)
        return (self.tanque_litros >= consumo)

    def andar(self, distancia_percorrida):
        if (self.pode_andar(distancia_percorrida)):
            self.tanque_litros -= (distancia_percorrida/self.consumo)
        else:
            print ("Combustivel insuficiente para andar {distancia} Km!")
            
    def mostrar_tanque(self):
        print (f'Restam {self.tanque_litros} litros de combustivel no tanque!!')

monster = Carro("Carro Monstro", "Vermelho", 30)
monster.pintar(0)
print(monster.pintado())
monster.abastecer(8)
monster.andar(20)
monster.mostrar_tanque()


            







 

