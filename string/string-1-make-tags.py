import unittest

class TestStringMethods(unittest.TestCase):

    def test_make_tags(self):
        self.assertEqual(make_tags("i", "Hello World!"), "<i>Hello World!</i>")

def make_tags(tag, word):
    starting_tag = "<" + tag + ">"
    ending_tag = starting_tag[:1] + "/" + starting_tag[1:]

    return starting_tag + word + ending_tag

if __name__ == '__main__':
    unittest.main()