#recebendo dados do usuário
#input() tipo String tudo em aspas!

#print('qual o seu nome:')
#nome =input()
nome = input('qual seu nome:') #input ->entrada
#print('Seja bem vindo(a) %s' % nome )ou
#print('seja bem vindo(a) {0}'.format(nome))ou
print(f'Seja bem vindo(a) {nome}')

#print('qual sua idade?') #pergunta
#idade = input() #recebi
#idade = input('qual sua idade?') 
idade = int(input('qual sua idade?')) 

#processamento

#saida de dados
#print('A %s tem %s anos' % (nome,idade))ou
#print('A {0} tem {1} anos'.format(nome,idade))ou
print(f'A {nome} tem {idade} anos')

#int(idade) => cast
# cast é a conversão de um tipo de dado para outro
print(f'A {nome} nasceu em {2019-idade}')
