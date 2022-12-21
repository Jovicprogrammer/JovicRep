#Lembrando que:
# snake_case para variáveis, funções e métodos;
# PascalCase para classes;
#============================================================
# Crie um ambiente O.O. completo utilizando classes e métodos:
# Na classe Livraria sub-classes Revista e Livro sabemos que:
# atributos: nome, Número de páginas, Idioma, Editora, tipo e status
# todos atributos encapsulados fortemente
# métodos para:
# controlar o aluguel dos livros, calculo do aluguel em (07)dias
# controlar a venda dos livros
# OBS: Lembre-se de fazer os GETs e SETs
# OBS: Não esqueça das validações
# OBS: Sempre que acontecer um aluguel ou venda diminuir do estoque.
# OBS: Faça a impressão dos elementos

import datetime
import re 

class Livraria():
    def __init__(self, titulo, num_paginas, idioma, editora, preco, tipo, status):
            self.__titulo = titulo
            self.__num_paginas = num_paginas
            self.__idioma = idioma
            self.__editora = editora
            self.__preco = preco
            self.__tipo = tipo 
            self.__status = status
    

#--------------------------------------revista-----------------------------------------------------
            
class Revista(Livraria):
        def __init__(self, titulo, num_paginas, idioma, editora, preco, tipo, status):
              super().__init__(titulo, num_paginas, idioma, editora, preco, tipo, status)

        @property
        def titulo (self):
            return self.__titulo

        @property 
        def num_paginas (self):
            return self.__num_paginas

        @property
        def idioma (self):
            return self.__idioma

        @property
        def editora (self):
            return self.__editora 

        @property
        def preco (self):
            return self.__preco

        @property
        def tipo (self):
            return self.__tipo 

        @property
        def status (self):
            return self.__status

        @titulo.setter
        def titulo (self, titulo_alterado):
            if type(titulo_alterado) == type(str):
                self.titulo = titulo_alterado
            else:
                ("Preencha com um titulo valido")
        
        @num_paginas.setter
        def num_paginas (self, nova_quantidade):
            if type (nova_quantidade) == type(int):
                self.num_paginas = nova_quantidade
            else:
                ("Preencha com uma quantidade valida")

        @idioma.setter
        def idioma (self, alteracao_idioma):
            if alteracao_idioma != 1 and alteracao_idioma != 2 and alteracao_idioma != 3 and alteracao_idioma != 4 and alteracao_idioma != 5 and type(alteracao_idioma) != type(int):
                print("Idioma não Disponível, escolha 1 para 'portugues'") 
                ("2 para 'Ingles'")
                ("3 para 'Espanhol") 
                ("4 para 'Tcheco'")
                ("e 5 para 'Albanes'")
            else:
                lista_de_idiomas = [0, "Portugues", "Ingles", "Espanhol", "Tcheco", "Albanes"]
                self.__idioma = lista_de_idiomas[alteracao_idioma]

        @editora.setter
        def editora (self, alterando_editora):
            if type (alterando_editora) != type(str):
                print ("Preencha com algo valido")
            else:
                self.editora = alterando_editora

        @preco.setter
        def preco (self, alterando_preco):
            if type (alterando_preco) == type(float):
                self.__preco = alterando_preco
            else:
                print ("Digite um valor valido")

        @tipo.setter
        def tipo (self, tipo_novo):
            if tipo_novo != 1 and tipo_novo != 2 and type(tipo_novo) != type(int):
                print ("Configuracao nao disponivel, escolha 1 para 'Para Aluguel' ou 2 para 'Para Venda'")
            else:
                opcoes_de_tipo = [0, "Para Aluguel", "Para Venda"]
                self.tipo == opcoes_de_tipo[tipo_novo]

        @status.setter 
        def status (self, alterando_status):
                if type (alterando_status) == type(bool):
                    self.__status = alterando_status
                else:
                    print ("Operação nao Disponivel")

        def alugar (self):
            if self.__tipo == 2:
                print ("{} so esta disponivel para venda".format(self.__titulo))
            elif self.__tipo == 1:
                self.__status = False 
                print ("Você alugou a revista {}".format(self.__titulo))
                print ("Sua conta inicial é de {}".format(self.__preco))
            else:
                ("Operação não Disponivel")

        def vender (self):
            if self.__tipo == 1:
                print ("{} nao esta disponivel para venda".format(self.__titulo))
            elif self.__tipo == 2:
                self.__status = False 
                print ("Você adquiriu {}".format(self.__titulo))
                print ("Sua conta é de R${}".format(self.__preco))
            else:
                ("Operação não Disponivel")

        def verificar_estoque_aluguel (self):
            if self.__tipo == 1:
                if self.__status == True:
                    print ("{} esta disponivel para aluguel".format(self.__titulo))
                elif self.__status == False:
                    print ("{} esta Indisponivel no momento".format(self.__titulo))
                else:
                    print ("Operação nao Disponivel")
            if self.__tipo == 2:
                print ("{} so esta disponivel para venda".format(self.__titulo))

        def verificar_estoque_venda (self):
            if self.tipo == 2:
                if self.__status == True:
                    print ("{} esta disponivel para venda".format(self.__titulo))
                elif self.__status == False:
                    print ("{} esta fora de estoque".format(self.__titulo))
                else:
                    print ("Operacao nao Disponivel")
            if self.__tipo == 1:
                print ("{} so esta disponivel para aluguel".format(self.__titulo))

#---------------------------------livro--------------------------------------------------------
class Livro(Livraria):
    def __init__(self, titulo, num_paginas, idioma, editora, preco, tipo, status):
          super().__init__(titulo, num_paginas, idioma, editora, preco, tipo, status)

@property
def titulo (self):
        return self.__titulo

