
import numpy as np
from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution(number=4_000_000):

        """ Even Fibonacci Numbers
        Each new term in the Fibonacci sequence is generated by adding the previous 
        two terms. By starting with 1 and 2, the first 10 terms will be:

        1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

        By considering the terms in the Fibonacci sequence whose values do not exceed
        four million, find the sum of the even-valued terms.
        """

        # === == === Solution === == ===  #

        total: int = 2
        fibo = np.array([1, 2])
        i = 1
        not_finished = True

        while not_finished:
            # Fibonacci sequence
            fibo = np.append(fibo, fibo[i] + fibo[i-1])
            
            # Now 'fibo[i]' is the new generated member of the list.
            i += 1

            # If 'i' is even, add 'Fibo[i]' to 'total'.
            if fibo[i] % 2 == 0: total += fibo[i]

            # In order to the while to work, 'j' is now the last number on the sequence.
            if fibo[i] >= number:
                not_finished = False
        
        return total


Problem.solution()  # Result: 4613732
