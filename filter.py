"""
Filter
filter() ->Serve para filtrar dados de uma determinada coleção.

#Biblioteca para trabalhar com dados estatisticos
import statistics

# dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

#Calculando a media dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'Média: {media}')

#OBs: Assim como a função map(), a filter() recebe dois aparametros, sendo
#uma função e um iterável.

res = filter(lambda valor: valor > media, dados)
print(list(res))

#OBs: Assim com na funçaõ map(), apos serem utilizados os dados de filter() eles são excluidos da memória.

paises = ['', 'Argentina', '', 'Brasil']

#res = filter(lambda pais: len(país) > 0,paises)
#res = filter(None, paises)
res = filter(lambda pais: pais != '', paises)

print(list(res))

#a difernça entre map() e filter() é:
#map() -> Recebe dois parametros,uma função e um iteravel  e retorna um objeto mapeando a
# função para cada elemento do iteravel.

#filter() -> Recebe dois parametros, uma função e um iteravel e retorna um objeto filtrando
#apenas os elementos de acordo o a função.

#Exemplos mais complexos

usuarios = [
    {"username": "Samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "Carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "Samuel", "tweets": ["Eu gosto de cachorros"]},
    {"username": "Samuel", "tweets": []}
]
print(usuarios)

#Filtar os usuarios que stão inativos nao twitter

#Forma1
#inativos = list (filter(lambda usuario: len(usuarios['tweets'] == 0, usuarios))

#Forma2
inativos = list(filter(lambda usuario: not usuario['tweets'], usuarios))

print(inativos)

"""
#Combinar filter() e map()
nomes = ['vanessa', 'ana', 'maria']

#Devemos criar uma lista contendo 'Sua estrutura é ' + nome, desde cada nome tenha menos de 5 caracteres
lista = list(map(lambda nome: f'sua instrutora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

