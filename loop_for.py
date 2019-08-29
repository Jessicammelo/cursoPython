"""
Loop for
Loop: estrutura de repetição
for:
for item in interavel
     execução do loop
"""
"""
nome = 'Jessica Melo'
lista = [1, 3, 5, 7, 9]
numero = range(1, 10) #temos que tranformar em uma lista

#ex:
for letra in nome: #iterando em uma string
    print(letra)

#ex2
for numero in lista: #iterando sobre uma lista
     print(numero)

#ex3
# range [valor_inicial, valor_final]
# obs: o valor final não é inclusive {1 até 9}
for numero in range[1, 10]:#iterando sobre um range
    print(numero)

#enumerate:
# ((0, J),(1, e),(2, s),(3, s),(4, i)...)
for indice, letra in enumerate(nome):
    print(nome[indice])

for indice,letra in enumerate(nome):
    print(letra)

for _, letra in enumerate(nome):# quando querer descartar um valor colocar underline!
    print(letra)

for valor in enumerate(nome):
    print(valor)
"""

"""
nome = 'Jessica Melo'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10) #temos que tranformar em uma lista


qtd = int(input("quantas vezes esse loop deve rodar?"))
soma = 0
#for n in range(1, qtd):
    #print(f'imprimindo {n}')

for n in range(1, qtd+1):
    num = int(input(f'Informe o {n}/{qtd} valor:'))
    soma = soma + num
print(f'a soma é {soma}')

nome = "melo"
for letra in nome:
    #print(letra)#ou
    print(letra, end='')
"""

# original: U + 1F60D
#modificado: U0001F60D

for _ in range(3):
    for num in range(1, 11):
        print('\U0001F60D' * num)