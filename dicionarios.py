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

#tuplas por exemplo são bastante interessantes de serem utilizadas como chaves de dicionarios,
# pois as mesmas são imutáveis.

localidades = {
    (35.6985, 39.6917): 'Escritorio em Toquio',#coodenadas
    (35.6985, 39.6925): 'Escritorio em Nova Iorque',
    (35.6985, 39.2585): 'Escritorio em São Paulo',
}
print(localidades)
print(type(localidades))

#Adicionar elementos em um dicionario

receita = {'jan': 100, 'Fev': 250, 'Mar': 600}


#Forma 2:
novo_dado = {'mai': 500}
receita.update(novo_dado) #receita.update({'mai': 500})

#Atualizando dados em um dicionario
#Forma 1
receita['mai'] = 550
print(receita)

#Forma 2
receita.update({'mai': 400})
print(receita)

 #Conclusão 1:
 #A forma de adicionar novos elementos ou atualizar dados em um dicionario é a mesma.
 #Conclusão 2:
 #Em dicionarios não podemos ter chaves repetidas.

#Remover dados de um dicionario
receita = {'jan': 100, 'Fev': 250, 'Mar': 600}
print(receita)

#Forma 1 mais comum
ret = receita.pop('mar')
print(ret)

print(receita)

# Obs 1: Aqui precisamos sempre infirmar a chave, e caso não encontre o elemento, um KeyError
# é retornado.
# Obs 2: Ao removermos um objeto, o valor deste objeto pe sempre retornado.
#Forma 2

del receita['fev']
print(receita)
#del receita['abril'] se não exite sera gerado um erro.
#Obs: Neste caso o valor removido não é retornado.


#Imagine que você tem um comercio eletronico, onde temos um carrinho de compras na qual
#adicionamos produtos.

Carrinho de compras:
    Produto 1:
    -nome
    -quant
    -preço
    Produto 2:
   -nome
    -quant
    -preço

#Poderiamos usra uma lsita pra isso? Sim
carrinho = []
produto1 = ['Playstation 4', 1, 2300]
produto2 = ['God of war 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Teriamos quw saber qual é o indice de cada informação no produto
#2- Poderiamosutilizarr um tupla para fazer ?Sim

produto1 = ('Playstation 4', 1, 2300)
produto2 = ('God of war 4', 1, 150.00)
carrinho = (produto1, produto2)
print(carrinho)

##Teriamos que saber qual é o indice de cada informação no produto
#3- Poderiamosutilizarr um dicionario para fazer ?Sim

carrinho = []
produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preço': 230.00}
produto2 = {'nome': 'God of war 4', 'quantidade': 1, 'preço': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

#Dessa forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto
#podemos ter a certeza  sobre cada informação.


#Métodos de dicionarios
#console
#dir({})

d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Limpar o dicionario (Zerar dados)

d.clear()
print(d)

#Copiando um dicioanrio para outro
#Forma 1- deep copy

novo = d.copy()
print(novo)

novo['d'] = 4
print(d)
print(novo)

#Forma 2 #Shalow Copy

novo = d
print(novo)
novo['d'] = 4

print(d)
print(novo)


d = dict(a=1, b=2, c=3)
print(d)
print(type(d))

#Uma forma não usual de criação de dicionarios

outro = {}.fromkeys('a', 'b')
print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email'], 'desconhecido')
print(usuario)
print(type(usuario))

#O metodo fronkeys recebe dois parametros: um interavel e um valor
#Ele vai gera para cada valor de interavel uma chave e irá atribuir
# a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""
