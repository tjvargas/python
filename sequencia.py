#
#  Algoritmo que retorna a sequência de caracteres que mais aparecem em sequência
#

class Sequencia():

    def __init__(self, string):
        self.string = string
        ## var auxiliar
        self.aux_char_anterior = ''
        ## lista auxiliar das sequencias
        self.sequencias = []

    # Adiciona caracteres na lista auxiliar, se repetir concatena
    def add_sequencia(self, x):
        ultima_sequencia = self.sequencias[-1];
        ultimo_char = ultima_sequencia[len(ultima_sequencia)-1];
        if ultimo_char == x :
            self.sequencias[-1] = ultima_sequencia + x;

    # retorna a posição do maior item da lista
    def maior_item_da_lista(self, seq):
        maior = 0
        i = 0
        while i < len(seq):
            if len(seq[i]) > len(seq[maior]):
                maior = i
            i = i + 1
        return maior;

    # percorre a string e adiciona na lista auxiliar.
    def run(self):
        for i in range(len(self.string)):
            if i > 0:
                self.char_anterior = self.string[i-1]
                if self.string[i] == self.char_anterior:
                    self.add_sequencia(self.string[i])
                else:
                    self.sequencias.append(self.string[i]);
            else:
                self.sequencias.append(self.string[i]);

        # imprime a maior sequencia de caracteres. Empates imprimem a primeira da esquerda para a direita
        print(self.sequencias[self.maior_item_da_lista(self.sequencias)]);

sequencia = Sequencia("gloooooobbbbbo.commmmmm.br")  #deve imprimir oooooo

sequencia.run()