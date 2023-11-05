import unittest

class TestStringMethods(unittest.TestCase):

    def test_extra_end(self):
        self.assertEqual(extra_end("Hello"), 'lololo')
        self.assertEqual(extra_end("ab"), 'ababab')
        self.assertEqual(extra_end("Hi"), 'HiHiHi')

def extra_end(str):
    return str[len(str)-2:] * 3

if __name__ == '__main__':
    unittest.main()
