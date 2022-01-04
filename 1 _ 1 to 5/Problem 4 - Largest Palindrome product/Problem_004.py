import math


class problem_004(problem):


    def isPalindrome(number):
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


    def solution(number=3):
        
        """ Largest Palindrome
        A palindromic number reads the same both ways. The largest palindrome made from the 
        product of two 2-digit numbers is 9009 = 91 × 99.

        Find the largest palindrome made from the product of two 3-digit numbers.
        """

        # === == === Solution === == ===  #

        # The imput to solution is the lenght of the number witch is going to be used
        # Exp: 4 = 9999, 2 = 99

        # Setting of the range expected.
        nine = 0.99999999999999 
        ProductRange = int(math.ceil(nine * 10 ** number))
        
        Biggest = 1

        for i in range(int(ProductRange / 10), ProductRange):
            for j in range(i, ProductRange):
                if isPalindrome(i*j) and i*j > Biggest:
                    Biggest = i*j

        return Biggest