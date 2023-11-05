import unittest

class TestStringMethods(unittest.TestCase):

    def test_combo_string(self):
        self.assertEqual(combo_string("Hello", "hi"), "hiHellohi")
        self.assertEqual(combo_string("hi", "Hello"), "hiHellohi")

def combo_string(a, b):
    a_len = len(a)
    b_len = len(b)

    # Ternary - Awesome!
    short = a if a_len < b_len else b
    long = a if a_len > b_len else b

    return short + long + short

if __name__ == '__main__':
    unittest.main()