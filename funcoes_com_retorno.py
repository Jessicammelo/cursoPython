"""
Funçoes com Retorno

"""
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


