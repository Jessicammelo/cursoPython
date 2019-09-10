"""
Conjuntos
Conjuntos em linguagem de programação fazem referencia a conjuntos da matemática.
Em python conjuntos são sets.

Sets:
Não possuem valores duplicados;
Não possuem valores ordenados;
Não são indexados (não possui indice);

Usados para armazanar elemento que não precisem ser ordenados, quando não precisamos
nos preocupar com chaves, valores e itens duplicados.

 Os sets são referenciados com {}

 Diferença  entre conjuntos(sets)  e mapas (dicionários) em Python:
    -Um dicionário tem chave/valor;
    -Um conjunto tem apenas valor;

#definindo um conjunto
#forma 1
s = set({1, 2, 3, 4, 5, 5, 6,7, 2, 3}) #valores repetidos
print(s)
print(type(s))
 #Obs:Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
 #será ignorado sem gerar error e não fará parte do conjunto.

 #Forma 2 mais comum
s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

#Podemos verificar se determinado elemento está contido no conjunto

if 3 in s:
    print('Tem o 3')
else:
    print('Não tem 3')

# importante, não temos valores duplicados nem ordem:

#Listas aceitam valores duplicados
lista = [99, 25, 25, 36]
print(f'Lista: {lista} com {len(lista)} elementos')

#Tuplas  aceitam valores duplicados
tupla = 99, 25, 25, 36
print(f'tupla: {tupla} com {len(tupla)} elementos')

#Não aceitam valores chaves duplicadas
dicionario = {}.fromkeys([99, 25, 25, 36], 'dict')
print(f'dicionario: {dicionario} com {len(dicionario)} elementos')

#Não aceitam valores chaves duplicados
conjunto = {99, 25, 25, 36}
print(f'conjunto: {conjunto} com {len(conjunto)} elementos')

#Assim como todo outro conjunto Python podemos colocar tipos de dados misturados  em sets

s = {1, 'b', True, 34.2, 44}
print(s)
print(type(s))

#podemos iterar em ums et normalmente
for valor in s:
    print(valor)

#Usos interessantes com sets:
#Imagine que fisemos um formulario de cadastros de visitantes
#em uma feira e os visitantes informam manualmente a cidade de onde vieram.

#add cada cidade em uma lista python, uma lista pode add novos elementos e ter repetição

cidades = ['Blumenau', 'Joinvile', 'são Miguel', 'Lages', 'Blumenau']
print(cidades)
print(len(set(cidades)))
 #quantas cidades difentes temos?
 #oq vc faria ? Faria um lop na lista?
 #Podemos utilizar o set para isso.

#Add elementos em um conjuntos

s = {1, 2, 3}

s.add(4)
s.add(4) #Duplicidade não gera erro. Simplesmente é ignorado  e não é adcionado
print(5)


#Remover elementos em um conjuntos

s = {1, 2, 3}
print(s)

#forma 1
s.remove(3) # não é indice, é o valor a ser removido
print(s)

OBS: caso o valor não seja encontrado será gerado error

#forma 2
s.discard(22)
print(s)
#Obs: se o valor não é encontrado, nenhuem erro é gerado

#Copiando um conjunto para outro

s = {1, 2, 3}
print(s)

#forma 1  - Deep copy
novo = s.copy()
print(novo)

novo.add(4)

print(novo)
print(s)

#forma 2 - Shallow Copy
novo = s

novo.add(4)
print(novo)
print(s)


 #Podemos remover todos os itens de um conjunto
 s.clear()
print(s)

#Métodos Matematicos de conjuntos
#Imagine dois conjuntos

estudantes_python = {'alex', 'Juliano', 'matheus', 'leticia', 'ana'}
estudantes_java = {'alex', 'Juliano', 'matheus'}

#precisamso gerar um conjuntos com nomes unicos

#forma 1 - utilizando union

unicos1 = estudantes_python.union(estudantes_java)
#ou
unicos1 = estudantes_java.union(estudantes_python)
print(unicos1)

#forma 2 utilizando o papi => |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

#alguns alunos que estudam python tbm estudam java

#Gerar um conjunto de alunos que stão em ambos os cursos

#Forma 1  - utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

#Forma 2 utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)

#Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)


# Soma*, valorMaximo*, valorMinimo*, tamanho
# *Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))


"""



