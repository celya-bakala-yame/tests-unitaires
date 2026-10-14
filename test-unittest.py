import unittest

class TestStringMethods(unittest.TestCase):

    def setUp(self):
        # Code de configuration qui sera exécuté avant chaque test
        pass

    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOO')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        with self.assertRaises(TypeError):
            s.split(2)

    def tearDown(self):
        # Code de nettoyage qui sera exécuté après chaque test
        pass

if __name__ == '__main__':
    unittest.main()