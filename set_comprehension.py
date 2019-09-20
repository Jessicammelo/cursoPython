"""
Set Comprehension

Lista = [1, 2, 3, 4, 5]
Set = {1, 2, 3, 4, 5}

"""
#Exemplos
numeros = {num for num in range(1, 7)}
print(numeros)

#outro exemplo
numeros = {x ** 2 for x in range(10)}
print(numeros)

#Desafio
# faça uma alteração pra ser dicionario não set

numeros = {x: x ** 2 for x in range(10)}
print(numeros)

#Para finalizar
letras = {letra for letra in 'Jessica melo'}
print(letras)