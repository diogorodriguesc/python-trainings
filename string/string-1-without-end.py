import unittest

class TestStringMethods(unittest.TestCase):

    def test_without_end(self):
        self.assertEqual(without_end("Hello"), "ell")
        self.assertEqual(without_end("java"), "av")
        self.assertEqual(without_end("coding"), "odin")

def without_end(str):
    return str[1:len(str)-1]

if __name__ == '__main__':
    unittest.main()