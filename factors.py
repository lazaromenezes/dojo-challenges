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
        
        static_primes = [2, 3, 5, 7, 11, 13, 23]

        last_mod = None
        i = 0

        while not self.primes.is_prime(number):
            while i < len(static_primes):
                last_mod = number % static_primes[i]

                if last_mod != 0:
                    i += 1
                    continue
                
                factors.append(static_primes[i])
                number = int(number / static_primes[i])

        return factors




