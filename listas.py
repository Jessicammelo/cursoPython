"""
Listas e Python funcionam com listas e matrizes
Dinamico pode se colocar qualquer tipo de dado!

#dinamico (não possui tamanho fixo)
#qualquer tipo de dado (recebi qualquer tipo de dado)

type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['j', 'e', 's', 's', 'i', 'c', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('jessica')

#listas são conchetes[]
type([])
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['j', 'e', 's', 's', 'i', 'c', 'a']
lista3 = []
lista4 = list(range(11))
lista5 = list('jessica')

#podemos identificar facilmente se determinado valor esta na lista
num = 7
if num in lista4:
    print(f'Encontrei o numero {num}')
else:
    print(f'Não encontrei o numero {num}')

#podemos facilmente ordenar uma lista
lista1.sort()
print(lista1)

#podemos facilmente contar o numero de ocorrencias de um valor em uma lista
print(lista1.count(1))
print(lista5.count('e'))

#adicionar elementos em listas

#para adicionar elementos em listas, usamos a função append
print(lista1)
lista1.append(42)
print(lista1)
#com append adicionamos apenas um elemento por vez
lista1.append([8, 3, 1])#coloca a lista  como elemento unico
print(lista1)

if [8, 3, 1] in lista1:
    print('Encontrei a lista')
else:
    print('Não encontrei a lista')

lista1.extend([123, 44, 67])#coloca cada elemento da lista como valor adicionar a lista
print(lista1)

#podemos inserir um novo elemento da lista informando a posição do indice
#isso não subistitui o valor inicial. O mesmo sera deslocado para a direita da lista.
lista1.insert(2, 'novo valor')
print(lista1)

#podemos facilmente juntar duas listas
#lista6 = lista1 + lista2
#lista1.extend(lista2)
print(lista1)

#forma 2
print(lista1[::-1])
print(lista2[::-1])

#podemos facilmente inverter duas listas

lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)


#copiar uma lista
lista6 = lista2.copy()
print(lista6)

#contar os elementos da lista
print(len(lista1))

#podemos remover facilmente o ultimo elemento de uma lista
#obs: O pop não somente remove o ultimo elemento mais tbm retorna
print(lista5)
lista5.pop()
print(lista5)

#podemos remover um elemento pelo indice
#obs: Os elementos á direita  desde indice serão deslocados para esquerda
#se não houver elemento no indice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

#podemos remover todos os elementos e zerar a lista
print(lista5)
lista5.clear()
print(lista5)

#podemos facilmente repetir elementos em uma lista
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)

#podemos facilmente converter uma string para uma lista
lista6 = ['Programação' ,'em', 'Python']
print(lista6)
 #exemplo 1
curso = 'Programação em Python'
print(curso)
curso = curso.split()
print(curso)

#obs: Por padrão, o split separa os elemento da lista pelo espaço entre elas
#exemplo 2
curso = 'Programação em Python'
print(curso)
curso = curso.split(',')
print(curso)

#podemos facilmente converter uma string para uma lista
lista6 = ['Programação', 'em', 'Python']
print(lista6)

#abaixo estamos falando: pega a lista6, coloca espaço entre cada elemento e transforma em uma string
curso = ' '.join(lista6)
print(curso)

#abaixo estamos falando: Pega a lista6 ,coloca cifrão entre cada elementoe transforma em uma string
curso = '$'.join(lista6)
print(curso)

#podemos realmente colocar qualquer tipo de dado em uma lista, inclusive misturando esses dados
lista6 = [1, 2.34, True, 'Jessy', 'd', [1, 2, 3], 546456456456]
print(lista6)
print(type(lista6))

#interando sobre uma listas
#exemplo 1 (utilizando for)
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(soma)

#exemplo 2 (uzando while)
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' pra sair:")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

#utilizando variaveis  em listas
numeros = [1, 2, 3, 4, 5]

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5

numeros = [num1, num2, num3, num4, num5]
print(numeros)

#fazemos acessos aos elementos de forma indexada
#           0          1        2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0]) #verde
print(cores[1]) #amarelo
print(cores[2]) #azul
print(cores[3]) #branco

# fazer acesso  aos elementos de forma indexada inversa
# Para entender melhor o indice negativo, pense na lista como um circulo,
# onde o final de um elemento está ligado ao inicio  da lista

print(cores[-1]) #branco
print(cores[-2]) #azul
print(cores[-3]) #amarelo
print(cores[-4]) #verde
#print(cores[-5]) # Erro, pois não existe -5 de indice

for cor in cores:
    print(cor)

indice = 0
while indice < len(cores):
    print(cores[indice])
    indice = indice + 1

#gerar indice em um for

for indice, cor in enumerate(cores):
    print(indice, cor)


# Listas aceitam valores repetidos
lista  = []
lista.append(42)
lista.append(42)
lista.append(33)
lista.append(33)
lista.append(42)
print(lista)

#metodos não muito importantes mais tbm uteis
#encontrar o indice  de um elemento na lista

numeros = [5, 6, 7, 5, 8, 9, 10]
#Em qual indice  da lista esta o valor 6?
print(numeros.index(6))

#Em qual indice  da lista esta o valor 6?
print(numeros.index(9))

#print(numeros.index(19)) dará erro
#Obs: caso não tenho esse elemento na lista, sera apresentado erro

print(numeros.index(5))# retorna o indice do primeiro elemento encontrado

#podemos fazer busca dentro de um range, ou seja, qual indice começar a buscar

print(numeros.index(5, 1))#buscando a partir  do indice 1
print(numeros.index(5, 2))#buscando a partir  do indice 2
print(numeros.index(5, 3))#buscando a partir  do indice 3
#print(numeros.index(5, 4))#buscando a partir  do indice 4
#Obs: caso não tenho esse elemento na lista, sera apresentado erro

#podemos fazer busca dentro de um range, inicio /fim
print(numeros.index(8, 3, 6))# buscar indice  do valor 8 , entre os indices 3 e 6


# Revisão do slicing
#lista[inicio:fim:passo]
#range(incio:fim:passo)

#trabalhando com slaicing de lista com parametro 'inicio'

lista = [1, 2, 3, 4]
print(lista[::])# iniciando  no indice 1  e pegando todos os elementos restantes

#trabalhando com slice de lista com o paraetro ' fim'
#console
#lista[1]
#lsita[3:]
#lista[-1:]

print(lista[:2]) # começa em 0, pega até o indice 2 - 1
print(lista[:4]) # começa em 0, pega até o indice 4 - 1
print(lista[1:3]) # começa em 1, pega até o indice 3 - 1

#trabalhando com slice de lista com o paraetro 'passo'

print(lista[1::2]) #Começa em 1, vai até o final, de 2 em 2
print(lista[::2]) #Começa em 0, vai até o final, de 2 em 2

#invertendo valores da lista
nomes = ['Jessica', 'Melo']
nomes[0], nomes[1] = nomes[1], nomes[0]
print(nomes)

nomes = ['Jessica', 'Melo']
nomes.reverse()
print(nomes)


#Soma*, valor maximo*, valor minimo*, tamanho
#* Se valores forem inteiros ou flutuantes ( reais)

lista = [1, 2, 3, 4, 5, 6]
print(sum(lista)) #Soma
print(max(lista)) #maximo valor
print(min(lista)) #minimo valor
print(len(lista)) #tamanho da lista

#Transformar uma lista em tupla
lista = [1, 2, 3, 4, 5, 6]
print(lista)
print(type(lista))

tupla = tuple(lista) #tuplas usam parenteses
print(tupla)
print(type(tupla))

#Desempacotamento de listas
lista = [1, 2, 3,]
num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)
#se tivermos um numero diferente de elementos na lista ou variaveis para receber  os dados, teremos valueError

"""


