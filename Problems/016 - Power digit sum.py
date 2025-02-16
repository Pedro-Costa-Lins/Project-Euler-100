import numpy as np
from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution(number=2**1000):

        """ Power digit sum
        2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

        What is the sum of the digits of the number 2^1000?
        """

        sum_of = str(number)

        sum_list = np.array([int(sum_of[i]) for i in range(len(sum_of))])

        return np.sum(sum_list)


Problem.solution()  # Result: 1366
