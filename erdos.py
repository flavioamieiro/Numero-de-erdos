import sys

INFINITO = sys.maxsize

class No:
    def __init__(self, nome, numero=None):
        self.nome = nome
        self._numero = numero
        self.pai = None

    @property
    def numero(self):
        if self._numero is None:
            if self.nome == 'Erdos':
                self._numero = 0
            elif self.pai:
                self._numero = self.pai.numero + 1
            else:
                self._numero = INFINITO
        return self._numero

    def perfilhar_nos_em(self, nos):
        for no in nos:
            if no.nome != self.nome and self.numero != INFINITO:
                no.pai = self
                no._numero = None

    def __cmp__(self, other):
        if self.numero == other.numero:
            return 0
        elif self.numero < other.numero:
            return -1
        else:
            return 1

    def __repr__(self):
        return '{0} - {1}'.format(self.nome, self.numero)

class Erdos(dict):

    def __init__(self, livros):
        self['Erdos'] = No('Erdos', 0)

        for livro in livros:
            nos = list(map(lambda x: self.get(x, No(x, INFINITO)), livro))
            for no in nos:
                self[no.nome] = no

            min(nos).perfilhar_nos_em(nos)

    def numero_do(self, autor):
        return self[autor].numero
