## Algoritmo para descobrir o número que gera a maior sequência pela conjectura de collatz
import time

#Diferentemente do cache anterior, agora só guarda a quantidade de passos para cada número
def sequence_collatz(x, tab={}):
    steps = 0
    y = x
    if x < 1:
       return 0
    while x > 1:
       if x in tab:
         steps += tab[x]
         tab[y] = steps
         return steps
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       steps += 1
    tab[y] = steps
    return steps


def lista_entradas():
    return list(range(1,1000000,2)) #O maior número é sempre impar


# retorna a posição do maior item da lista
def maior_item_da_lista(tab):
  maior = 0
  maiork= 0
  for k,val in tab.items():
    if val > maior:
      maior = val
      maiork = k
  return maiork,maior


start = time.clock()
lista = lista_entradas()
tab = {};
for i in lista:
    (sequence_collatz(i,tab))
print(maior_item_da_lista(tab))
print(time.clock() - start)

