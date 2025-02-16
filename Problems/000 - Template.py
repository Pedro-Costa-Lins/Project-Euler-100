
from decorators import time_it
from useful import is_palindrome
from useful import is_prime_brute_force


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ Template.

        So I can quickly copy.
        """

        # === == === Solution === == ===  #

        return is_palindrome(101), is_prime_brute_force(101)


Problem.solution()  # Result: (True, True)
