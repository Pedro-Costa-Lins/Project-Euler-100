
from decorators import time_it


class Problem:

    @time_it
    def solution(number=100):

        """ Sem Square Difference
        The sum of the squares of the first ten natural numbers is:

        1² + 2² + ... + 10² = 385

        The square of the sum of the first ten natural numbers is:

        (1 + 2 + ... + 10)² = 55² = 3025

        Hence the difference between the sum of the squares of the
        first ten natural numbers and the square of the sum is:

        3025 - 385 = 2640

        Find the difference between the sum of the squares of the
        first one hundred natural numbers and the square of the sum.
        """

        # === == === Solution === == ===  #

        sum_sqr = 0
        sqr_sum = 0

        for i in range(1, number + 1):
            sum_sqr += (i**2)
            sqr_sum += + i

        sqr_sum **= 2

        return sqr_sum - sum_sqr


Problem.solution()  # Result: 25164150
