from support_functions import is_prime
from super import Problem


class Problem003(Problem):

    def solution(self, number=600851475143):
        
        """ Largest Prime Factor
        The prime factors of 13195 are 5, 7, 13 and 29.

        What is the largest prime factor of the number 600851475143?
        """

        # === == === Solution === == ===  #

        # If the number is a factor and is Prime, it is the biggest.
        for i in range(3, number, 2):
            if not(number % i) and is_prime(number / i):
                return number / i