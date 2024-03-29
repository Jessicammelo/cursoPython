"""
OBS:
A partir do python3+ a função reduce() não é mais uma função integrada ( built - in).
Agora temos que importar e utilizar esta função a partir do modulo 'functools'

Guido van Rossum: Utilize a função reduce()se vc realmente precisa dela.
Em todo caso, 99% dads vezes um loop for é mais legível.

Para entender o reduce()
# imagine que vc tem uma coleção de dados:
dados = [a1, a2, a3, ...an]

#Evc tem uma função que recebe dois parametros:
def funcao(x, y):
    return x * y

Assim como map() e filter(), a funçaõ reduce() recebe dois parametros: a funçaõ e o interavel.
 redece(funcao, dados)

 A função reduce(), funciona da seguinte forma:
    Passo 1: res1 = f(a1, a2) #Aplica a funçaõ nos dois primeiros elementos da coleção  e guarda o resultado.
    Passo 2: res2 = f(res1, a3) #Aplica a função passando o resultado do passo1 mais o terceiro elemento e
    guarda o res.

    Isso é repetido até o final.
    Passo 3: res3 = f(res2, a4)
    .
    .
    .
    Passo n: resn = f(resm, an)

    Então em cada passo ele aplica a funçaõ passando como primeiro argumento o resultado da aplicação anterior
    No final reduce() irá retornar o resultado final.

    Alternativamente, poderiamos ver a função reduce() como:
    funcao(funcao(funcao(a1, a2), a3), a4), ...), an)



"""
#Como funciona?
#Vamos utilizar a função reduce() para multiplicar todos os numeros de uma lista

from functools import reduce

dados = [2, 3, 4, 5, 7, 11, 13]

#Para utilizar o reduce() nós precisamos de uma função que recebadois parametros
multi = lambda x, y: x * y

res = reduce(multi, dados)
print(res)

#utilizando o loop normal

res = 1
for n in dados:
    res = res * n
print(res)