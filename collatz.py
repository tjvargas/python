def sequence_collatz(x):
    seq = [x]
    if x < 1:
       return []
    while x > 1:
       if x % 2 == 0:
         x = x / 2
       else:
         x = 3 * x + 1
       seq.append(x)
    return seq



def lista_entradas():
    lista_entradas = [];
    for i in range(1000000):
        lista_entradas.append(++i);
    return lista_entradas

# retorna a posição do maior item da lista
def maior_item_da_lista(seq):
    maior = 0
    i = 0
    while i < len(seq):
        if len(seq[i]) > len(seq[maior]):
            maior = i
        i = i + 1
    return maior;

import multiprocessing as mp
import time

if __name__ == '__main__':
    start = time.clock()
    cpus = mp.cpu_count()
    print(cpus)
    with mp.Pool(cpus) as p:
        lista = lista_entradas()
        maior_teim = p.map(sequence_collatz, lista)
        print(time.clock() - start);
        print(maior_item_da_lista(maior_teim))
        print(time.clock() - start);
