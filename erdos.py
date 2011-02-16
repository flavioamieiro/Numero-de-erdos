import sys

INFINITO = sys.maxsize

class No:
    def __init__(self, nome, numero=None):
        self.co_autores = set()
        self.nome = nome
        self.numero = numero
        self.pai = None

    def update_co_autores(self, nos):
        self.co_autores.update(nos)
        self.co_autores.discard(self)

    def perfilhar_nos_em(self, nos):
        for no in nos:
            if no.nome != self.nome and \
               self.numero != INFINITO and \
               self.numero < no.numero:
                no.pai = self
                no.numero = self.numero + 1
                autores_a_perfilhar = no.co_autores - set([self])
                no.perfilhar_nos_em(autores_a_perfilhar)

    def __cmp__(self, other):
        if self.numero == other.numero:
            return 0
        elif self.numero < other.numero:
            return -1
        else:
            return 1

    def __repr__(self):
        return '{0} - {1}'.format(self.nome, self.numero)

    def __hash__(self):
        return hash(self.nome)

class Erdos(dict):

    def __init__(self, livros):
        self['Erdos'] = No('Erdos', 0)
        self.incluir_livros(livros)

    def incluir_livros(self, livros):
        for livro in livros:
            nos = list(map(lambda x: self.get(x, No(x, INFINITO)), livro))
            for no in nos:
                no.update_co_autores(nos)
                self[no.nome] = no

            min(nos).perfilhar_nos_em(nos)

    def numero_do(self, autor):
        return self[autor].numero
