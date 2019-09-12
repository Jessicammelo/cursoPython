"""
Definindo funcoes

- Funcões são pequenos trechos de codigos que realizam tarefas especificas;
- Pode ou não receber entradas de dados  e retornar uma saída;
- Muito uteis para executar procedimentos similares por repetidos vezes
Já utilizamos:
    -print()
    -len()
    -max()
    -min()
    -count()
    -e outras;


"""
#exemplo de utilização de funçoes

cores = ['verdes', 'amarelo', 'azul', 'branco']

#utilizando a função integrada (Built-in) do Python print()

print(cores)
curso = 'Programação em python'
print(curso)

cores.append('roxo') #Usa em lista
print(cores)

#curso.append('mais dados')#AttributeError
#print(curso)

cores.clear()
print(cores)

print(help(print))

#DRY - don´t repeat Yourseft - não repita vc mesmo / não repita seu codigo.
#Mas então, como definir Funções?

"""
Em Python, a forma ideal para definir uma função é:
def nome_da_funcao(parametro_de_entrada):
    bloco_da_funcao
    
Onde:
nome_da_funcao -> sempre, com letras minusculas, e se for nome composto, separado por underline (snake case);
parametros_de_entrada -> Opcionais,onde tendo mais de um, cada um separado por vírgula, podendo ser opcionais ou não;
bloco_da_funcao -> Também chamado  de corpo da função ou implementação, é onde  o processamento da função acontece.
Neste bloco pode ter ou nãoretorno da função.

Obs: Veja que para definir uma função, utilizamos a paravra reservada 'def' informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utilizado e python
para definir  blocos


Definindo a primeira  função

definição:
def diz_oi():
    print ('oi')
    
    
OBS:
1 - Dentro de uma função podemos utilizar outras funções;
2 - Veja que nossa função executa somente uma tarefa;
3 - Veja que essa função não recebe nunhum parametro;
4 - Veja que essa função não retorna nada;


Utilizando funções:

chamada de execução:

diz_oi()

ATENÇÂO - nunca esqueça de usar o parenteses


Exemplo 2 

def cantar_parabens():
    print('parabens pra vc')
    print('parabens pra vc')
    print('parabens pra vc')
    print('parabens pra vc')
    
cantar_parabens()
cantar_parabens()
 ou 
for n in range(5):
    print(n)
    cantar_parabens()   


Em python podemos inclusive criar variaveis do tipo de uma função e executar  esta função atraves da variavel
canta = cantar_parabens
canta()
"""

