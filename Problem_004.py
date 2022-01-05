import math
from super import Problem


class Problem004(Problem):

    def is_palindrome(number):

        """Compares the digits until finding a difference, if it does,
        then it's not palindrome.
        """

        digits = str(number)

        # Compares the first digit to the last, the second to the before
        # the last an so on.
        for i in range(1, math.floor(len(digits) /2) +1):
            if digits[-i] != digits[i-1]:
                return False

        return True

    def solution(self, number=3):
        
        """ Largest Palindrome
        A palindromic number reads the same both ways. The largest palindrome made from the 
        product of two 2-digit numbers is 9009 = 91 × 99.

        Find the largest palindrome made from the product of two 3-digit numbers.
        """

        # === == === Solution === == ===  #

        # The input to solution is the length of the number witch is going to be used
        # Exp: 4 = 9999, 2 = 99

        # Setting of the range expected.
        nine = 0.99999999999999 
        product_range = int(math.ceil(nine * 10 ** number))

        biggest = 1

        for i in range(int(product_range / 10), product_range):
            for j in range(i, product_range):
                if self.is_palindrome(i * j) and i * j > biggest:
                    biggest = i*j

        return biggest
