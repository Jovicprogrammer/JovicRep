class Livro():
    def __init__(self, titulo, qtdPaginas, autor):
        self.titulo = titulo
        self.qtdPaginas = qtdPaginas
        self.autor = autor

    def get_preco (self):
            return self.__preço 

    def set_preco (self, novo_preço):
            if type(novo_preço) == type(float()):
                self.__preço = novo_preço
            else:
                print ("Deve ser float!!")

    def __str__(self):
        return f' O livro {self.titulo} da autora {self.autor} possui {self.qtdPaginas} páginas e custa {self.get_preco()} reais.'

    preço = property(get_preco, set_preco)

        

rosa = Livro("A Bela e a Fera", 290, "Gabrielle-Suzanne de Villeneuve")

rosa.set_preco(20.00) 

print (rosa.get_preco())
print (rosa)