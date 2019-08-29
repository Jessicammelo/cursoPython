"""
Estruturas Logicas

Operadores unarios:
    not
Operadores Binarios: E /Ou
    and-or-is

"""
ativo = False
logado = False

if ativo and logado:
    print('seja bem vindo')
else:
    print("Você precisa ativar sua conta")

if not ativo: # modelo pythonico
    print("Você precisa ativar sua conta")
else:
    print('seja bem vindo')

if ativo is False:
    print('seja bem vindo')
else:
    print("Você precisa ativar sua conta")

#ativo é True?
print(ativo is True)
#console
# nome = 'jessica'
#dir(nome)
