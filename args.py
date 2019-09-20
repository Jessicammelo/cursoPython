"""
Entendendo o *args

O args é um parametro, como outro qualquer.
Pode ser chamado de qualqer coisa;
Tem que começar com asterístico;

*xis

Mais por convenção, utilizamos *args para defini-lo

Mas oq são args?
O parametro *args utilizado em uma função, coloca os valores extras informados
como entrada em uma tupla. E lembre que tuplas são imutáveis.



#Exemplos

def soma_todos_numeros(num1=1, num2=2, num3=3, num4=4):
    return num1 + num2 + num3 + num4

print(soma_todos_numeros(4, 6, 9))

print(soma_todos_numeros(4, 6))
print(soma_todos_numeros(4, 6, 9, 5))

#Entendo o args

def soma_todos_numeros(*args):
    total = 0
    for numero in args:
        total = total + numero
     return total

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))


#Entendo o args com tuplas

def soma_todos_numeros(*args):
    return sum(args)

print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(2, 3, 4, 5))


#Entendo o args com tuplas

def soma_todos_numeros(nome, email, *args):
    return sum(args)

print(soma_todos_numeros('Jessica', 'Melo'))
print(soma_todos_numeros('Jessica', 'Melo', 1))
print(soma_todos_numeros('Jessica', 'Melo', 2, 3))
print(soma_todos_numeros('Jessica', 'Melo', 2, 3, 4))
print(soma_todos_numeros('Jessica', 'Melo', 2, 3, 4, 5))


#Outro exemplo  de utilização do *args

def verifica_info(*args):
    if 'jessi' in args and 'melo' in args:
        return 'bem vindos'
    return 'Eu n sei quem vc é'

print(verifica_info())
print(verifica_info(1, True, 'jessi', 'melo'))
print(verifica_info(1, 'jessi', 3.154))


def soma_todos_numeros(*args):
    return sum(args)

#print(soma_todos_numeros())
#print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7] #uma coleção, dicionario não

#Desempacotador
print(soma_todos_numeros(*numeros))

#print(soma_todos_numeros(numeros))

#OBS:
O asteristico serve para que informemos ao Python que estamos
passando como argumento uma coleção de dados. Desta forma, ele saberá
que precisará antes desempacotar estes dados.
"""
