from decorators import time_it


class Problem:

    @staticmethod
    @time_it
    def solution():
        """Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral
         is formed as follows:

        21 22 23 24 25
        20  7  8  9 10
        19  6  1  2 11
        18  5  4  3 12
        17 16 15 14 13

        It can be verified that the sum of the numbers on the diagonals is 101.

        What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?
        """

        # === == === Solution === == ===  #

        target = 1001

        square_size = 1
        total_sum = 1
        increase_current_number_by = 2
        current_number = 1

        while square_size != target:
            for _ in range(4):
                current_number += increase_current_number_by
                total_sum += current_number
            square_size += 2
            increase_current_number_by += 2

        return f'total sum={total_sum}, square size={square_size}'


Problem.solution()  # Result: total sum=669171001, square size=1001
