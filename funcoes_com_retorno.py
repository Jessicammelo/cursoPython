"""
Funçoes com Retorno

numeros = [1, 2, 3]
ret_pop = numeros.pop()
print(f'Retorno de pop: {ret_pop}')

ret_pr = print(numeros)
print(f'Retorno de print: {ret_pr}')

#Em python quando uma função não tem valor, o retorno é none.
#Funções python que retornam valores, devem retornar estes valores com a palavra reservada return
#Não precisamos necessariamente criar uma variavel para receber o retorno de uma função. Podemos
#passar a execução da função para outras funções.

#vamos refatorar está função para que ela retorne o valor


def quadrado_de_7():
    return 7 * 7

#criamos uma variavel para receber o retorno da função
ret = quadrado_de_7()
print(f'Retorno {ret}')

print(f'Retorno: {quadrado_de_7()}')

#Refatorando a primeira função


def diz_oi():
    print('oi')

#com return
    def diz_oi():
        return 'oi'

alguem = 'Pedro!'

diz_oi()
print(alguem)

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

#Exemplo 1 - Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado antes do retorn')
    return 'oi!'
    print('Estou sendo executado após o retorn')

    print(diz_oi())

#Exemplo 2 - Podemos ter em uma função diferentes returns;

def nova_funcao():
    variavel = false
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

print(nova_funcao())

#Exemplo 3 - Podemos, em uma função, retornar qualquer tipo de dado e até mesmo multiplos valores;

def outra_funcao():
    return 2, 3, 4, 5

#num1,num2, num3,num4 = outra_funcao()
#print(num1,num2,num3,num4)

print(outra_funcao())
print(type(outra_funcao()))

#Vamos criar uma função para jogar a moeda

from random import random

def joga_moeda():
    #gera um numero pseudo-randomico entre 0 e 1
    if random > 0.5:
        return 'cara'
    return 'coroa'

print(joga_moeda())

#Erros comuns na utilizaçõa dos retornos de uma função, codificação desnecessaria.

def eh_impar():
    numero = 5
    if numero % 2 != 0:
        return True
    return False

print(eh_impar())
"""

