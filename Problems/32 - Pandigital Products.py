
from decorators import time_it
import itertools


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ Pandigital Products

        We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n  exactly once.
        For example, the 5-digit number, 15234, is 1 through 5 pandigital.

        The product 7254 is unusual, as the identity, 39 x 186 = 7254, containing multiplicand, multiplier, and product
        is 1 through 9 pandigital.

        Find the sum of all products whose multiplicand/multiplier/product identity can be written as a 1 through 9
        pandigital.

        HINT: Some products can be obtained in more than one way so be sure to only include it once in your sum.
        """

        # === == === Solution === == ===  #

        great_set = []
        digits = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        for _ in range(len(digits) + 1):
            for permutation in itertools.permutations('123456789', 9):

                for j in range(0, 4):
                    for k in range(j+1, j+5):

                        permutation_as_string = ''.join(permutation)

                        a = int(permutation_as_string[:j+1])
                        b = int(permutation_as_string[j:k])
                        c = int(permutation_as_string[k:])

                        if c == a * b and c not in great_set:
                            great_set.append(c)

        return sum(great_set)


Problem.solution()  # Result:
