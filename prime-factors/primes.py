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

    def next_prime(self, number):
        next_prime = number + 1
        
        while not self.is_prime(next_prime):
            next_prime += 1

        return next_prime

    def __is_odd(self, number):
        return number % 2 == 1
