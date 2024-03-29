import unittest

class TestStringMethods(unittest.TestCase):

    def test_hello_name(self):
        self.assertEqual(hello_name("Rafaela"), "Hello Rafaela!")
        self.assertEqual(hello_name("Diogo"), "Hello Diogo!")

def hello_name(name):
    return "Hello " + name + "!"

if __name__ == '__main__':
    unittest.main()