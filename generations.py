"""
Generations Expression
Em aulas anteriores nós estudamos :
-List camprehension
-Dictionary Comprehension
- set Comprehension

Não vimos:
Tuple Comprehension...porque elas se chamam Generators

nomes = ['carlos', 'catarina', 'Catia', 'vanessa']

print(any([nome[0] == 'C' for name in names]))

#Poderiamos ter feito utilizando generations

nomes = ['carlos', 'catarina', 'Catia', 'vanessa']

print(any(nome[0] == 'C' for nome in nomes))

#List Comprehension
res = [nome[0] == 'C' for nome in nomes]
print(type(res))
print(res)

#generator
res = (nome[0] == 'C' for nome in nomes)
print(type(res))
print(res)

#Qual é a utilidade de getsizeof()?
Retorna  a quantidade de bytes em memoria do elemento passado como parametro
from sys import getsizeof

#Mostra quantos bytes a string 'jessy' está acupando em memoria. quanto maior a string, mais espaço ocupa.
print(getsizeof('jessy'))
print(getsizeof('University'))
print(getsizeof('9'))
print(getsizeof('91'))
print(getsizeof('4454654987987'))
print(getsizeof('True'))

from sys import getsizeof

#Gerando uma lista de numeros com list Comprehension
list_comp = getsizeof([x * 10 for x in range(1000)])

#gerando uma lista de numeros com set Comprehension
set_comp = getsizeof({x * 10 for x in range(1000)})

#gerando uma lista de numeros com Dictionary Comprehension
dic_comp = getsizeof({x: x * 10 for x in range(1000)})

#gerando uma lista de numeros com generator
gen = getsizeof(x * 10 for x in range(1000))

print('Para fazer a mesma tarefa gastamos em memoria:')
print(f'List Comprehension: {list_comp} bytes')
print(f'Set Comprehension: {set_comp} bytes')
print(f'Dictionary Comprehension: {dic_comp} bytes')
print(f'Generation Expression: {gen} bytes')



"""
#Eu posso iterar no Generator Expression? Sim

gen = (x * 10 for x in range(1000))
print(gen)
print(type(gen))

for num in gen:
    print(num)

