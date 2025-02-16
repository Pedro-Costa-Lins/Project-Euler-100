
from decorators import time_it


def is_multiple(n, numbers):
    # If the 'n' is not multiple, it's ruled out.
    for j in range(numbers[0], numbers[1]):
        if n % j != 0:
            return False
    return True


class Problem:

    @staticmethod
    @time_it
    def solution(numbers=[11, 20]):

        """ Smallest Multiple
        2520 is the smallest number that can be divided by each of the numbers
        from 1 to 10 without any remainder.

        What is the smallest positive number that is evenly divisible by all
        of the numbers from 1 to 20?
        """

        # Thoughts:
        #   Should be even (Throughout iterations of an even number it is resolved)
        #   Should finish with 20, 40, 60, 80 or 00
        #   (Throughout iterations of 20 it is resolved)
        #   20, 19, 18, 17, 16, 15, 14, 13, 12, 11 are the only numbers to worry about.

        # === == === Solution === == ===  #

        not_found = True
        iteration = 20
        n = 20
        
        while not_found:
            if is_multiple(n, numbers):
                not_found = False
                continue
            n += iteration
        
        return n


Problem.solution()  # Result: 232792560
