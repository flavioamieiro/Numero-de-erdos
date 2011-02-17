#-*- coding: utf-8 -*-
import sys

INFINITO = sys.maxsize

class Autor:
    def __init__(self, nome, numero=INFINITO):
        self.co_autores = set()
        self.nome = nome
        self.numero = numero

    def update_co_autores(self, autores):
        self.co_autores.update(autores)
        self.co_autores.discard(self)

    def perfilhar_autores_em(self, autores):
        for autor in autores:
            if self.numero < autor.numero:
                # Eu estou mais perto de Erdos que o outro nó,
                # tenho autoridade para determinar o número dele.
                # Ele está na posição mais próxima possível de mim.
                autor.numero = self.numero + 1
                autor.perfilhar_autores_em(autor.co_autores)

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
        self['Erdos'] = Autor('Erdos', 0)
        self.incluir_livros(livros)

    def incluir_livros(self, livros):
        for livro in livros:
            autores = [self.get(nome, Autor(nome)) for nome in livro]
            for autor in autores:
                autor.update_co_autores(autores)
                self[autor.nome] = autor

            min(autores).perfilhar_autores_em(autores)

    def numero_do(self, autor):
        return self[autor].numero
