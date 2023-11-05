import unittest
import sys

sys.path.insert(1, '../../string/')

from string_utils import StringUtils

class TestStringUtilsMethods(unittest.TestCase):

    def test_left2(self):
        self.assertEqual(StringUtils.left2("Hello"), "lloHe")
        self.assertEqual(StringUtils.left2("java"), "vaja")
        self.assertEqual(StringUtils.left2("Hi"), "Hi")

    def test_combo_string(self):
        self.assertEqual(StringUtils.combo_string("Hello", "hi"), "hiHellohi")
        self.assertEqual(StringUtils.combo_string("hi", "Hello"), "hiHellohi")

    def test_first_half(self):
        self.assertEqual(StringUtils.first_half("José"), "Jo")

    def test_first_half_throws_exception_on_passing_name_len_odd(self):
        with self.assertRaises(Exception) as context:
            StringUtils.first_half("Diogo")

    def test_first_two(self):
        self.assertEqual(StringUtils.first_two("Hello"), "He")
        self.assertEqual(StringUtils.first_two("java"), "ja")
        self.assertEqual(StringUtils.first_two("Hi"), "Hi")

    def test_hello_name(self):
        self.assertEqual(StringUtils.hello_name("Rafaela"), "Hello Rafaela!")
        self.assertEqual(StringUtils.hello_name("Diogo"), "Hello Diogo!")

    def test_make_abba(self):
        self.assertEqual(StringUtils.make_abba("Hi", "Bye"), 'HiByeByeHi')

    def test_make_out_word(self):
        self.assertEqual(StringUtils.make_out_word("[[]]", "Diogo"), '[[Diogo]]')
        self.assertEqual(StringUtils.make_out_word("[[[[]]]]", "Diogo"), '[[[[Diogo]]]]')

    def test_make_tags(self):
        self.assertEqual(StringUtils.make_tags("i", "Hello World!"), "<i>Hello World!</i>")

    def test_extra_end(self):
        self.assertEqual(StringUtils.extra_end("Hello"), 'lololo')
        self.assertEqual(StringUtils.extra_end("ab"), 'ababab')
        self.assertEqual(StringUtils.extra_end("Hi"), 'HiHiHi')

    def test_without_end(self):
        self.assertEqual(StringUtils.without_end("Hello"), "ell")
        self.assertEqual(StringUtils.without_end("java"), "av")
        self.assertEqual(StringUtils.without_end("coding"), "odin")

if __name__ == '__main__':
    unittest.main()