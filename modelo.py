class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    def dar_likes(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def __str__(self):
        return f'Nome: {self._nome} Likes: {self.likes}'

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao

    def __str__(self):
        return f'Nome: {self._nome} - {self.duracao} - Likes: {self.likes}'

class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'Nome: {self._nome} - {self.temporadas} - Likes: {self.likes}'

class Playlist(list):
    def __init__(self, nome,Programa):
        self.nome = nome
        super().__init__(Programa)


vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Serie('atlanta', 2018, 2)
tmep = Filme("Todo mundo em pânico", 1999, 100)
demolidor = Serie("Demolidor", 2016, 2)


vingadores.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
demolidor.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
tmep.dar_likes()
vingadores.dar_likes()
vingadores.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()
atlanta.dar_likes()

listinha = [vingadores, atlanta, demolidor, tmep]
playlist_fim_de_semana = Playlist(f'Fim de semana', listinha)

print(f'Tamanho do playlist: {len(playlist_fim_de_semana)}')

for Programa in listinha:
    print(Programa)

