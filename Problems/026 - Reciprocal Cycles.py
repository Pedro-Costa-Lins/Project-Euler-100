from decorators import time_it


def cycle_spotter(target_limit):
    d = 1
    longest_sequence = 1

    for current_number in range(3, target_limit, 2):
        if current_number % 5 == 0:
            continue

        j = 1
        while (10 ** j) % current_number != 1:
            j += 1

        if j > longest_sequence:
            d, longest_sequence = current_number, j

    return f'd = {d}, longest_sequence: {longest_sequence}'


class Problem:

    @staticmethod
    @time_it
    def solution():

        """ A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators
        2 to 10 are given:

        1/2  = 0.5
        1/3  = 0.(3)
        1/4  = 0.25
        1/5  = 0.2
        1/6  = 0.1(6)
        1/7  = 0.(142857)
        1/8  = 0.125
        1/9  = 0.(1)
        1/10 = 0.1

        Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring
        cycle.

        Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
        """

        # === == === Solution === == ===  #

        target_limit = 1000
        return cycle_spotter(target_limit)


Problem.solution()  # Result: 983
