"""
Dicionarios
obs:  algumas linguagens de programação, os dicionarios são conhecidos como mapas
#Dicionarios são coleções do tipo chave/valor.
#São representados por chaves{}

print(type({}))

Obs:Sobre:
  Chave e valor são separados por dois pontos ' chave: valor';
  Os dois podem ser de qualquer tipo de dado;
  Podemos misturar tipos de dados;

  #Criação de dicionarios
#Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print(paises)
print(type(paises))

#Forma 2 ( menos comum)
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')
print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}



#Acessando elementos
#Forma1  acessando via chave, da mesma forma que lista/tupla
print(paises['br'])
#print(paises['ru'])
#caso tentamos fazer uma acesso com uam chave que não exite, teremos um erro


#Forma 2 Acesso via get- recomendada
print(paises.get('br'))
#print(paises.get('ru'))

#Caso o get não encontre o objeto com a chave informada será retornado
 o valor None e não será gerado o KeyError

pais = paises.get('ru')
if pais:
    print(f'Encontrei o país {pais}')
else:
    print('Não encontrei o país')


#PODEMOS definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')
if pais:
    print(f'Encontrei o país {pais}')

#podemos verificar  se determinada chave se encontra em um dicionario

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguay'}
print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

if 'ru' in paises:
    russia = paises['ru']

# Podemos utilizar qualquer tipo de dado(int, float, String, booleam), inclusive lista,
tupla dicionario, como chaves de dicionario.

"""

