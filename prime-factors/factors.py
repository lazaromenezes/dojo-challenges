from primes import Primes

class Factors(object):

    def __init__(self):
        self.primes = Primes()

    def breakup_primes(self, number):
        if self.primes.is_prime(number):
            return number

        return self.__find_factors(number)

    def __find_factors(self, number):
        factors = []
        
        current_factor = 2

        while number > 1:
            last_mod = number % current_factor

            if self.__is_multiple(number, current_factor):
                factors.append(current_factor)
                number = int(number / current_factor)
            else:
                current_factor = self.primes.next_prime(current_factor) 

        return factors

    def __is_multiple(self, number, factor):
        return number % factor == 0



