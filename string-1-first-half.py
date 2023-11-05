import unittest

# Given a string of even length, return the first half. So the string "WooHoo" yields "Woo".

class TestStringMethods(unittest.TestCase):

    def test_first_half(self):
        self.assertEqual(first_half("José"), "Jo")

    def test_first_half_throws_exception_on_passing_name_len_odd(self):
        with self.assertRaises(Exception) as context:
            first_half("Diogo")

def first_half(str):
    len_str = len(str)
    half_str = len_str / 2

    if (half_str%2 != 0):
        raise Exception(str + " length is not even")

    half_str = int(half_str);

    return str[:half_str]

if __name__ == '__main__':
    unittest.main()