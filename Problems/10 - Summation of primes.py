from decorators import time_it
from math import ceil, sqrt


def is_prime(number):
    for i in range(2, ceil(sqrt(number))+1):
        if number % i == 0:
            return False

    return True


class Problem:

    @time_it
    def solution(number=2_000_000):
        """ Summation of primes
        The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

        Find the sum of all the primes below two million.
        """

        # # Thoughts:
        #
        #     After 2, all subsequent primes are odd, only half of the numbers
        #     need to be tested.

        # === == === Solution === == ===  #

        i = 1
        total = 2
        
        while i < number:

            i += 1
            if is_prime(i):
                total += i

        return total


Problem.solution()  # Result: 142913828922
