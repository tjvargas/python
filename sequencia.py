#
#  Algoritmo que retorna a sequência de caracteres que mais aparecem em sequência
#

string = "glooooobbbbbo.commmmm.br";

charAnterior = '';

sequencias = [];


def addSequencia(x):
    ultimaPosicao = len(sequencias)-1;
    ultimaSequencia = sequencias[ultimaPosicao];
    ultimoChar = ultimaSequencia[len(ultimaSequencia)-1];
    if ultimoChar == x :
        sequencias[ultimaPosicao] = ultimaSequencia + x;


def maiorSequencia(seq):
    maior = 0
    i = 0
    while i < len(seq):
        if len(seq[i]) > len(seq[maior]):
            maior = i
        i = i + 1
    return maior;

for i in range(len(string)):
    if i > 0:
        charAnterior = string[i-1]
        if string[i] == charAnterior:
            addSequencia(string[i])
        else:
            sequencias.append(string[i]);
    else:
        sequencias.append(string[i]);

print(sequencias[maiorSequencia(sequencias)]);