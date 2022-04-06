from decorators import time_it
from math import ceil, sqrt


def is_prime(number):
    for i in range(2, ceil(sqrt(number))+1):
        if not (number % i):
            return False

    return True


class Problem:

    @time_it
    def solution(number=10_001):

        """ 10001st prime
        By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13,
        we can see that the 6th prime is 13.

        What is the 10001st prime number?
        """

        # # Thoughts:
        #     After 2, all subsequent primes are odd, only half of the numbers
        #     need to be tested.

        counter = 3
        i = 5

        while counter < number:
            i += 2
            if is_prime(i):
                counter += 1

        return i


Problem.solution()  # Result: 104743
