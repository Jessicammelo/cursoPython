"""
Funcoes com parametros (de entrada)

- Funções que recebem dados para serem processados dentro da mesa;
Se a gente pensar em um programa qualquer, geralmente temos:
entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funçoes que:
 -Não possuem entrada
 -Não possuem saída
 -Possuem entrada mas não possuem saída ;
 -Não possuem entrada mais possuem saída;
 -Possuem entrada e saida;


#Refatorando uma função

def quadrado(numero):
    #return numero * numero
    return numero**2

print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

ret = quadrado(6)
print(ret)

print(quadrado()) #TypeError

#Refatorando uma função

def cantar_parabens(aniversariante):
    print('parabens pra vc')
    print('parabens pra vc')
    print('parabens pra vc')
    print('parabens pra vc')
    print(f'Viva a/o {aniversariante}!')

cantar_parabens('Patricia')

#Funções podem ter n parametros de entrada, podemos receber como entrada
#em uma função quantos parametros forem necessarios. Eles são separados por vírgula.

#Exemplo

def soma(a, b):
    return a+b

def multiplica(num1, num2):
    return num1 * num2

def outra(num1, b, msg):
    return (num1 + b) * msg

print(soma(2, 5))
print(soma(10, 20))
print(multiplica(4, 5))
print(multiplica(2, 8))
print(outra(2, 5, 'Jessica'))
print(outra(5, 4, 'Melo'))

#OBS: Se infomar o numero errado da TypeError

#Nomeando parametros

def nome_completo(nome, sobrenome):
    return f'Seu nome completo é {nome}{sobrenome}'

print(nome_completo('Angelina', 'Jolie'))

#A diferença entre parametros  e argumentos
#Parametros são variaveis declaradas na definição de uma função;
#Argumentos são dados passados durante a execução de uma função;

#A ordem dos parametros importa!

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(nome, sobrenome))

#Argumentos nomeados (Keyword Argumentos)
#Caso utilizemos nomes dos parametros nos argumentos para informa-los,
# podemos utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

#Erro comum
def soma_impares(numeros):
    total = 0
    for num in numeros:
        if num % 2 != 0:
            total = total + num
    return total

lista = [1, 2, 3, 4, 5, 6, 7]
print(soma_impares(lista))

tupla = (1, 2, 3, 4, 5, 6, 7)
print(soma_impares(tupla))

"""
