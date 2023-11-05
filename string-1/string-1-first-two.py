import unittest

class TestStringMethods(unittest.TestCase):

    def test_first_half(self):
        self.assertEqual(first_two("Hello"), "He")
        self.assertEqual(first_two("java"), "ja")
        self.assertEqual(first_two("Hi"), "Hi")

def first_two(str):
  return str[:2:]

if __name__ == '__main__':
    unittest.main()