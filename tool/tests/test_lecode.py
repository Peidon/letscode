from solutions.array.kmp import Solution as kmp_so
import unittest


class TestLetCode(unittest.TestCase):
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

    def test_kmp(self):
        s = kmp_so()
        idx = s.str_index("abcbbc", "bbc")
        self.assertEqual(idx, 3)
        idx = s.str_index("leetcode", "leeto")
        self.assertEqual(idx, -1)
        idx = s.str_index("aaa", "aaaa")
        self.assertEqual(idx, -1)
        idx = s.str_index("mississippi", "issipi")
        self.assertEqual(idx, -1)


if __name__ == '__main__':
    unittest.main()
