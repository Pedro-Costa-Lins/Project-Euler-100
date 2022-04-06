import math
from decorators import time_it


class Problem:

    @time_it
    def solution():

        """ Factorial digit sum
        n! means n × (n − 1) × ... × 3 × 2 × 1

        For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
        and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

        Find the sum of the digits in the number 100!
        """

        number_str = str(math.factorial(100))
        sum_of_numbers = 0

        for i in range(len(number_str)):
            sum_of_numbers += int(number_str[i])

        return sum_of_numbers


Problem.solution()  # Result: 648
