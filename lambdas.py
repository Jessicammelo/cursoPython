"""
Utilizando Lambdas
Conhecidas por expressões Lambdas, ou simplesmente Lambdas, são funções sem nome,
ou seja, funções anonimas.

#Função em Paython:

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

#Expressão Lambda
lambda x: #Função em Paython:

def funcao(x):
    return 3 * x + 1

print(funcao(4))
print(funcao(7))

#Expressão Lambda
lambda x: 3 * x + 1

#como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))

#como utilizar a expressão lambda?
calc = lambda x: 3 * x + 1

print(calc(4))
print(calc(7))


#Podemos ter expressões lambdas com multiplos entradas
nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()
 # strip = remeve espaços
 #title = aplica letra maiuscula

print(nome_completo('angelina ', 'Jolie'))
print(nome_completo('  Felicity ', 'jones     '))

#Em funções Python podemos ter nenhuma ou varias entradas.Em lambdas tbm:

amar = lambda: ' Como não amar python'
uma = lambda x: 3 * x + 1
duas = lambda x, y: (x * y) ** 0.5
tres = lambda x, y, z: 3 / (1/ x + 1 / y + 1/z)
#n lambda x1, x1 ....xn: <expressão

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

#Obs|:
# Se passamos mais argumentos do que parametros esperados teremos TypeError

#Outro exemplo

autores = ['Isacc Assimov', 'Ray Bradbury']
print(autores)

autores.sort(Key=lambda  sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""
# Função quadratica

#f(x) = a * x ** 2 + b * x + c

#Definindo a função 
def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c

teste = geradora_funcao_quadratica(2, 3, -5)
print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(2))