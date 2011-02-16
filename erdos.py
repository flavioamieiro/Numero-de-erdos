import sys

INFINITO = sys.maxsize

class No:
    def __init__(self, nome, numero=INFINITO):
        self.nome = nome
        self.pai = None

    @property
    def numero(self):
        if self.nome == 'Erdos':
            return 0
        elif self.pai:
            return self.pai.numero + 1
        else:
            return INFINITO

    def perfilhar_nos_em(self, nos):
        for no in nos:
            no.pai = self

class Erdos(dict):

    def __init__(self, livros):
        self['Erdos'] = No('Erdos', 0)

        for livro in livros:
            nos = list(map(lambda x: self.get(x, No(x)), livro))
            for no in nos:
                self[no.nome] = no
                if no.nome == 'Erdos':
                    no.perfilhar_nos_em(nos)

    def numero_do(self, autor):
        return self[autor].numero