@property 
def num_paginas (self):
    return self.__num_paginas

@property
def idioma (self):          
        return self.__idioma

@property
def editora (self):
                return self.__editora 

@property
def preco (self):
    return self.__preco

@property
def tipo (self):
    return self.__tipo 

@property
def status (self):
    return self.__status

@titulo.setter
def titulo (self, titulo_alterado):
                if type(titulo_alterado) == type(str):
                    self.titulo = titulo_alterado
                else:
                    ("Preencha com um titulo valido")
            
@num_paginas.setter
def num_paginas (self, nova_quantidade):
                if type (nova_quantidade) == type(int):
                    self.num_paginas = nova_quantidade
                else:
                    ("Preencha com uma quantidade valida")

@idioma.setter
def idioma (self, alteracao_idioma):
                if alteracao_idioma != 1 and alteracao_idioma != 2 and alteracao_idioma != 3 and alteracao_idioma != 4 and alteracao_idioma != 5 and type(alteracao_idioma) != type(int):
                    print("Idioma não Disponível, escolha 1 para 'portugues'") 
                    ("2 para 'Ingles'")
                    ("3 para 'Espanhol") 
                    ("4 para 'Tcheco'")
                    ("e 5 para 'Albanes'")
                else:
                    lista_de_idiomas = [0, "Portugues", "Ingles", "Espanhol", "Tcheco", "Albanes"]
                    self.__idioma = lista_de_idiomas[alteracao_idioma]

@editora.setter
def editora (self, alterando_editora):
                if type (alterando_editora) != type(str):
                    print ("Preencha com algo valido")
                else:
                    self.editora = alterando_editora

@preco.setter
def preco (self, alterando_preco):
                if type (alterando_preco) == type(float):
                    self.__preco = alterando_preco
                else:
                    print ("Digite um valor valido")

@tipo.setter
def tipo (self, tipo_novo):
                if tipo_novo != 1 and tipo_novo != 2 and type(tipo_novo) != type(int):
                    print ("Configuracao nao disponivel, escolha 1 para 'Para Aluguel' ou 2 para 'Para Venda'")
                else:
                    opcoes_de_tipo = [0, "Para Aluguel", "Para Venda"]
                    self.tipo == opcoes_de_tipo[tipo_novo]

@status.setter 
def status (self, alterando_status):
                    if type (alterando_status) == type(bool):
                        self.__status = alterando_status
                    else:
                        print ("Operação nao Disponivel")

def alugar (self):
                if self.__tipo == 2:
                    print ("{} so esta disponivel para venda".format(self.__titulo))
                elif self.__tipo == 1:
                    self.__status = False 
                    print ("Você alugou a revista {}".format(self.__titulo))
                    print ("Sua conta inicial é de {}".format(self.__preco))
                else:
                    print ("Operação não Disponivel")

def vender (self):
            if self.__tipo == 1:
                print ("{} so esta disponivel para aluguel".format(self.__titulo))
            elif self.__tipo == 2:
                self.__status = False 
            print ("Você adquiriu o livro {}".format(self.__titulo))
            print ("Sua conta é de R${}".format(self.__preco))

def alugar (self):
            if self.__tipo == 2:
                print ("{} so esta disponivel para venda".format(self.__titulo))
            elif self.__tipo == 1:
                self.__status = False 
                print ("Você alugou o livro {}".format(self.__titulo))
                print ("Sua conta inicial é de {}".format(self.__preco))
            else:
                print ("Operação não Disponivel")

def controlar_multa (self, data_de_aluguel, data_de_devolucao):
    if self.__tipo == 1:
        padrao = re.compile("[2-9]{4}[-]{1}[0-9]{2}[-]{1}[0-9]{2}")
        busca = padrao.search(data_de_aluguel, data_de_devolucao)
        if busca:
            devolucao = datetime.strptime(data_de_devolucao, '%Y-%m-%d')
            aluguel = datetime.strptime(data_de_aluguel, '%Y-%M-%d')
            quantidade_dias = abs((devolucao - aluguel).days)
            if quantidade_dias > 7:
                multa = 2.00
                for dia in quantidade_dias:
                    multa += 1
                    print ("Sua conta final é de {}".format(multa))
    else:
        print ("{} não esta disponivel para aluguel".format(self.__titulo))
            
def verificar_estoque_aluguel (self):
            if self.__tipo == 1:
                if self.__status == True:
                    print ("{} esta disponivel para aluguel".format(self.__titulo))
                elif self.__status == False:
                    print ("{} esta Indisponivel no momento".format(self.__titulo))
                else:
                    print ("Operação nao Disponivel")
            if self.__tipo == 2:
                print ("{} so esta disponivel para venda".format(self.__titulo))

def verificar_estoque_venda (self):
            if self.tipo == 2:
                if self.__status == True:
                    print ("{} esta disponivel para venda".format(self.__titulo))
                elif self.__status == False:
                    print ("{} esgotou".format(self.__titulo))
                else:
                    print ("Operacao nao Disponivel")
            if self.__tipo == 1:
                print ("{} so esta disponivel para aluguel".format(self.__titulo))


#-----------------------------------------------------------------------------------------------
superinteressante = Revista("Superinteressante - Mundo Aquatico", 60, 1, "Abril", 10.00, 2, True)
superinteressante.vender()
superinteressante.verificar_estoque_venda()
print ("-"*20)
metamorfose = Livro("A Metamorfose", 180, 4, "Leya", 13.00, 2, True)
metamorfose.vender()
metamorfose.verificar_estoque_venda()
print ("#"*30)
alice = Livro("Alice no País das Maravilhas", 200, 2, "Intriseca", 5.00, 1, True)
alice.alugar()




