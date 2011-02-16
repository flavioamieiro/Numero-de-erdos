#-*- coding: utf-8 -*-
import unittest
from erdos import Erdos, INFINITO

class TestErdos(unittest.TestCase):

    def test_erdos_eh_zero(self):
        livros = [['Erdos']]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)

    def test_autor_nao_relacionado_eh_infinto(self):
        livros = [['Mané']]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Mané'), INFINITO)

    def test_erdos_eh_zero_e_autor_nao_relacionado_eh_infinto(self):
        livros = [['Mané'],
                  ['Erdos']]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Mané'), INFINITO)

    def test_varios_autores_infinitos(self):
        livros = [['Zé', 'Mané'],
                  ['Erdos']]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Mané'), INFINITO)

    def test_coautor_de_erdos_eh_1(self):
        livros = [['Erdos', 'Berrondo']]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)

    def test_coautor_de_Berrondo_eh_2(self):
        livros = [
            ['Erdos', 'Berrondo'],
            ['Berrondo', 'Flávio'],
        ]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)

    def test_coautor_de_Berrondo_eh_2_independente_da_ordem(self):
        livros = [
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)

    def teste_alguem_de_fora_escreve_com_alguem_de_dentro(self):
        livros = [
            ['A', 'B'],
            ['B', 'C'],
            ['C', 'D'],
            ['Berrondo', 'Flávio'],
            ['Erdos', 'Berrondo'],
        ]
        erdos = Erdos(livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('A'), INFINITO)
        self.assertEqual(erdos.numero_do('B'), INFINITO)
        self.assertEqual(erdos.numero_do('C'), INFINITO)
        self.assertEqual(erdos.numero_do('D'), INFINITO)

        novos_livros = [['B', 'Flávio']]
        erdos.incluir_livros(novos_livros)
        self.assertEqual(erdos.numero_do('Erdos'), 0)
        self.assertEqual(erdos.numero_do('Berrondo'), 1)
        self.assertEqual(erdos.numero_do('Flávio'), 2)
        self.assertEqual(erdos.numero_do('A'), 4)
        self.assertEqual(erdos.numero_do('B'), 3)
        self.assertEqual(erdos.numero_do('C'), 4)
        self.assertEqual(erdos.numero_do('D'), 5)



if __name__ == '__main__':
    unittest.main()
