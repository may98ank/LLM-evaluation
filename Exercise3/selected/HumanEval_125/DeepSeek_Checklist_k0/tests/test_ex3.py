import unittest
from src.solution import split_words

class TestSplitWordsSpec(unittest.TestCase):

    def test_case_whitespace(self):
        self.assertEqual(split_words("a b c"), ["a", "b", "c"])

    def test_case_multiple_spaces(self):
        self.assertEqual(split_words("hello   world"), ["hello", "world"])

    def test_case_commas(self):
        self.assertEqual(split_words("x,y,z"), ["x", "y", "z"])

    def test_case_no_comma_no_space(self):
        self.assertEqual(split_words("abcdef"), 3)

    def test_case_mixed(self):
        self.assertEqual(split_words("a1b2c3d"), 2)

    def test_case_upper(self):
        self.assertEqual(split_words("XYZ"), 0)
