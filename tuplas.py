"""
Tuplas ( tuple)

Tuplas são bastante parecidas com listas
Existem basicamente duas diferenças basicas:
1- As tuplas são representadas por parenteses()
2- Elas sõo imutaveis: isso significa que ao se criar um tupla ela não muda.
Toda operação em uma tupla gera uma nova tupla.


#cuidado 1: As tuplas são representadas por () , mais veja:
tupla1 = (1, 2, 3, 4, 5,6)
print(tupla1)

print(type(tupla1))

tupla2 = (1, 2, 3, 4, 5,6)
print(tupla2)

print(type(tupla2))

#cuidado 2 : Tuplas com 1 elemento

tuplas3 = (4) #Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tuplas4 = (4,) #Isso é uma tupla
print(tupla4)

print(type(tupla4))

#Conclusão: Podemos concluir que tuplas são definidas pela vigula não pelo uso do parentes.

(4) -> não pe tupla
(4,) -> tuplas
4, ->tuplas

#Podemos gerar uma tupla dinamicamente com range(inicio, fim, passo)
tupla = tuple(range(11))
print(tupla)
print(type(tupla))

#Desempacotamento de tupla
tupla = ('Jessica', 'Melo')
escola, curso = tupla

print(escola)
print(curso)
#obs: Gera erro (ValueError) se colocarmos um numero difente de elementos para desenpacotar.

#Métodos para adição e remoção de elementos nas tuplas são existem, dado o fato das
# tuplas serem imutáveis.

#Soma* , valor maximo* e minimo* e tamanho, vale a msma coisa
#Se os valores forem todos inteiros ou reais

tupla = (1, 2, 3, 4, 5, 6, 'b')
print(sum(tupla))
print(max(tupla))
print(min(tupla))
print(len(tupla))

#Concatenação de tuplas

tupla1 = (1, 2, 3)
print(tupla1)

tupla2 = (4, 5, 6)
print(tupla2)

tupla1 = (tupla1, tupla2) #Tuplas são imutaveis
print(tupla1)
print(tupla2)

tupla3 = tupla1 + tupla2
print(tupla1)
print(tupla2)
print(tupla3)

tupla1 = tupla1 + tupla2#Tuplas são imutaveis, mais podemos sobrescrever seus valores
print(tupla1)

#Verificar se  determinado elemento está contido na tupla
tupla = (1, 2, 3)
print(3 in tupla)

#Iterando sobre uma tupla
for n in tupla:
    print(n)

for indice, valor in enumerate(tupla):
    print(indice, valor)

#Contando elementos dentro de uma tupla
tupla = ('a', 'b', 'c', 'a')
print(tupla.count('a'))

escola = tuple('Jessica')
print(escola)

print(escola.count('e'))

meses.append('playstation') add
print(meses)

# O acesso  a elementos de uma tupla tambem é semelhante a de uma lista

print(meses[3])
#Interar com while
i = 0

while i < len(meses):
    print(meses[i])
    i = i + 1

#Dicas na utilização de tuplas
#Devemos usar tuplas SEMPRE que não precisarmos modificaros dados contidos em uma coleção
#Exemplo 1

meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio')#...
meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio']#...

#Slicing
#Tupla[inicio:fim:passo]
print(meses[5:9])

 #O acesso a elementos de uma tupla tambem é semelhante a de uma lista
print(meses[5])

#Verificamos em qual indice um elemento esta na tupla

print(meses.index('fevereiro'))

#Caso o elemento não exista será gerado erro.

#Por que utilizar Tuplas?
# São mais rapidas do que listas.
# Tuplas deixam seu codigo mais seguro
#* Isso porque trabalhar com elementos imutaveis traz segurança para o codigo.

# Copiando  uma tupla para outra
tupla = (1, 2, 3)
print(tupla)
nova = tupla #na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)
outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)

"""
