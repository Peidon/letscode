from argparse import Namespace

from pkg import obj_storage
from moo.model_tool import *
import unittest


class TestS3Methods(unittest.TestCase):
    # def test_upper(self):
    #     self.assertEqual('foo'.upper(), 'FOO')
    #
    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())
    #
    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

    def test_bin(self):
        bi = b'1656511831'
        bis = str(bi)
        print(type(bi), bis)


if __name__ == '__main__':
    unittest.main()
