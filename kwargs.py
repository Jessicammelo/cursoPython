"""
**kwargs
Poderiamos chamar este parametro de **xix, mais por convenção
chamamos de kwargs
Esse é só mais um parametro, mais diferente do *args que coloca os valores extras
em uma tupla, o **kwargs exige que utilizamos parametros nomeados, e transforma esses
parâmetros  extras  em um dicionario.

#exemplo

def cores_favoritas(**kwargs):
    for pessoa, cor in kwargs.itens():
        print(f'A cor favorita de {pessoa.title()} é {cor}')

cores_favoritas(marcos='verde', fernanda='rosa', vanessa='azul')

#Os parametros *args e **kwargs não são obrigatorios

cores_favoritas()
cores_favoritas(jessy='oi')

#Exemplo mais complexo

def cumprimento_especial(**kwargs):
    if 'jessy' in kwargs['jessy'] =='Python':
        return 'Vc recebeu um cumprimento'
    elif 'jessy' in kwargs:
        return f"{kwargs['jessy']} Jessy"
    return 'Não tenho certeza...'

print(cumprimento_especial())
print(cumprimento_especial(jessy='Python'))
print(cumprimento_especial(jessy='oi'))
print(cumprimento_especial(jessy='especial'))

#Nas nossas funções, podemos ter:

-Parametros obrigatorio;
-*args;
-parametros default (não obrigatorios)
**kwargs

def minha_funcao(idade, nome, *args, solteiro=False, **kwargs ):
    print(f'{nome} tem {idade} anos')
    print(args)
    if solteiro:
        print('solteiro')
    else:
        print('casado')
        print(kwargs)

minha_funcao(8, 'julia')
minha_funcao(18, 'jessica', 4, 5, 6, solteiro=True)
minha_funcao(34, 'Felipe', eu='Não', voce='vai')
minha_funcao(19, 'carla', 9, 4, 3, java=False, python=True)


# Entenda pq é importante manter a ordem dos parametros na declaração

#Função com a ordem correta de parametros
#def mostra_info(a, b, *args, instrutor='jessy', **kwargs):
 #   return [a, b, args, instrutor, kwargs]


#Função com a orgem incorreta de parametros
def mostra_info(a, b, instrutor='jessy',*args, **kwargs):
  return [a, b, args, instrutor, kwargs]



a = 1
b = 2
args = (3,)
instrutor = 'jessy'
kwargs = {'sobrenome': 'University', 'cargo': 'Instrutor'}



print(mostra_info(1, 2, 3, sobrenome='University', cargo='Intrutor'))


#Desempacotar com **kwargs

def mostra_nomes(**kwargs):
    return f"{kwargs['nome']} {kwargs['sobrenome']}"

nomes = {'nome': 'Felicity', 'sobrenome': 'Jones'}
print(mostra_nomes(**nomes))

def soma_multiplos_numeros(a, b, c):
    print(a + b + c)

lista = [1, 2, 3]
tupla = (1, 2, 3)
conjunto = {1, 2, 3}
soma_multiplos_numeros(*lista)
soma_multiplos_numeros(*tupla)
soma_multiplos_numeros(*conjunto)

dicionario = dict(a=1, b=2, c=3)
soma_multiplos_numeros(**dicionario)

# OBS:
Os nomes da chave em um dicionario devem ser o mesmos dos parametros da função
dicionario = dict(d=1, e=2, f=3) #TypeError
soma_multiplos_numeros(**dicionario)

dicionario = dict(a=1, b=2, c=3, nome='Jessy')
soma_multiplos_numeros(**dicionario, lang='Python')

"""



