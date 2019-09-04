"""
saindo de loops com break
"""
# ex: 1
for numero in range(1, 11):
    if numero == 6:
        break
    print(numero)
print('Sai do loop')

# ex: 2

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break