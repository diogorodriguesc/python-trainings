import unittest

class TestStringMethods(unittest.TestCase):

    def test_make_abba(self):
        self.assertEqual(make_abba("Hi", "Bye"), 'HiByeByeHi')

def make_abba(a, b):
    return a + b * 2 + a

if __name__ == '__main__':
    unittest.main()
