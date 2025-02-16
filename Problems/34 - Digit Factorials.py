
import math
from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ Digit Factorials

        145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

        Find the sum of all numbers which are equal to the sum of the factorial of their digits.

        Note: As 1! = 1 and 2! = 2 are not sums they are not included.
        """
        factorials = {
            '0': 1,
            '1': 1,
            '2': 2,
            '3': 6,
            '4': 24,
            '5': 120,
            '6': 720,
            '7': 5040,
            '8': 40320,
            '9': 362880
        }

        result = 0
        for number in range(3, 1_000_000_000):
            sum_of_factorials = 0
            for digit in str(number):
                sum_of_factorials += factorials[digit]

            if sum_of_factorials == number:
                result += number

        return result
        # Very, very bad performance


Problem.solution()  # Result: 40730
