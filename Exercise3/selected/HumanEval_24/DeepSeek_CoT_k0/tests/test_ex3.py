import unittest
from src.solution import largest_divisor

class TestLargestDivisorSpec(unittest.TestCase):

    def test_smallest_valid_input(self):
        self.assertEqual(largest_divisor(2), 1)

    def test_prime_number(self):
        self.assertEqual(largest_divisor(97), 1)

    def test_even_number(self):
        self.assertEqual(largest_divisor(28), 14)

    def test_composite_odd(self):
        self.assertEqual(largest_divisor(45), 15)

    def test_large_composite(self):
        self.assertEqual(largest_divisor(100), 50)

    def test_many_divisors(self):
        self.assertEqual(largest_divisor(36), 18)
