"""
Modulos colection - Default Dict

https://docs.python.org/3/library/collections.html#collections.defaultdict

# Recap Dicionarios
dicionario = {'curso': 'Programação em Python: essencial'
print(dicionario)
print(dicionario['curso'])
print(dicionario['outro']) #???KeyError

Default Dict -> Ao criar um dicionario utilizando-o, nós informamos um valor default,
podendo utilizar um lambda para isso. Esse valor será utilizado sempre que não houver
um valor definido. Caso tentemos acessar uma chave que não existe, essa chave será criada
e o valor default será atribuido.

OBs: Lambdas são funcoes sem nome, que podem ou não receber parametros de entrada e retornar
valores.


"""
#Fazendo import
from collections import defaultdict

dicionario = defaultdict(lambda: 0)
dicionario['curso'] = 'programação  em python: essencial'
print(dicionario)
print(dicionario['outro']) # KeyError no dicionario comum, mais aqui não
print(dicionario)