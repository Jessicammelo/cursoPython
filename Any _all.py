"""
Any e All

All() -> retorna true se todos os elementos do iteravel são verdadeiros ou ainda se o iteravel está vazio;


#Exemplo all()

print(all([0, 1, 2, 3, 4])) # Todos os numeros são verdadeiros?False

print(all([1, 2, 3, 4])) #Todos os numeros são verdadeiros?True

print(all([])) #todos os numeros são verdadeiros?True

print(all((1, 2, 3, 4))) #todos os numeros são verdadeiros?True

print(all({1, 2, 3, 4}))#todos os numeros são verdadeiros?True

print(all('jessy'))#todos os numeros são verdadeiros?True
nomes = ['camila', 'carlos', 'catharina']

print(all([nome[0] == 'C' for nome in nomes]))
print(all([letra for letra in 'eiof' if letra in 'aeiou']))

print(all([num for num in [4, 2,10, 6, 8] if num % 2 == 1]))


# algum - any() -> Retorna True se qualquer elemento do iterável for verdadeiro.
Se o iteravel estiver vazio, retorna False

print(any([0, 1, 2, 3, 4])) #True

nomes = ['camila', 'carlos', 'catharina']
print(any([nome[0] == 'C' for nome in nomes]))

print(any([num for num in [4, 2, 10, 6, 8, 9] if num % 2 == 0]))
"""





