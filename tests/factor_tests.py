from factors import Factors
import unittest

class FactorsTests(unittest.TestCase):

    def test_breakup_primes_return_same_value_if_prime_number(self):
        factors = Factors()

        result = factors.breakup_primes(5)

        self.assertEqual(5, result)

    def test_breakup_primes_return_same_value_if_other_prime_number(self):
        factors = Factors()

        result = factors.breakup_primes(11)

        self.assertEqual(11, result)

    def test_breakup_primes_return_factors_for_non_prime_number(self):
        factors = Factors()

        result = factors.breakup_primes(6)

        self.assertEqual([2,3], result)

    def test_breakup_primes_return_factors_for_other_non_prime_number(self):
        factors = Factors()

        result = factors.breakup_primes(9)

        self.assertEqual([3,3], result)

    def test_breakup_primes_return_factors_for_100(self):
        factors = Factors()

        result = factors.breakup_primes(100)

        self.assertEqual([2, 2, 5, 5], result)
        
    def test_breakup_primes_return_factors_for_198(self):
        factors = Factors()

        result = factors.breakup_primes(198)

        self.assertEqual([2, 3, 3, 11], result)

    def test_breakup_primes_return_factors_for_276(self):
        factors = Factors()

        result = factors.breakup_primes(276)

        self.assertEqual([2, 2, 3, 23], result)
