from decorators import time_it
from useful import clear_list_from_duplicates


class Problem:

    @time_it
    def solution():
        """ Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

        1634 = 1^4 + 6^4 + 3^4 + 4^4
        8208 = 8^4 + 2^4 + 0^4 + 8^4
        9474 = 9^4 + 4^4 + 7^4 + 4^4

         As 1 = 1^4 is not a sum it is not included.

        The sum of these numbers is 1634 + 8208 + 9474 = 19316.

        Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
        """

        full_list = []
        for number in range(10, 10_000_000):
            compare_to_number = 0
            for j in str(number):
                compare_to_number += (int(j)**5)
            if compare_to_number == number:
                full_list.append(number)

        return f'full list {full_list}, sum {sum(full_list)}'


Problem.solution()  # Result: full list [4150, 4151, 54748, 92727, 93084, 194979], sum 443839
