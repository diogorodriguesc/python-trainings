import unittest

class TestStringMethods(unittest.TestCase):

    def test_make_out_word(self):
        self.assertEqual(make_out_word("[[]]", "Diogo"), '[[Diogo]]')
        self.assertEqual(make_out_word("[[[[]]]]", "Diogo"), '[[[[Diogo]]]]')

def make_out_word(out, word):
    len_out = len(out)
    half_middle_out = int(len_out / 2)
    
    return out[:half_middle_out] + word + out[half_middle_out:]

if __name__ == '__main__':
    unittest.main()
