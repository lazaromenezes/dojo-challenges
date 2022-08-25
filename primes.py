class Primes(object):

    def is_prime(self, number):
        if number >= 0 and number <= 2:
            return True
        
        if not self.__is_odd(number):
            return False
        
        for n in range(number - 1, 2, -1):
            if number % n == 0:
                return False

        return True

    def __is_odd(self, number):
        return number % 2 == 1
