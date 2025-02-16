from decorators import time_it
from useful import is_palindrome


class Problem:

    @staticmethod
    @time_it
    def solution():
        """ The decimal number, 585 = 1001001001₂ (binary), is palindromic in both bases.

        Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

        (Please note that the palindromic number, in either base, may not include leading zeros.)
        """
        sum_of_all = 0
        for i in range(1_000_000):
            if is_palindrome(i) and is_palindrome(int(bin(i)[2:])):
                sum_of_all += i
        return sum_of_all

Problem.solution()  # Result: 872187
