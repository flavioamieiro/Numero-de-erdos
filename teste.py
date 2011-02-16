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

if __name__ == '__main__':
    unittest.main()
