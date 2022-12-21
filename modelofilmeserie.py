class Programa:
    def __init__(self, nome, ano, genero):
        self._nome = nome.title()
        self.ano = ano
        self.genero = genero 
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes 


    def dar_likes(self):
        self.__likes += 1


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def __str__(self):
        return f'{self._nome} - {self.ano} - {self.genero}; Likes - {self.likes}'





class Filme(Programa):
    def __init__(self, nome, ano, genero, duraçao):
        super().__init__(nome, ano, genero)
        self.duraçao = duraçao

    def __str__ (self):
        return f'{self._nome} - {self.ano}, {self.duraçao} duração - {self.likes}'
    
    
class Serie(Programa):
    def __init__(self, nome, ano, genero, temporadas):
        super().__init__(nome, ano, genero)
        self.temporadas = temporadas
    
    def __str__(self):
        return f'{self._nome} - {self.ano}, {self.temporadas} temporadas - {self.likes}'


class Playlist():
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas
    
    def __getitem__ (self, item):
        return self._programas[item]


    @property
    def listagem(self):
        return self._programas

    def __len__ (self):
        return len(self._programas)

    

pearl = Filme("Pearl", 2022, "Terror", 100)
fleabag = Serie("Fleabag", 2016, "Dramédia", 2)
dogday = Filme("dog day afternoon", 1976, "Ação e drama", 120)
ianowt = Serie("i am not okay with this", 2020, "dramédia", 1)



pearl.dar_likes()
pearl.dar_likes()
pearl.dar_likes()
pearl.dar_likes()

fleabag.dar_likes()
fleabag.dar_likes()
fleabag.dar_likes()

dogday.dar_likes()
dogday.dar_likes()
dogday.dar_likes()

ianowt.dar_likes()
ianowt.dar_likes()



filmes_e_series = [pearl, fleabag, dogday, ianowt]
playlist_fim_de_semana = Playlist("fim de semana", filmes_e_series)

print (f'Tamanho da playlist: {len(playlist_fim_de_semana)}')

print (f'Está na lista: {pearl in playlist_fim_de_semana}')