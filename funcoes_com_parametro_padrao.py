"""
Funções com parametros padrão ( default Paramters)

- Funções onde a passagem de parametro seja opcional;

#Exemplo de função onde a passagem de parametro  seja opcional
print('Jessica Melo')

print()

#Exemplo de função onde a passagem de parametro seja obrigatoria;
def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # typeError


def exponencial(numero, potencia):
    return numero **potencia

print(exponencial(2, 3)) #2 * 2 * 2 = 8
print(exponencial(3, 2)) # 3*3 = 9

print(exponencial(3)) # Por favor eleve ao quadrado
print(exponencial(3, 5)) # Eleva  a potencia  informada  pelo usuario

#Obs:
#Se o usuario passar somente 1 argumento, este será atribuido ao parametro numero,
#e será calculado o quadrado deste numero;
#Se o usuario passar dois argumentos, o primeiro será atribuido ao parametro numero e o
# segundo ao parametro potencia, então será calculada essa potencia.

print(exponencial())

OBS:
#Em funções python, os parametros com valores default (padrão) devem sempre estra no final da declaração;

Error
def teste (potencia, num=2):
    return num ** potencia

print(teste(6))

#outros exemplos
def soma(num1=5, num2=3):
    return num1 + num2

print(soma(4, 3))
print(soma(4))
print(soma())

#Exemplo mais completo
def mostra_informacao(nome='Jessica', instrutor=false):
    if nome =='Jessica' and instrutor:
        return 'Bem vindo instrutor Jessica'
    elif nome=='Jessica':
         return 'Eu pensei que vc era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('ozzy'))
print(mostra_informacao(nome='Estafane'))

#Porque utilizar parametros com valor default?

-Nos permite ser mais flexiveis nas funções
-Evita erros com parametros incorretos
-Nos permite trabalhar com exemplos mais legiveis de código
-quais tipos de dados podemos utilizar como valores default para parametro?

-Qualquer tipo de dado:
    -Numeros, strings, floats, booleanos, listas, tuplas, dicionarios, funcões e etc;

def diz_oi():
    print('oi')
"""


