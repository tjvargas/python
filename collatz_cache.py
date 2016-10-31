import time

def cache(f):
    def func(args):
        if args not in func.cache:
            func.cache[args] = f(args)
        return func.cache[args]
    func.cache = {}
    return func


@cache
def sequence_collatz(x):
    if x == 1:
        seq = []
    elif x % 2 == 0:
        seq = sequence_collatz(x / 2)
    else:
        seq = sequence_collatz(3 * x + 1)
    return [x] + seq


def lista_entradas():
    lista_entradas = [];
    for i in range(1000000):
        if i%2!=0: #O maior número é sempre impar
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
    return seq[maior][0];


#if __name__ == '__main__':
start = time.clock()
lista = lista_entradas()
sequencia = [];
for i in lista :
    sequencia.append(sequence_collatz(i))
print(maior_item_da_lista(sequencia))
print(time.clock() - start)

