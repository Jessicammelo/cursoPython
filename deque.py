"""
Modulos collections - Deque

Podemos dizer que uma lista de alta performance.


"""
#importa
from collections import deque

#Criando deques

deq = deque('jessy')
print(deq)

#Adicionando elementos  no deque

deq.append('y') #Adiciona no final
print(deq)

deq.appendleft('j') # Adiciona no inicio
print(deq)

#Remover elementos

print(deq.pop()) # remove e retorna o ultimo elemento

print(deq.popleft()) #Remove e retorna o primeiro elemento
print(deq)