import unittest
import main


class TestStringMethods(unittest.TestCase):

    def test_match(self):
        is_match = main.is_interleave('10110110110', '101', '0')
        self.assertTrue(is_match)

    def test_no_match(self):
        is_match = main.is_interleave('101111', '101', '0')
        self.assertFalse(is_match)

    def test_too_short(self):
        is_match = main.is_interleave('101', '101', '0')
        self.assertFalse(is_match)


if __name__ == '__main__':
    unittest.main()
