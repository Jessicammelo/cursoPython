"""
Modulos collections - Named tuple (tupla nomeada)

#Recap tupla

tupla = (1, 2, 3)

print(tupla[1])

Named Tuple -> São tuplas, diferenciadas, onde, especificamos um nome para a mesma e tambem um parametro


"""

#importando
from collections import namedtuple

#precisamos definir o nome para parametros

#forma 1 - Declaração Named tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

#forma 2 - Declaração Named tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

#forma 3 - Declaração Named tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])

#usando
ray = cachorro(idade=2, raca='chow-chow', nome='ray')
print(ray)

#acessando os dados

#Forma 1
print(ray[0]) #idade
print(ray[1]) #raça
print(ray[2]) #nome

#forma2
print(ray.idade) #idade
print(ray.raca) #raça
print(ray.nome)

print(ray.index('Chow-chow'))
print(ray.count('Chow-chow'))