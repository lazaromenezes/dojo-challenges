from primes import Primes
import unittest

class PrimesTests(unittest.TestCase):

    def test_zero_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(0))

    def test_one_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(1))

    def test_two_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(2))

    def test_three_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(3))

    def test_four_is_not_prime(self):
        primes = Primes()

        self.assertFalse(primes.is_prime(4))

    def test_five_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(5))

    def test_nine_is_not_prime(self):
        primes = Primes()

        self.assertFalse(primes.is_prime(9))

    def test_twenty_seven_is_not_prime(self):
        primes = Primes()

        self.assertFalse(primes.is_prime(27))

    def test_twenty_nine_is_prime(self):
        primes = Primes()

        self.assertTrue(primes.is_prime(29))

    def test_next_prime_from_two_is_three(self):
        primes = Primes()

        next_prime = primes.next_prime(2)

        self.assertEqual(3, next_prime)

    def test_next_prime_from_three_is_five(self):
        primes = Primes()

        next_prime = primes.next_prime(3)

        self.assertEqual(5, next_prime)

    def test_next_prime_from_four_is_five(self):
        primes = Primes()

        next_prime = primes.next_prime(4)

        self.assertEqual(5, next_prime)

    def test_next_prime_from_23_is_29(self):
        primes = Primes()

        next_prime = primes.next_prime(23)

        self.assertEqual(29, next_prime)
