"""
Mapas  ->   Conhecemos em Python como dicionarios
Dicionarios em Python são repretesentados por chaves {}

receita = {'jan': 100, 'Fev': 250, 'Mar': 600}
print(receita)

#Interar sobre dicionarios
for chave in receita:
    print(chave)

for chave in receita:
    print(receita[chave])

for chave in receita:
    print(f'Em {chave} recebi R$ {receita[chave]}')

#acessando as chaves
print(receita.keys())

for chave in receita.keys():
    print(receita[chave])

#Acessando os valores
print(receita.values())

for valor in receita.values():
    print(valor)

#Desempacotamento de dicionarios
print(receita.items())
for chave, valor in receita.items():
    print(f'chave={chave} e valor={valor}')

"""
receita = {'jan': 100, 'Fev': 250, 'Mar': 600}
print(receita)

#Soma*, valor maximo*,valor minimo*, tamanho
#*Se os valores forem todos inteiros ou reais

print(sum(receita.values()))
print(max(receita.values()))
print(min(receita.values()))
print(len(receita))

