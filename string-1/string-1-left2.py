import unittest

class TestStringMethods(unittest.TestCase):

    def test_first_half(self):
        self.assertEqual(left2("Hello"), "lloHe")
        self.assertEqual(left2("java"), "vaja")
        self.assertEqual(left2("Hi"), "Hi")

def left2(a):
    return a[2:] + a[:2:]

if __name__ == '__main__':
    unittest.main()